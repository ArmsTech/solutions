# -*- coding: utf-8 -*-
# Regex Substitution Challenge
"""
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify :

    && →  and
    || →  or

Both && and || should have space " " on both sides.
"""

import re

AND_OR_RE = re.compile('(?<= )(&{2}|\|{2})(?= )')

for _ in range(int(raw_input())):
    print re.sub(
        AND_OR_RE,
        lambda m: 'and' if m.group(1) == '&&' else 'or',
        raw_input())
