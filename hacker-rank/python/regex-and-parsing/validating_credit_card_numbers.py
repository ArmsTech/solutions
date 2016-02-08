# Validating Credit Card Numbers Challenge
"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit
cards from ABCD Bank. He wants to verify whether his credit card numbers are
valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

* It must start with a 4, 5 or 6.
* It must contain exactly 16 digits.
* It must only consist of digits (0-9).
* It may have digits in groups of 4, separated by one hyphen "-".
* It must NOT use any other separator like '  ' , '_', etc.
* It must NOT have 4 or more consecutive repeated digits.
"""

import re

CREDIT_CARD_RE = '^[456]\d{3}-?(?:\d{4}-?){2}\d{4}$'
CONSECUTIVE_CHARACTERS_RE = r'(.)\1{3,}'

for _ in range(int(raw_input())):
    card_number = raw_input()

    if re.match(CREDIT_CARD_RE, card_number) and not re.search(
       CONSECUTIVE_CHARACTERS_RE, card_number.replace('-', '')):
        print 'Valid'
    else:
        print 'Invalid'
