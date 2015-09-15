# Symmetric Difference Challenge
"""
You are given two sets of roll numbers of students, who have subscribed to
English and French newspapers. Your task is to find total number of students
who have subscribed to English or French newspapers but not both.
"""

raw_input()
english = set(map(int, raw_input().split()))
raw_input()
french = set(map(int, raw_input().split()))

print len(english.symmetric_difference(french))
