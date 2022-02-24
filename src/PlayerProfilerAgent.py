#!/usr/bin/env python3

"""
Simple ASIST Agent

Author: Roger Carff
email:rcarff@ihmc.us
"""
import os
import json
import uuid
from asistagenthelper import ASISTAgentHelper
import logging
from pprint import pprint
import PlayerModel

__author__ = 'rcarff'


def handle_trial_start(dat, exp_id, trial_id):
    PlayerModel.playerstate.handle_trial_start(dat['client_info'], exp_id, trial_id)


def handle_survey_message(dat, exp_id, trial_id):
    x = PlayerModel.playerstate.handle_survey_values(dat['values'], exp_id, trial_id)
    player_profile = x['player_profile']
    # collected = x['collected']
    # have_all = x['have_all']
    if player_profile:
        topic = f'agent/{helper.agent_name}/playerprofile'
        msg_type = 'agent'
        sub_type = 'playerprofile'
        sub_type_version = 0.1
        print('publishing player profile', player_profile)
        helper.send_msg(topic, msg_type, sub_type, sub_type_version, data=player_profile, trial_key=trial_id)


# This is the function which is called when a message is received for a to
# topic which this Agent is subscribed to.
def on_message(topic, header, msg, data, mqtt_message):
    global helper, extra_info, logger
    exp_id = msg['experiment_id']
    trial_id = msg['trial_id']
    # print('####')
    # pprint(header)
    # pprint(msg)
    # pprint(data)
    # pprint(mqtt_message)
    # print('-----\n')

    # Now handle the message based on the topic.  Refer to Message Specs for the contents of header, msg, and data
    if topic == 'trial' and msg['sub_type'] == 'start':
        # handle the start of a trial!!
        logger.info("Received a message on the topic: " + topic)
        logger.info(" - Trial Started with Mission set to: " + data['experiment_mission'])
        handle_trial_start(data, exp_id, trial_id)

    if msg['sub_type'] == 'Status:SurveyResponse':
        logger.info("Received a message on the topic: " + topic)
        handle_survey_message(data, exp_id, trial_id)

    # elif topic == 'observations/events/player/role_selected':
    #     minutes = int(data['elapsed_milliseconds'] / 1000 / 60)
    #     seconds = (data['elapsed_milliseconds'] / 1000) - (minutes * 60)
    #
    #     logger.info(" - At " + str(minutes) + ":" + str(seconds) + " into the mission " + data['participant_id'] + " selected the role: " + data['new_role'])
    #
    #     logger.info(" - Publishing a comment on the roll change!!")
    #     # use the info read in from the extra info file to form the comment
    #     if data['new_role'] in extra_info.keys():
    #         comment = extra_info[data['new_role']]
    #     else:
    #         comment = extra_info['default']
    #     comment = comment.format(data['new_role'])
    #
    #     # build up the message's data and publish it
    #     msg_data = {
    #         "id": str(uuid.uuid4()),
    #         "agent": helper.agent_name,
    #         "created": helper.generate_timestamp(),
    #         "start": -1,
    #         "content": comment,
    #         "receivers": [data['participant_id']],
    #         "type": 'string',
    #         "renderers": ["Minecraft_Chat"],
    #         "explanation": {"reason": "Role change caused a snarky remark from the agent."}
    #     }
    #     helper.send_msg("agent/intervention/"+helper.agent_name+"/chat",
    #                     "agent",
    #                     "Intervention:Chat",
    #                     "0.1",
    #                     timestamp=msg['timestamp'],
    #                     data=msg_data)


# Agent Initialization
helper = ASISTAgentHelper(on_message)

# Set the helper's logging level to INFO
LOG_HANDLER = logging.StreamHandler()
LOG_HANDLER.setFormatter(logging.Formatter("%(asctime)s | %(name)s | %(levelname)s — %(message)s"))
helper.get_logger().setLevel(logging.INFO)
helper.get_logger().addHandler(LOG_HANDLER)

# Create our own logger for the MoreComplexAgent
logger = logging.getLogger(helper.agent_name)
logger.setLevel(logging.INFO)
logger.addHandler(LOG_HANDLER)

# examples of manually subscribing and unsubscribing to topics
helper.subscribe('observations/events/player/tool_used')
helper.unsubscribe('observations/events/player/triage', 'event', 'Event:Triage')

# load extra info from the ConfigFolder for use later
extra_path = os.path.join(helper.config_folder, 'extraInfo.json')
extra_info = {}
if os.path.exists(extra_path):
    with open(extra_path) as extra_file:
        extra_info = json.load(extra_file)
if "default" not in extra_info.keys():
    extra_info["default"] = "I guess {0} is an okay role."

# Set the agents status to 'up' and start the agent loop on a separate thread
helper.set_agent_status(helper.STATUS_UP)
logger.info("Starting Agent Loop on a separate thread.")
helper.start_agent_loop_thread()
logger.info("Agent is now running...")

# if you need to do anything else you can do it here and if you want to stop the agent thread
# you can run the following, but until the agent loop is stopped, the process will continue to run.
#
# helper.stop_agent_loop_thread()
