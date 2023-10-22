#!/usr/bin/env python3

import sys

current_has_media = None
toot_count = 0

for line in sys.stdin:
    post_id, has_media, count = line.strip().split('\t')
    
    if current_has_media == has_media:
        toot_count += int(count)
    else:
        if current_has_media is not None:
            print(f"Posts with Media: {current_has_media}\t{toot_count}")
        current_has_media = has_media
        toot_count = int(count)

if current_has_media is not None:
    print(f"Posts with Media: {current_has_media}\t{toot_count}")

