# Sort Data Challenge
"""
You are given data in a tabular format i.e. the data contains N rows and each
row contains M space-separated elements.

You can imagine the M items to be different attributes (like height, weight,
energy, etc) and each of the N rows as an instance or a sample.

Your task is to sort the table on the Kth attribute and print the final
resulting table.

[If two attributes are the same for different rows, print the row that
appeared first in the input]
"""

from operator import itemgetter

lines, _ = raw_input().split()
samples = []

for _ in range(int(lines)):
    samples.append(map(int, raw_input().split()))

k = int(raw_input())
for sample in sorted(samples, key=itemgetter(k)):
    print ' '.join(map(str, sample))
