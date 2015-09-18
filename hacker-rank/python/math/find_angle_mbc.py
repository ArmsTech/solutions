# -*- coding: utf-8 -*-
# Find Angle MBC Challenge
"""
You are given the lengths AB and BC.
Your task is to find ∡MBC ( angle θ°, as shown in figure ) in degrees.
"""

import math

b = int(raw_input())
a = c = math.hypot(b, int(raw_input())) / 2  # Isosceles triangle

cos = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)
print '%d%s' % (round(math.degrees(math.acos(cos))), '°')
