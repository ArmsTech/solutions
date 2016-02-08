# Validating UID Challenge
"""
ABCXYZ company has up to 100 employees. The company decides to create a unique
identification number (UID) for each of its employees. The company has
assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

* It must contain at least 2 uppercase English alphabet characters.
* It must contain at least 3 digits (0 - 9).
* It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
* No character should repeat.
* There must be exactly 10 characters in a valid UID.
"""

import re

ONLY_ALPHANUMERIC_CHARACTERS_RE = r'[a-zA-Z0-9]{10}'
TWO_UPPERCASE_RE = r'.*(?:[A-Z].*){2,}'
THREE_DIGITS_RE = r'.*(?:[\d].*){3,}'
REPEATING_CHARACTERS_RE = r'.*(.).*\1'

for _ in range(int(raw_input())):
    uid = raw_input()

    matches = all([re.match(regex, uid) for regex in (
        ONLY_ALPHANUMERIC_CHARACTERS_RE, TWO_UPPERCASE_RE, THREE_DIGITS_RE)])

    if matches and not re.match(REPEATING_CHARACTERS_RE, uid):
        print 'Valid'
    else:
        print 'Invalid'
