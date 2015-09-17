# -*- coding: utf-8 -*-
# The Captain's Room Challenge
"""
Mr. Anant Asankhya is the manager at INFINITE hotel. The hotel has an
infinite amount of rooms.

One fine day, a finite number of tourists came to stay at the hotel.
Tourists consisted of :

→ a Captain.
→ Equal sized group of families (size K each and K ≠ 1).

The Captain was given a separate room and rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list
consists of room numbers of all the tourists. The room numbers will appear K
times per group except for the Captain's room.

Mr. Anant needs help from you to find the Captain's room number.
Total number of Tourists or total group of families is not known to you.
You only have the value of K and room number list.
"""

from collections import Counter

raw_input()
rooms = map(int, raw_input().split())

print Counter(rooms).most_common()[-1][0]
