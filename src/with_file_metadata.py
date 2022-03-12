#!/usr/bin/env python3

# Copyright 2022 Dynamic Object Language Labs Inc.
# DISTRIBUTION STATEMENT C: U.S. Government agencies and their contractors.
# Other requests shall be referred to DARPA’s Public Release Center via email at prc@darpa.mil.

# Run this command as below: The argument must be a .metadata file or directory containing metadata files.
# ./with_file_metadata.py qid.metadata

import argparse
from pathlib import Path
import metadata_utils
import PlayerModel
from pprint import pprint


def process_metadata_file(fname):
    print('Working on file', fname)
    msgs = metadata_utils.read_file(fname)
    print(f'Got msgs {len(msgs)}')
    for m in msgs:
        msg = m['msg']
        header = m['header']
        dat = m['data']
        exp_id = msg['experiment_id']
        trial_id = msg['trial_id']
        message_type = header['message_type']
        sub_type = msg['sub_type']

        if 'elapsed_milliseconds' in dat:
            elapsed_ms = dat['elapsed_milliseconds']
            ret = PlayerModel.playerstate.update_elapsed(elapsed_ms)
            # if not ret:
            #     pprint(f'Issue updating elapsed time.\nBad message {m}')
            timed_out_180 = PlayerModel.playerstate.check_180_timeout()
            if timed_out_180:
                PlayerModel.playerstate.handle_180_timeout()
                for pid, p in PlayerModel.playerstate.players.items():
                    if 'update_180' in p:
                        print('for participant_id', pid)
                        pprint(p['update_180'])

        if message_type == 'trial' and sub_type == 'start':
            # pprint(m)
            PlayerModel.playerstate.handle_trial_start(dat['client_info'], exp_id, trial_id)

        if sub_type == 'Status:SurveyResponse':
            vals = PlayerModel.playerstate.handle_survey_values(dat['values'],
                                                                exp_id, trial_id)
            # pprint(vals)
            pp = vals['player_profile']
            if pp:
                PlayerModel.playerstate.handle_player_profile(pp)

        if sub_type == 'Event:MissionState':
            PlayerModel.playerstate.handle_mission_state(dat)

        if sub_type == 'Event:Triage':
            PlayerModel.playerstate.handle_event_triage(dat, exp_id, trial_id)

        if sub_type == 'Event:RubbleDestroyed':
            PlayerModel.playerstate.handle_rubble_destroyed(dat, exp_id, trial_id)

        if sub_type == 'Event:VictimEvacuated':
            PlayerModel.playerstate.handle_victim_evacuated(dat, exp_id, trial_id)

        if sub_type == 'Event:VictimPickedUp':
            PlayerModel.playerstate.handle_victim_picked_up(dat, exp_id, trial_id)

        if sub_type == 'Event:VictimPlaced':
            PlayerModel.playerstate.handle_victim_placed(dat, exp_id, trial_id)

        if message_type == 'observation' and sub_type == 'state':
            PlayerModel.playerstate.handle_obs_state(dat, exp_id, trial_id)
    # PlayerModel.playerstate.print_player_state()


def main(pth):
    if pth.is_dir():
        print('Processing files in dir:', pth)
        files = [x for x in pth.iterdir() if x.is_file() and x.suffix == '.metadata']
        sfiles = sorted(files)
        for f in sfiles:
            process_metadata_file(f)
    else:
        process_metadata_file(pth)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create Player profile for metadata file or dir containing metadata files. ')
    parser.add_argument('fl_dir', help='.metadata file or dir containing them', default='./')
    args = parser.parse_args()
    main(Path(args.fl_dir))
