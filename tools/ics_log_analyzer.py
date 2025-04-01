#!/usr/bin/env python3
with open("ics_log.txt") as f:
    for line in f:
        if "STOP_PROCESS" in line or "WRITE_REGISTER" in line:
            print("[!] Suspicious command:", line.strip())
