#!/usr/bin/env python3

# Copyright 2022 Dynamic Object Language Labs Inc.
# DISTRIBUTION STATEMENT C: U.S. Government agencies and their contractors.
# Other requests shall be referred to DARPA’s Public Release Center via email at prc@darpa.mil.

import argparse
import json
import copy
import os
from dateutil.parser import parse
from pprint import pprint
from pprint import pformat


def read_file(fname, sort=True):
    with open(fname, "r", encoding="utf-8") as f:
        messages = []
        for line in f:
            jline = None
            try:
                jline = json.loads(line)
            except:
                print(f"Bad json line of len: {len(line)}, {line}")
            if jline is not None:
                messages.append(jline)

        if not sort:
            return messages

        print("Sorting messages...")
        sorted_messages = sorted(
            messages, key=lambda x: parse(x["header"]["timestamp"])
        )
        return sorted_messages


def write_file(fname, messages):
    if fname is None:
        print('Write file is None')
        return
    if len(messages) == 0:
        print('messages len is 0')
        return
    print('Writing messages', len(messages), 'to', fname)
    with open(fname, 'w') as f:
        for m in messages:
            f.write(json.dumps(m) + os.linesep)


def write_json(jsn, fname):
    with open(fname, 'w') as fp:
        json.dump(jsn, fp, sort_keys=True, indent=True)


def write_to_file(obj, fname):
    copied = copy.deepcopy(obj) #obj.copy()
    for pid, val in copied.items():
        if 'dynamic_profile' in val:
            del val['dynamic_profile']
    str = pformat(copied)
    text_file = open(fname, "w")
    text_file.write(str)
    text_file.close()


def dateutil_time_to_millis_since_epoch(x):
    return int(x.timestamp() * 1000)


def get_mission_timer_start_stop_times(messages):
    if len(messages) > 0:
        start = dateutil_time_to_millis_since_epoch(parse(messages[0]['header']['timestamp']))
        stop = dateutil_time_to_millis_since_epoch(parse(messages[-1]['header']['timestamp']))
        return {'start-time': start,
                'stop-time': stop}
    return None


def get_mission_timer_msgs(messages):
    "filter messages between 'mission_timer':'10 : 0' and 0:0"

    collect = False
    ret = []

    for msg in messages:
        if 'data' in msg and 'mission_timer' in msg['data']:
            if msg['data']['mission_timer'] == "10 : 0":
                collect = True

            if msg['data']['mission_timer'] == "0 : 0":
                ret.append(msg)
                collect = False

            if collect:
                ret.append(msg)
    return ret


def explore_mission_timer(messages):
    timer_messages = get_mission_timer_msgs(messages)
    print(f'Read {len(messages)}')
    print(f'timer messages {len(timer_messages)}')
    if len(timer_messages) > 0:
        start = timer_messages[0]['header']['timestamp']
        stop = timer_messages[-1]['header']['timestamp']
        print('start stop', start, stop, parse(stop).timestamp() - parse(start).timestamp())
    else:
        print('No Timer messages')

    print('Mission timer ', get_mission_timer_start_stop_times(timer_messages))


def fix_trial_id(messages, trial_id, outf):
    # When we collect data in rita lab with faceSensor, we don't specify trial_id
    # Update messages that does not has trial_id
    print('Updating messages with trial-id', trial_id)
    found_trial_ids = {}
    fixed = []
    for m in messages:
        if 'msg' in m and 'trial_id' in m['msg']:
            tid = m['msg']['trial_id']
            # if debug and tid is None:
            #     print('trial_id is None for', m)
            if tid != trial_id:
                m['msg']['trial_id'] = trial_id
                if tid not in found_trial_ids:
                    found_trial_ids[tid] = True
                    print('Will replace trial_id:', tid)
            fixed.append(m)
        else:
            print('Bad message no trial_id')
            pprint(m)
    write_file(outf, fixed)


def get_trial_id(f):
    name = f.name.split('_')
    for x in name:
        if x.startswith('Trial-'):
            return x
    return None


def get_experiment_info(metadata_f):
    with open(metadata_f) as mf:
        line = mf.readline()
        jsn = json.loads(line)
        # pprint(jsn)
        return {'experiment_id': jsn['msg']['experiment_id'],
                'trial_id': jsn['msg']['trial_id']}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('metadata_file')
    parser.add_argument('--trial_id')
    parser.add_argument('--out_meta_file')
    args = parser.parse_args()
    messages = read_file(args.metadata_file)
    # explore_mission_timer(messages)
    fix_trial_id(messages, args.trial_id, args.out_meta_file)
