#!/usr/bin/env python
"""mapper_mean.py"""

import sys


def custom_parser(line, id=9):
    counter = 0
    nstr = True
    res = ''
    for char in line:
        if nstr and char not in ["'", '"']:
            if char == ',':
                counter = counter + 1
                if counter > id:
                    try:git 
                        return float(res)
                    except ValueError:
                        return 0
            elif counter == id:
                res = res + char
        else:
            nstr = not nstr

# input comes from STDIN (standard input)

mean = 0
count = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    # line = line.strip()
    # split the line into words
    # words = line.split(',')
    # words = list(csv.reader(line))
    words = custom_parser(line)
    # increase counters
    # pdb.set_trace()
    if words is not None:
        mean = mean + words
    count = count + 1
print('%s, %s' % (mean/count, count))
