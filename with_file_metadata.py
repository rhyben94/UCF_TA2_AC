#!/usr/bin/env python3

# Copyright 2022 Dynamic Object Language Labs Inc.
# DISTRIBUTION STATEMENT C: U.S. Government agencies and their contractors.
# Other requests shall be referred to DARPA’s Public Release Center via email at prc@darpa.mil.

# Run this command as below: The argument must be a .metadata file or directory containing metadata files.
# ./with_file_metadata.py FILE_OR_DIR

import argparse
from pathlib import Path
import metadata_utils


def process_metadata_file(fname):
    print('Working on file', fname)
    msgs = metadata_utils.read_file(fname)
    print(f'Got msgs {len(msgs)}')


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
