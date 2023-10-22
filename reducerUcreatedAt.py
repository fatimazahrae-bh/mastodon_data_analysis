#!/usr/bin/env python3

import sys

current_year = None
user_count = 0

for line in sys.stdin:
    year, count = line.strip().split('\t')
    
    if current_year == year:
        user_count += int(count)
    else:
        if current_year:
            print(f"{current_year}\t{user_count}")
        current_year = year
        user_count = int(count)

if current_year:
    print(f"{current_year}\t{user_count}")
