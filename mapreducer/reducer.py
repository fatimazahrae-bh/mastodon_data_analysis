#!/usr/bin/env python3

import sys

current_user = None
current_followers = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 2:
        username, followers_count = parts
        if current_user == username:
            current_followers += int(followers_count)
        else:
            if current_user:
                print(f"{current_user}\t{current_followers}")
            current_user = username
            current_followers = int(followers_count)

if current_user:
    print(f"{current_user}\t{current_followers}")

