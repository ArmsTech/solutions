# ginortS Challenge
"""
You are given a string S. S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

    * All sorted lowercase letters are ahead of uppercase letters.
    * All sorted uppercase letters are ahead of digits.
    * All sorted odd digits are ahead of sorted even digits.
"""

from __future__ import print_function


def ginortS(char):
    """Sort a string according to HR rules."""
    if char.islower():
        sort_class = 1
    elif char.isupper():
        sort_class = 2
    else:
        try:
            digit = int(char)
        except ValueError:
            sort_class = 5
        else:
            sort_class = 4 if digit % 2 == 0 else 3

    return sort_class, ord(char)


print(*sorted(raw_input(), key=ginortS), sep='')
