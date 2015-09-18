# Collections Most Commons Challenge
"""
You are given a string S.
The string consists of lowercase alphabets.

Your task is to find top three most common characters in the string S.
"""

from collections import Counter
from operator import itemgetter

characters = Counter(list(raw_input()))

# qwertyuiopasdfghjklzxcvbnm
# sorted_by_count = sorted(characters.items(), key=itemgetter(1), reverse=True)
# sorted_by_character = sorted(sorted_by_count, key=itemgetter(0))
for item in characters.most_common(3):
    print ' '.join(map(str, item))
