# Incorrect Regex Challenge
"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.
"""

import re

for _ in range(int(raw_input())):
    regex = raw_input()

    try:
        re.compile(regex)
    except re.error:
        print False
    else:
        print True
