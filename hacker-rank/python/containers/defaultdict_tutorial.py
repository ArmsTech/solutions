# Default Dict Tutorial Challenge
"""
In this challenge, you will be given 2 integers (n and m) and n words which
might repeat, say they belong to a word group A. Then you'll be given m other
words belonging to word group B. For each of these m words, you have to check
whether the word has appeared in A or not. If it has then you have to print
indices of all of its occurences. If it has not then just print -1.
"""

from collections import defaultdict

words = defaultdict(list)
n, m = map(int, raw_input().split())

for number in range(1, n + 1):
    words[raw_input()].append(str(number))

occurences = []
for _ in range(m):
    occurences.append(raw_input())

for occurence in occurences:
    print ' '.join(words[occurence] or ['-1'])
