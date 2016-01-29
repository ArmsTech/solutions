# Group, Groups, and Groupdict Challenge
"""
You are given a string S. Your task is to find the first occurrence of an
alphanumeric character in S (read from left to right) that has consecutive
repetitions.
"""

import re

REPETITIONS_RE = re.compile(r'([0-9a-zA-Z])\1+')

match = REPETITIONS_RE.search(raw_input())
print match.group(1) if match else -1
