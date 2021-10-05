#!/usr/bin/env python
"""reducer.py"""

import sys

mean_tot = 0
count_tot = 0
for line in sys.stdin:
    line = line.strip()
    mean, count = line.split(',')
    try:
        mean = float(mean)
        count = int(count)
    except ValueError:
        continue
    if count_tot + count != 0:
        mean_tot = (mean_tot * count_tot + mean * count) / (count_tot + count)
        count_tot = count_tot + count
print(mean_tot)
