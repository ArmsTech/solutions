# Capitalize Challenge
"""
You are given a string S. Your task is to capitalize each word of S.
"""

string = raw_input()
print ' '.join([substring.capitalize() for substring in string.split(' ')])
