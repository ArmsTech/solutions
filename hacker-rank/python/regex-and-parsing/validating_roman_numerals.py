# Validating Roman Numerals Challenge
"""
You are given a string and you have to validate whether it's a valid Roman
numeral. If it is valid, print True, otherwise print False. Try to create a
regular expression for a valid Roman numeral.
"""

import re

ROMAN_RE = re.compile(
    '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

print ROMAN_RE.search(raw_input()) is not None
