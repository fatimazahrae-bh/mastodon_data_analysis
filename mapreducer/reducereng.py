#!/usr/bin/env python3

import sys

current_user = None
current_engagement = 0

for line in sys.stdin:
    username, reblogs_count = line.strip().split('\t')
    
    if current_user == username:
        current_engagement += int(reblogs_count)
    else:
        if current_user:
            print(f"{current_user}\t{current_engagement}")
        current_user = username
        current_engagement = int(reblogs_count)

if current_user:
    print(f"{current_user}\t{current_engagement}")
