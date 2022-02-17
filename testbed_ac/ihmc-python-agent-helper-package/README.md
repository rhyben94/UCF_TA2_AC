# IHMC's ASIST Agent Helper Library

The library provides a class which handles the heavy lifting of an ASIST agent.  It 
deals with managing the connection to the MQTT bus, provides methods to subscribe to
and publish topics.  Furthermore it makes sure your agent is a 'model citizen' in the
ASIST agent world by handling agent heart beats, version_info messages, and roll call 
messages in the background so all you have to worry about is your agent's specific code.

## Minimal ASIST Agent script using the `ASISTAgentHelper` Library
This is the agent helper library that does most of the heavy work of managing the MQTT bus.  To see how
it works let's look at a minimal script:

    # import the ASISTAgentHelper class
    from asistagenthelper import ASISTAgentHelper

    # Define the method to call when subscribed to messages are received
    def on_message(topic, header, msg, data, mqtt_message):
        print("Received a message on the topic: ", topic)
    
    # Initialize the helper class and tell it our method to call
    helper = ASISTAgentHelper(on_message)
    
    # Set the agent's status to 'up' and start the Main loop (which does not return)!!!
    helper.set_agent_status(helper.STATUS_UP)
    helper.run_agent_loop() 

That's it.  This is all you need to have a 'model citizen' agent which runs on the ASIST Testbed.  The
ASISTAgentHelper class handles connecting to the MQTT message bus, subscribing the to topics listed in 
a `config.json` and dealing with publishing the required heartbeat, versionInfo, and rollcall messages for 
you, so as long as you have the `version_info` set correctly in the `config.json` file, your agent is 
good to go. 

## ASISTAgentHelper Methods

These are the methods and variables provided for use by the ASISTAgentHelper class:

| Method/Variable | Description |
| --- | --- |
| agent_name | This variable holds the agent's name loaded from `settings.env`. |
| config_folder | This variable holds the path to the `ConfigFolder`. |
| is_connected() | Returns True if the agent is connected to the MQTT message bus, otherwise it returns False. |
| get_version_info() | Returns the version_info object read in from the `config.json` file. |
| get_logger() | Returns the logger.|
| generate_timestamp() | Helper method which returns an ASIST formatted timestamp string. |
| set_agent_state(state, message=None, active=True) | Sets the agent's state which can be 'ok', 'info', 'warn', 'error', or 'fail', an optional corresponding message if appropriate, and an optional active state (True or False).  This is reported to the system when heartbeat messages are published. (See `MessageSpec/Status`) |
| set_agent_status(status) | Sets the agent's status, which can be one of the following: "initializing", "up", "down", or "unknown".  The status is reported when a roll call message is published.  By default an agent's status is set to 'initializing'.  You should change it to 'up' when it is ready to run and then change it depending on your agent. (See `MessageSpece/Agent/rollcall`) |
| send_msg(topic, message_type, sub_type, sub_type_version, timestamp=None, data=None, trial_key=None, msg_version="1.1") | Publishes an ASIST formatted message (header, msg, data?) on the message bus. (If a trial key is not provided then the trial info for the msg section is obtained from the last trial topic message received.) |
| get_trial_key(msg) | If passed the `msg` part of a message bus message will return a trial key which can be used in the `send_msg` and `get_trial_info` methods. |
| get_trial_info(trial_key) | Returns the `data` part of the associated trail start message was received. (See `MessageSpecs/Trial`) |
| subscribe(topic, message_type=None, sub_type=None | Subscribes to the specified message bus topic. |
| unsubscribe(topic, message_type=None, sub_type=None | Unsubscribes from the specified message bus topic. |
| run_agent_loop() | This will start the agent loop which manages connecting to the MQTT bus and sending heartbeat messages. Note that this method will not return!! |
| start_agent_loop_thread() | Starts the agent loop on a separate thread. |
| stop_agent_loop_thread() | Stops the agent loop if it is running on a separate thread. |
