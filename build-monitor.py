#!/usr/bin/env python

import time
from datetime import datetime
from os import path, walk

target_dirs = ["test-dir"]

current_time = time.time()
latest_modified = current_time

def monitor():
    while True:
        _trigger_build_if_a_file_has_been_modified()
        time.sleep(1)

def _trigger_build_if_a_file_has_been_modified():
    global target_dirs, latest_modified
    start_time = time.time()
    for dir in target_dirs:
        for file_root, file_dir, files in walk(dir):
            for filename in files:
                file = path.join(file_root, filename)
                if path.exists(file):
                    last_modified = _get_last_modified(file)
                    if last_modified > latest_modified:
                        latest_modified = last_modified
                        print("The file {0} is modified. Triggered build at {1}".format(file, datetime.now()))
    end_time = time.time()
    print("Start: {0}, End: {1}, Difference: {2}".format(start_time, end_time, (end_time - start_time)))

def _get_last_modified(file):
    return path.getmtime(file)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("Exiting build monitor")
