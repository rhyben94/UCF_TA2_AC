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
        if msg['sub_type'] == 'Status:SurveyResponse':
            PlayerModel.playerstate.handle_survey_values(m['data']['values'],
                                                         exp_id, trial_id)
        if header['message_type'] == 'trial' and msg['sub_type'] == 'start':
            PlayerModel.playerstate.handle_trial_start(dat['client_info'], exp_id, trial_id)


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
