#!/usr/bin/env python3

import time
import re

log_file_path = "/var/log/openvpnas.log"

def monitor_openvpn_connections():
    with open(log_file_path, "r") as log_file:
        log_file.seek(0, 2)

        while True:
            line = log_file.readline()
            if not line:
                time.sleep(0.1)
                continue

            if re.search(r"initialized with 256 bit key", line, re.IGNORECASE):
                print(f"Connection Initialized: {line.strip()}")
            elif re.search(r"client-instance exiting", line, re.IGNORECASE):
                print(f"Client Disconnected: {line.strip()}")

monitor_openvpn_connections()
