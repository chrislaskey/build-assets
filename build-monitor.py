#!/usr/bin/env python

import time
import os.path

target_dirs = ["test-dir"]

current_time = time.time()
latest_modified = current_time

def monitor():
    while True:
        _trigger_build_if_a_file_has_been_modified()
        time.sleep(1)

def _trigger_build_if_a_file_has_been_modified():
    global latest_modified
    path = "test-dir/test-file"
    if os.path.exists(path):
        last_modified = _get_last_modified(path)
        if last_modified > latest_modified:
            latest_modified = last_modified
            print("building")

def _get_last_modified(file):
    return os.path.getmtime(file)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("Exiting build monitor")
