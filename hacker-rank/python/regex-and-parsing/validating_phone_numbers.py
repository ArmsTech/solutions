# Validating Phone Numbers Challenge
"""
Let's dive into the interesting topic of regular expressions! You are given
some inputs and you are required to check whether they are valid mobile
numbers.

A valid mobile number is a ten digit number starting with 7, 8 or 9.
"""

import re

PHONE_RE = re.compile('[7-9]\d{9}$')

for _ in range(int(raw_input())):
    print 'YES' if PHONE_RE.match(raw_input()) else 'NO'
