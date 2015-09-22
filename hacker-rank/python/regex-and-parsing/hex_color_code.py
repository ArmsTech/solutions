# Hex Color Code Challenge
"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination
of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code
 * It must start with a '#' symbol.
 * It can have 3 or 6 digits.
 * Each digit is in the range of 0 to F. (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
   A, B, C, D, E and F).
 * A-F letters can be in lower case too. (i.e. a, b, c, d, e and f are also
   valid digits).
"""

import re

HEX_RE = re.compile(r'#(?:[\dA-Fa-f]{3}|[\dA-Fa-f]{6})\b')

matches = []
should_collect_hex_codes = False

for _ in range(int(raw_input())):
    line = raw_input()

    if line.endswith(('{', '}')):
        should_collect_hex_codes = '{' in line
        continue

    if should_collect_hex_codes:
        matches.append(HEX_RE.findall(line))

for match in reduce(lambda m1, m2: m1 + m2, matches, []):
    print match
