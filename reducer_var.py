#!/usr/bin/env python3
"""reducer_var.py"""

import sys

mean_tot = 0
var_tot = 0
count_tot = 0
for line in sys.stdin:
    line = line.strip()
    mean, var, count = line.split(',')
    try:
        mean = float(mean)
        var = float(var)
        count = int(count)
    except ValueError:
        continue
    if count_tot + count != 0:
        mean_tot = (mean_tot * count_tot + mean * count) / (count_tot + count)
        var_tot = (count_tot * var_tot + count * var) / (count_tot + count) + \
                  count * count_tot * ((mean_tot - mean) / (count_tot + count)) ** 2
        count_tot = count_tot + count
print(var_tot)
