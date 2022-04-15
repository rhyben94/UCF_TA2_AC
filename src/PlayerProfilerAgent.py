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
    PlayerModel.playerstate.handle_trial_start(dat, exp_id, trial_id)


def publish_complete_state(complete_state, trial_id):
    topic = f'agent/{helper.agent_name}/playerprofile_complete_state'
    msg_type = 'agent'
    sub_type = 'playerprofile:completestate'
    sub_type_version = 0.1
    print(f'Publishing complete state of AC: PlayerProfile {trial_id}')
    print(f'complete_state: {complete_state}')
    helper.send_msg(topic, msg_type, sub_type, sub_type_version, data=complete_state, trial_key=trial_id)


def send_message(player_profile, trial_id):
    topic = f'agent/{helper.agent_name}/playerprofile'
    msg_type = 'agent'
    sub_type = 'playerprofile'
    sub_type_version = 0.1
    print('send_message publishing player_profile')
    pprint(player_profile)
    helper.send_msg(topic, msg_type, sub_type, sub_type_version, data=player_profile, trial_key=trial_id)


def handle_survey_message(dat, exp_id, trial_id):
    x = PlayerModel.playerstate.handle_survey_values(dat['values'], exp_id, trial_id)
    player_profile = x['player_profile']
    # collected = x['collected']
    # have_all = x['have_all']
    if player_profile:
        print(f'handle_survey_message publishing player profile')
        send_message(player_profile, trial_id)
        PlayerModel.playerstate.handle_static_player_profile(player_profile)


def update_time(dat, trial_id):
    if 'elapsed_milliseconds' in dat:
        elapsed_ms = dat['elapsed_milliseconds']
        ret = PlayerModel.playerstate.update_elapsed(elapsed_ms)
        # if not ret:
        #     pprint(f'Issue updating elapsed time.\nBad message {m}')
        check_and_handle_180_timeout(trial_id)


def check_and_handle_180_timeout(trial_id):
    timed_out_180 = PlayerModel.playerstate.check_180_timeout()
    if timed_out_180:
        PlayerModel.playerstate.handle_180_timeout()
        # print(f'Timedout 180 data {PlayerModel.playerstate.last_factor_window}')
        for pid, p in PlayerModel.playerstate.players.items():
            if 'update_180' in p:
                print('for participant_id', pid)
                pprint(p['update_180'])
                print()
                PlayerModel.playerstate.set_dynamic_profile(pid, p)
                player_profile = PlayerModel.make_dynamic_player_profile_message(pid, p)
                print('check_and_handle_180_timeout publishing dynamic player_profile')
                # pprint(player_profile)
                send_message(player_profile, trial_id)
        print()


# This is the function which is called when a message is received for a to
# topic which this Agent is subscribed to.
competency_count = 0


def on_message(topic, header, msg, data, mqtt_message):
    global helper, extra_info, logger, competency_count
    exp_id = msg['experiment_id']
    trial_id = msg['trial_id']
    sub_type = msg['sub_type']
    message_type = header['message_type']
    # print('####')
    # pprint(header)
    # pprint(msg)
    # pprint(data)
    # pprint(mqtt_message)
    # print('-----\n')

    update_time(data, trial_id)
    # print(f'topic {topic}')
    # logger.info("Received a message on the topic: " + topic + ' sub_type: ' + sub_type)
    # Now handle the message based on the topic.  Refer to Message Specs for the contents of header, msg, and data
    if topic == 'trial' and sub_type == 'start':
        # handle the start of a trial!!
        print("Received a message on the topic: " + topic)
        print(" - Trial Started with Mission set to: " + data['experiment_mission'])
        handle_trial_start(data, exp_id, trial_id)

    if topic == 'trial' and sub_type == 'stop':
        # handle the stop of a trial!!
        print("Received a message on the topic: " + topic)
        print(" - Trial Stopped with Mission set to: " + data['experiment_mission'])
        # FIXME for docker
        complete_state = PlayerModel.playerstate.handle_trial_stop(data, exp_id, trial_id, 'agent')
        publish_complete_state(complete_state, trial_id)

    if sub_type == 'Status:SurveyResponse':
        # logger.info("Received a message on the topic: " + topic)
        handle_survey_message(data, exp_id, trial_id)

    if sub_type == 'Event:CompetencyTask':
        competency_count = competency_count + 1
        print(f'competency_count {competency_count}')
        PlayerModel.playerstate.handle_competency_task(data, exp_id, trial_id)

    if sub_type == 'Event:MissionState':
        PlayerModel.playerstate.handle_mission_state(data)

    if sub_type == 'Event:Triage':
        # logger.info("Received a message on the topic: " + topic)
        PlayerModel.playerstate.handle_event_triage(data, exp_id, trial_id)

    if sub_type == 'Event:RubbleDestroyed':
        # logger.info("Received a message on the topic: " + topic)
        PlayerModel.playerstate.handle_rubble_destroyed(data, exp_id, trial_id)

    if sub_type == 'Event:VictimEvacuated':
        # logger.info("Received a message on the topic: " + topic)
        PlayerModel.playerstate.handle_victim_evacuated(data, exp_id, trial_id)

    if sub_type == 'Event:VictimPickedUp':
        # logger.info("Received a message on the topic: " + topic)
        PlayerModel.playerstate.handle_victim_picked_up(data, exp_id, trial_id)

    if sub_type == 'Event:VictimPlaced':
        # logger.info("Received a message on the topic: " + topic)
        PlayerModel.playerstate.handle_victim_placed(data, exp_id, trial_id)

    if message_type == 'observation' and sub_type == 'state':
        PlayerModel.playerstate.handle_obs_state(data, exp_id, trial_id)

    if sub_type == 'Event:PlanningStage':
        PlayerModel.playerstate.handle_planning_event(data, exp_id, trial_id)

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
helper.set_use_header_time(True)

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
# helper.subscribe('observations/events/player/tool_used')
# helper.unsubscribe('observations/events/player/triage', 'event', 'Event:Triage')

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
