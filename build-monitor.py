#!/usr/bin/env python

import time
from datetime import datetime
from os import path, walk

class Monitor:

    def __init__(self):
        current_time = time.time()
        self.latest_modified = current_time
        self.target_dirs = ["test-dir"]

    def run(self, sleep_seconds = 1):
        while True:
            self.trigger_build_if_modified()
            time.sleep(sleep_seconds)

    def trigger_build_if_modified(self):
        for dir in self.target_dirs:
            for file_root, file_dir, files in walk(dir):
                for filename in files:
                    file = path.join(file_root, filename)
                    last_modified = self.get_last_modified(file)
                    if last_modified > self.latest_modified:
                        self.latest_modified = last_modified
                        return self.print_modified_message(file)

    def print_modified_message(self, file):
        print("The file {0} is modified. Triggered build at {1}"
                .format(file, datetime.now()))

    def get_last_modified(self, file):
        return path.getmtime(file)

if __name__ == "__main__":
    try:
        file_monitor = Monitor()
        file_monitor.run()
    except KeyboardInterrupt:
        print("Exiting build monitor")
