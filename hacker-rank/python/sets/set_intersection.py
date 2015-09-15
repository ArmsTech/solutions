# Set Intersection Challenge
"""
You are given two sets of roll numbers of students, who have subscribed to
English and French newspapers. Your task is to find total number of students
who have subscribed to both newspapers.
"""

raw_input()
english = set(map(int, raw_input().split()))
raw_input()
french = set(map(int, raw_input().split()))

print len(english.intersection(french))
