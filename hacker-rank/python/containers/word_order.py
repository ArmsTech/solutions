# Word Order Challenge
"""
You are given n words. Some words may repeat. For each word, you have to
output its number of occurences. But the output order should correspond with
the order of the first appearance of the word. See the sample input/output
for clarification. Note that each line in the input ends with a "\n"
character.
"""

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


word_counts = OrderedCounter(
    [raw_input() for _ in range(int(raw_input()))])

print len(word_counts)
print ' '.join([str(count) for _, count in word_counts.iteritems()])
