# Time Delta Challenge
"""
Given 2 timestamps, print the absolute difference (in seconds) between them.
"""

from datetime import datetime

for _ in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')

    absolute_difference = abs(int((t1 - t2).total_seconds()))
    print(absolute_difference)
