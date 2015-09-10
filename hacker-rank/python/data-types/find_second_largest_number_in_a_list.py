# Find Second Largest Number In A List Challenge
"""
You are given 'n' numbers. Store them in a list and find the second largest
number. NOTE : Don't use insertion sort
"""

raw_input()
list_ = set(map(int, raw_input().split()))

print sorted(list_)[-2]
