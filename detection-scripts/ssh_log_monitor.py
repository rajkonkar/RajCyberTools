#!/usr/bin/env python3
import re

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 5
failed_ips = {}

with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as log:
    for line in log:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                failed_ips[ip] = failed_ips.get(ip, 0) + 1

print("\nSuspicious IPs (Brute-force suspects):\n")
for ip, count in failed_ips.items():
    if count >= THRESHOLD:
        print(f"{ip} - {count} failed attempts")
