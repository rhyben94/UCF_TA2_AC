#!/usr/bin/env python3

"""
ASISTAgentHelper Class

Author: Roger Carff
email:rcarff@ihmc.org
"""

import os
import time
import json
import uuid
import logging
import threading
from datetime import datetime
from .RawConnection import RawConnection, RawMessage

__author__ = 'rcarff'


class ASISTAgentHelper(object):
    STATUS_INITIALIZING = "initializing"
    STATUS_UP = "up"
    STATUS_DOWN = "down"
    STATUS_UNKNOWN = "unknown"

    STATE_OK = "ok"
    STATE_INFO = "info"
    STATE_WARN = "warn"
    STATE_ERROR = "error"
    STATE_FAIL = "fail"

    def __init__(self, on_message_handler):
        self.__logging = logging.getLogger(__name__)
        self.agent_name = os.getenv('AGENT_NAME', 'Unknown_ASIST_Agent')
        self.__agent_helper_version = os.getenv('AGENT_HELPER_VERSION', '0.1.4')
        self.__agent_start_time = datetime.now()
        self.__agent_status = self.STATUS_INITIALIZING
        self.__agent_state = self.STATE_OK
        self.__agent_state_msg = None
        self.__agent_state_active = True
        self.__heartbeat_every_n_sec = 10
        self.__last_heartbeat_time = self.__agent_start_time
        self.__agent_loop_thread = None
        self.__agent_loop_running = False

        # load the agent version info from the config file
        self.__version_info = {"owner": "Unknown", "version": "0.0.0"}
        self.config_folder = 'ConfigFolder'
        if not os.path.exists(self.config_folder):
            self.config_folder = '../ConfigFolder'
        if os.path.exists(self.config_folder):
            with open(self.config_folder + '/config.json') as config_file:
                data = json.load(config_file)
                if "version_info" in data.keys():
                    self.__version_info = data["version_info"]
                if "heartbeats_per_minute" in data.keys() and type(data["heartbeats_per_minute"]) == int or float:
                    self.__heartbeat_every_n_sec = int(60 / data["heartbeats_per_minute"])
        self.__version_info['agent_name'] = self.agent_name
        if 'version' not in self.__version_info.keys():
            self.__version_info['version'] = "0.0.0"
        if 'owner' not in self.__version_info.keys():
            self.__version_info['owner'] = 'Unknown'
        if 'dependencies' not in self.__version_info.keys():
            self.__version_info['dependencies'] = []
        self.__version_info['dependencies'].append("ASISTAgentHelper_v" + self.__agent_helper_version)

        self.__subscribe_topic_list = []
        if "subscribes" in self.__version_info.keys():
            for sub in self.__version_info['subscribes']:
                if 'topic' in sub and sub['topic'] not in self.__subscribe_topic_list:
                    self.__subscribe_topic_list.append(sub['topic'])
        # Always listen for trial and roll call requests.
        if 'trial' not in self.__subscribe_topic_list:
            self.__subscribe_topic_list.append('trial')
        if 'agent/control/rollcall/request' not in self.__subscribe_topic_list:
            self.__subscribe_topic_list.append('agent/control/rollcall/request')

        # start the MQTT bus pub/sub system
        self.__connected_to_mqtt = False
        self.__trial_infos = {}
        self.__message_bus = RawConnection(self.agent_name+":"+str(uuid.uuid4()))
        self.__message_bus.onConnectionStateChange = self.__on_connection
        self.__message_bus.onMessage = self.__on_message
        self.__on_message_handler = on_message_handler
        self.__tried_to_connect = False

    # Returns the version_info dictionary read in from the config file
    def get_version_info(self):
        return self.__version_info

    def get_logger(self):
        return self.__logging

    # Subscribe to a topic
    def subscribe(self, topic, message_type=None, sub_type=None):
        # Update Version Info's subscribes list
        sub = {"topic": topic}
        if message_type is not None:
            sub["message_type"] = message_type
        if sub_type is not None:
            sub["sub_type"] = sub_type
        found_it = False
        for csub in self.__version_info['subscribes']:
            if csub == sub:
                found_it = True
                break
        if not found_it:
            self.__version_info['subscribes'].append(sub)

        # Now subscribe to the topic if not already subscribed.
        if topic not in self.__subscribe_topic_list:
            self.__subscribe_topic_list.append(topic)
            if self.__connected_to_mqtt:
                self.__message_bus.subscribe(topic)
                self.__logging.debug("Subscribed to topic: " + topic)

    # Unsubscribe to a topic
    def unsubscribe(self, topic, message_type=None, sub_type=None):
        # Update Version Info's subscribes list
        sub = {"topic": topic}
        if message_type is not None:
            sub["message_type"] = message_type
        if sub_type is not None:
            sub["sub_type"] = sub_type
        unsubscribe = True
        for csub in self.__version_info['subscribes']:
            if csub == sub:
                self.__version_info['subscribes'].remove(sub)
            elif csub["topic"] == topic:
                # do not unsubscribe from the topic if another subscribes item with the same topic exists.
                unsubscribe = False

        if unsubscribe and topic in self.__subscribe_topic_list and topic not in ["trial"]:
            self.__subscribe_topic_list.remove(topic)
            if self.__connected_to_mqtt:
                self.__message_bus.unsubscribe(topic)
                self.__logging.debug("Unsubscribed from topic: " + topic)

    def set_agent_state(self, state, message=None, active=True):
        if state is None or state not in [self.STATE_OK, self.STATE_INFO, self.STATE_WARN, self.STATE_ERROR, self.STATE_FAIL]:
            return False
        self.__agent_state = state
        self.__agent_state_msg = message
        self.__agent_state_active = active
        return True

    def set_agent_status(self, status):
        if status is None or status not in [self.STATUS_INITIALIZING, self.STATUS_UP, self.STATUS_DOWN, self.STATE_ERROR]:
            return False
        self.__agent_status = status
        return True

    # returns an ASIST happy timestamp string for the current date and time
    @staticmethod
    def generate_timestamp():
        return str(datetime.utcnow().isoformat()) + 'Z'

    @staticmethod
    def __generate_asist_header(message_type, timestamp=None, msg_version="1.1"):
        if message_type is None:
            message_type = "unknown"
        if timestamp is None:
            timestamp = ASISTAgentHelper.generate_timestamp()
        return {
            "timestamp": timestamp,
            "message_type": message_type,
            "version": msg_version
        }

    # Publish an ASIST message to the message bus with the given info
    #  - If timestamp is None a new timestamp will be generated
    #  - If data is None, then no 'data' part will be sent
    #  - If trial_key is None (default) then the latest running trial info (experiment_id, trial_id, replay_id, ...)
    #    will be used in the 'msg' object.  If it is specified, then it will be used to generate this info.
    #  - msg_version defaults to 1.1 if it is not passed in
    def send_msg(self, topic, message_type, sub_type, sub_type_version, timestamp=None, data=None, trial_key=None, msg_version="1.1"):
        json_dict = {"header": self.__generate_asist_header(message_type, timestamp, msg_version), "msg": {}}

        json_dict["msg"]["sub_type"] = sub_type
        json_dict["msg"]["version"] = sub_type_version
        json_dict["msg"]["source"] = self.agent_name
        json_dict["msg"]["timestamp"] = json_dict["header"]["timestamp"]

        if trial_key is None or trial_key not in self.__trial_infos.keys():
            # look up the latest running trial from the list and use it
            for tkey in reversed(list(self.__trial_infos.keys())):
                if self.__trial_infos[tkey]['trial_running']:
                    trial_key = tkey
                    break
            # if no running trial found, just use the last trial added.
            if trial_key is None and len(self.__trial_infos) > 0:
                trial_key = list(self.__trial_infos.keys())[-1]

        if trial_key is not None and trial_key in self.__trial_infos.keys():
            trial_info = self.__trial_infos[trial_key]
            json_dict["msg"]["experiment_id"] = trial_info['experiment_id']
            json_dict["msg"]["trial_id"] = trial_info['trial_id']
            if trial_info['replay_root_id'] is not None:
                json_dict["msg"]["replay_root_id"] = trial_info['replay_root_id']
            if trial_info['replay_id'] is not None:
                json_dict["msg"]["replay_id"] = trial_info['replay_id']

        if data is not None:
            json_dict["data"] = data

        self.send_message_generic(topic, json_dict)

    # Publish an MQTT message to the message bus with the given topic and JSON Dictionary
    def send_message_generic(self, topic, json_dict):
        if topic is None or json_dict is None:
            return
        self.__message_bus.publish(RawMessage(topic, jsondata=json_dict))

    # Returns the MQTT bus connection state.
    def is_connected(self):
        return self.__connected_to_mqtt

    # This method reconnects to the message bus if disconnected.
    # It should be called routinely by anyone using this helper class
    def check_and_reconnect_if_needed(self):
        if not self.__connected_to_mqtt:
            try:
                self.__message_bus.connect()
            except Exception as ex:
                if not self.__tried_to_connect:
                    self.__logging.warning("- Failed to connect, MQTT Message Bus is not running!!")
                    self.__tried_to_connect = True
        else:
            self.__tried_to_connect = False

            # if trial is running see if it is time to send out a heartbeat
            trial_running = False
            for trial in self.__trial_infos.values():
                if trial['trial_running']:
                    trial_running = True
                    break

            current_time = datetime.now()
            if (current_time - self.__last_heartbeat_time).total_seconds() > self.__heartbeat_every_n_sec:
                self.__last_heartbeat_time = current_time
                if trial_running:
                    self.__publish_heartbeat_message()
                else:
                    self.__logging.debug("Not sending Heartbeat because no trial is running.")

        time.sleep(0.1)
        return

    def run_agent_loop(self):
        self.__logging.info("Starting ASIST Agent Loop: " + self.agent_name)
        self.__logging.debug(self.__version_info)
        self.__agent_loop_running = True
        self.__logging.info("Starting the MQTT Bus pub/sub system...")
        while self.__agent_loop_running:
            self.check_and_reconnect_if_needed()
            time.sleep(0.1)
        self.__agent_loop_thread = None

    def start_agent_loop_thread(self):
        if self.__agent_loop_thread is not None:
            return
        self.__agent_loop_thread = threading.Thread(target=self.run_agent_loop)
        self.__agent_loop_thread.start()

    def stop_agent_loop_thread(self):
        self.__agent_loop_running = False

    # MQTT Connection callback
    #   Called when connected to or disconnected from the MQTT Message bus
    def __on_connection(self, is_connected, rc):
        if self.__connected_to_mqtt == is_connected:
            return

        self.__connected_to_mqtt = is_connected
        if self.__connected_to_mqtt:
            self.__logging.info('- Connected to the Message Bus.')
            for topic in self.__subscribe_topic_list:
                self.__message_bus.subscribe(topic)
                self.__logging.debug('- subscribed to topic: ' + topic)
        else:
            self.__logging.info('- Disconnected from the Message Bus!!')

    @staticmethod
    def get_trial_key(msg):
        if msg is None or 'trial_id' not in msg.keys():
            return None
        trial_key = msg['trial_id']
        if 'replay_id' in msg and not msg['replay_id'] is None:
            trial_key = trial_key + ":" + msg['replay_id']
        return trial_key

    def get_trial_info(self, trial_key):
        if trial_key is None or trial_key not in self.__trial_infos.keys():
            return None
        return self.__trial_infos[trial_key]

    # MQTT Message callback
    #  Called when there is a message on the message bus for a topic which we are subscribed to
    def __on_message(self, message):
        try:
            topic = message.key
            header = message.jsondata['header'] if 'header' in message.jsondata else {}
            msg = message.jsondata['msg'] if 'msg' in message.jsondata else {}
            data = message.jsondata['data'] if 'data' in message.jsondata else {}

            self.__logging.debug("topic: " + topic)
            if msg is not None:
                self.__logging.debug("msg: " + str(msg))
            if data is not None:
                self.__logging.debug("data: " + str(data))

            # handle 'trial' messages and retain trail info for future reference
            if topic == 'trial':
                trial_key = self.get_trial_key(msg)
                if msg['sub_type'] == 'start':
                    trial_info = data
                    trial_info['experiment_id'] = msg['experiment_id']
                    trial_info['trial_id'] = msg['trial_id']
                    trial_info['replay_id'] = msg['replay_id'] if 'replay_id' in msg.keys() else None
                    trial_info['replay_root_id'] = msg['replay_root_id'] if 'replay_root_id' in msg.keys() else None
                    trial_info['trial_running'] = True
                    self.__trial_infos[trial_key] = trial_info

                    self.__publish_agent_version_message(trial_key)

                elif msg['sub_type'] == 'stop' and trial_key in self.__trial_infos.keys():
                    self.__trial_infos[trial_key]['trial_running'] = False

            # handle Roll Call requests
            elif topic == 'agent/control/rollcall/request' and \
                    'sub_type' in msg.keys() and msg['sub_type'] == 'rollcall:request' and \
                    data is not None and 'rollcall_id' in data.keys():
                self.__publish_rollcall_message(data['rollcall_id'], self.get_trial_key(msg))
                # do not pass on roll call requests to the 'on_message_handler' callback
                return

            self.__logging.debug("Received message for topic: " + topic)
            self.__logging.debug(message.jsondata)

            self.__on_message_handler(topic, header, msg, data, message.jsondata)

        except Exception as ex:
            self.__logging.exception(str(ex))
            self.__logging.error(str(ex))
            self.__logging.error('RX Error, topic = {0}'.format(topic))

    def __publish_agent_version_message(self, trial_key):
        self.__logging.debug("Publishing Agent Version Message.")
        self.send_msg("agent/" + self.agent_name + "/versioninfo", "agent", "versioninfo", "0.1", trial_key=trial_key, data=self.__version_info, msg_version="0.6")

    def __publish_rollcall_message(self, rollcall_id, trial_key):
        data = {
            "rollcall_id": rollcall_id,
            "version": self.__version_info['version'],
            "status": self.__agent_status,
            "uptime": (datetime.now() - self.__agent_start_time).total_seconds()
        }
        self.send_msg("agent/control/rollcall/response", "agent", "rollcall:response", "0.1", trial_key=trial_key, data=data, msg_version="0.6")
        self.__logging.debug("Published roll call response for rollcall_id: " + rollcall_id)

    def __publish_heartbeat_message(self):
        data = {
            "state": self.__agent_state
        }
        if self.__agent_state_msg is not None:
            data['status'] = self.__agent_state_msg
        if not self.__agent_state_active:
            data['active'] = False
        self.send_msg("status/" + self.agent_name + "/heartbeats", "status", "heartbeat", "0.3", data=data, msg_version="0.1")
        self.__logging.debug("Published heartbeat.")
