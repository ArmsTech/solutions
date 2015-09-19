# Collections Most Commons Challenge
"""
You are given a string S.
The string consists of lowercase alphabets.

Your task is to find top three most common characters in the string S.
"""

from collections import Counter


def custom_sort(x, y):
    """Sort by descending {x,y}[1] with secondary ascending {x,y}[0]"""
    if x[1] == y[1]:
        return 1 if x[0] > y[0] else -1
    return cmp(y[1], x[1])


characters = Counter(list(raw_input()))

for item in sorted(characters.most_common(3), cmp=custom_sort):
    print ' '.join(map(str, item))
