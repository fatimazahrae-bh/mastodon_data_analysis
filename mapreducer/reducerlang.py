#!/usr/bin/env python3

import sys

current_language = None
toot_count = 0

for line in sys.stdin:
    language, count = line.strip().split('\t')
    
    if current_language == language:
        toot_count += int(count)
    else:
        if current_language:
            print(f"{current_language}\t{toot_count}")
        current_language = language
        toot_count = int(count)

if current_language:
    print(f"{current_language}\t{toot_count}")
