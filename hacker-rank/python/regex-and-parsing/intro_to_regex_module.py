# -*- coding: utf-8 -*-
# Introduction To Regex Module Challenge
"""
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following
requirements:

> Number can start with +, - or . symbol.
    For example:
    ✔ +4.50
    ✔ -1.0
    ✔ .5
    ✔ -.7
    ✔ +.4
    ✖ -+4.5

> Number must contain at least 1 decimal value.
    For example:
    ✖ 12.
    ✔ 12.0

> Number must have exactly one . symbol.
> Number must not give any exceptions when converted using float(N).
"""

import re

VALID_FLOAT_RE = re.compile('[+-]?\d*\.\d{1,}$')

for _ in range(int(raw_input())):
    print VALID_FLOAT_RE.match(raw_input()) is not None
