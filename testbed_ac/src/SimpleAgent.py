#!/usr/bin/env python3

"""
VERY Simple ASIST Agent

Author: Roger Carff
email:rcarff@ihmc.us
"""

from asistagenthelper import ASISTAgentHelper

__author__ = 'rcarff'

# This is the function which is called when a message is received for a
# topic which this Agent is subscribed to.  Topics subscribed to can be
# specified in the ConfigFolder/config.json file or by using the
# helper.subscribe(topic) function.
def on_message(topic, header, msg, data, mqtt_message):
    print("Received a message on the topic: ", topic)
    print(" - header:", header)
    print(" - msg:", msg)
    print(" - data: ", data)

# Initialization
helper = ASISTAgentHelper(on_message)

# Set the agent's status to 'up' and start the Main loop (which does not return)!!!
print("Starting")
helper.set_agent_status(helper.STATUS_UP)
helper.run_agent_loop()
