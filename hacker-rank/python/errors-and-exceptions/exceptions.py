# Exceptions Challenge
"""
You are given two values a and b.
Your task is to do integer division and print a/b.
"""

for _ in range(int(raw_input())):
    try:
        a, b = map(int, raw_input().split())
        print a / b
    except (ValueError, ZeroDivisionError) as error:
        print "Error Code: %s" % str(error)
