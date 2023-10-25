#!/usr/bin/env python3

import sys

current_url = None
share_count = 0

for line in sys.stdin:
    url, count = line.strip().split('\t')
    
    if current_url == url:
        share_count += int(count)
    else:
        if current_url:
            print(f"{current_url}\t{share_count}")
        current_url = url
        share_count = int(count)

if current_url:
    print(f"{current_url}\t{share_count}")
