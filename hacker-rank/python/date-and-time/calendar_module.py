# Calendar Module Challenge
"""
You are given the date of the day. Your task is to find what day it is on
that date.
"""

import calendar

WEEKDAYS = (
    'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY',
    'FRIDAY', 'SATURDAY', 'SUNDAY')

month, day, year = map(int, raw_input().split())

weekday = calendar.weekday(year, month, day)
print WEEKDAYS[weekday]
