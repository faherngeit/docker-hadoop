#!/usr/bin/env python3
"""mapper_var.py"""

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
                    try:
                        return float(res)
                    except ValueError:
                        return None
            elif counter == id:
                res = res + char
        else:
            nstr = not nstr


mean = 0
count = 0
var = 0
for line in sys.stdin:
    price = custom_parser(line)
    if price is not None:
        var = (count * var) / (count + 1) + count * ((mean - price) / (count + 1)) ** 2
        mean = (count * mean + price) / (count + 1)
        count = count + 1
print('%s, %s, %s' % (mean, var, count))
