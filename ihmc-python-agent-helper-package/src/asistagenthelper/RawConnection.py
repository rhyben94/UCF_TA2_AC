#!/usr/bin/python
# -*- coding: utf-8 -*-
# pip install paho-mqtt

import os
import logging
import json
import paho.mqtt.client as mqtt

data = {"host": ["mosquitto", "127.0.0.1"], "port": "1883"}

configFolder = 'ConfigFolder'
if not os.path.exists(configFolder):
    configFolder = '../ConfigFolder'
if os.path.exists(configFolder):
    with open(configFolder + '/config.json') as config_file:
        data = json.load(config_file)

if 'port' not in data.keys():
    data['port'] = '1883'
if 'host' not in data.keys():
    data['host'] = ["mosquitto", "127.0.0.1"]
if type(data['host']) is not list:
    data['host'] = [data['host']]

broker = {

    # COMMENT THIS OUT WHEN NOT RUNNING FROM CONFIG.JSON FILE SETTINGS
    'host': os.getenv('MQTT_BROKER_HOSTNAME', '9999'),
    'port': int(os.getenv('MQTT_BROKER_PORT', data['port'])),

    # COMMENT THIS OUT WHEN RUNNING FROM CONFIG.JSON FILES (OUTSIDE OF DOCKER-COMPOSE)
    # 'host': os.getenv('MQTT_BROKER_HOSTNAME', 'host.docker.internal'),
    # 'port': int(os.getenv('MQTT_BROKER_PORT', '1883')),

    'keepalive': 60,
    'bind_address': os.getenv('MQTT_BROKER_BIND_ADDRESS', "")
}

if broker['host'] != '9999':
    data['host'].insert(0, broker['host'])
broker['host'] = data['host']

################################################################################
# RawMessage object

class RawMessage(object):
    def __init__(self, key, payload=None, jsondata=None):
        self.key = key
        self.payload = payload
        if jsondata:
            self.payload = json.dumps(jsondata).encode('utf-8')
    @property
    def jsondata(self):
        return json.loads(self.payload.decode("utf-8"))
    def __repr__(self):
        return f"RawMessage(key='{self.key}',payload={self.payload})"

################################################################################
# RawConnection class

class RawConnection(object):
    def __init__(self, clientid, host=broker['host'], port=broker['port'],keepalive=broker['keepalive'], bind_address=broker['bind_address']):
        self.__logger = logging.getLogger(__name__)
        self.__logger.info(f'Connection host {host} port {port}')
        self.__client_id = clientid
        self.__host = host
        self.__port = port
        self.__keepalive = keepalive
        self.__bind_address = bind_address
        self.__background_loop = False
        self.__mqttc = mqtt.Client(clientid)
        self.__mqttc.on_message = self.__on_message
        self.__mqttc.on_connect = self.__on_connect
        self.__mqttc.on_disconnect = self.__on_disconnect
        self.__onConnectionStateChange = None
        self.__onMessage = None

    # Callbacks
    def __on_connect(self, client, userdata, flags, rc):
        callback = self.onConnectionStateChange
        if callback:
            try:
                callback(True, rc)
            except Exception as ex:
                self.__logger.error('Failed connect callback', exc_info=True)
        else:
            self.__logger.info('connect rc {0}'.format(rc))

    def __on_disconnect(self, client, userdata, rc):
        callback = self.onConnectionStateChange
        if callback:
            try:
                callback(False, rc)
            except Exception as ex:
                self.__logger.error('Failed disconnect callback', exc_info=True)
        else:
            self.__logger.info('disconnect rc {0}'.format(rc))

    def __on_message(self, client, userdata, msg):
        callback = self.onMessage
        if callback:
            try:
                callback(RawMessage(msg.topic, msg.payload))
            except Exception as ex:
                self.__logger.error('Failed message callback', exc_info=True)
        else:
            self.__logger.info(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    @property
    def onConnectionStateChange(self):
        return self.__onConnectionStateChange

    @onConnectionStateChange.setter
    def onConnectionStateChange(self, value):
        """ Define the connection callback implementation.

        Expected signature is:
            onConnectionStateChange(isConnected, rc)

        isConnected : the client instance for this callback
        rc          : the connection result

        The value of rc indicates success or not:
            0: Connection successful
            1-255: Connection unsuccessful.
        """
        self.__onConnectionStateChange = value

    @property
    def onMessage(self):
        return self.__onMessage

    @onMessage.setter
    def onMessage(self, value):
        """ Define the message callback implementation.

        Expected signature is:
        onMessage(rawMessage)

        rawMessage : the raw message
        """
        self.__onMessage = value

    # Publish
    def publish(self, msg, qos=0, retain=False):
        self.__mqttc.publish(msg.key, msg.payload,qos=qos, retain=retain)

    # Subscribe
    def subscribe(self, topic):
        qos = 2
        print(f'subscribe {topic} qos = {qos}')
        self.__mqttc.subscribe(topic, qos=qos)

    # deliver messages that match subscription filter to callback.
    # only messages that don't match any callbacks will be delivered to onMessage callback.
    def message_callback_add(self,sub,callback):
        def my_callback(client, userdata, msg):
            try:
                callback(RawMessage(msg.topic, msg.payload))
            except Exception as ex:
                self.__logger.error('Failed message callback', exc_info=True)
        self.__mqttc.message_callback_add(sub,my_callback)

    # remove subscription callback
    def message_callback_remove(self,sub):
        self.__mqttc.message_callback_remove(sub)

    # Unsubscribe
    def unsubscribe(self, topic):
        self.__mqttc.unsubscribe(topic)

    # Connect
    def connect(self,start_loop=True):
        #print("host : " + broker.host)
        #print("port : " + broker.port)
        #print("bind_address : " + broker.bind_address)
        exp = None
        for host in self.__host:
            try:
                self.__mqttc.connect(host, port=self.__port, keepalive=self.__keepalive, bind_address=self.__bind_address)
                self.__background_loop = start_loop
                if start_loop:
                    self.__mqttc.loop_start()
                return
            except Exception as ex:
                exp = ex
        if exp is not None:
            raise exp

    def start_loop(self):
        self.__background_loop = True
        self.__mqttc.loop_start()

    def loop_forever(self):
        self.__mqttc.loop_forever()
    def loop(self):
        self.__mqttc.loop()

    # Disconnect
    def disconnect(self):
        if self.__background_loop:
            self.__mqttc.loop_stop()
            self.__background_loop = False
        self.__mqttc.disconnect()

    @property
    def clientId(self):
        return self.__client_id

################################################################################
