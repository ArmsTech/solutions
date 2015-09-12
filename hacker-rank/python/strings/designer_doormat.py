# Designer Doormat Challenge
"""
Design specifications are as follows:
1. Size of mat must be NXM. (N is an odd natural number and M is 3 times N.)
2. Design should have 'WELCOME' written in the center.
3. Design pattern should only use '|', '.' and '-' characters.
"""

n, m = map(int, raw_input().split())

# Print Top
for i in xrange(1, n, 2):
    print '-' * ((m - (3 * i)) / 2) + ('.|.' * i) + '-' * ((m - (3 * i)) / 2)

# Print Welcome
print '-' * ((m - 7) / 2) + 'WELCOME' + '-' * ((m - 7) / 2)

# Print Bottom
for i in xrange(n - 2, -1, -2):
    print '-' * ((m - (3 * i)) / 2) + ('.|.' * i) + '-' * ((m - (3 * i)) / 2)
