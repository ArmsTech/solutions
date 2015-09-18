# Maximize It Challenge
"""
You are given a function f(X)=X2.

You are also given K lists. The ith list consists of Ni elements.

You have to pick exactly one element from each list such that
S=(f(X1)+f(X2)+...+f(Xk))%M is  maximized. Xi denotes the element picked
from the ith list . Find the maximized value Smax thus obtained.

% denotes the modulo operator.
"""

import itertools


def maximize(values, m_value):
    """Maximize S = (f(value1) + f(value2) + ...) % m"""
    fx = lambda x: x * x

    s_values = []
    for value in values:
        s_values.append(sum([fx(x) for x in value]) % m_value)

    return max(s_values)


k, m = raw_input().split()
k, m = map(int, (k, m))

elements = []
for _ in range(k):
    elements.append(map(int, raw_input().split()[1:]))

print maximize(itertools.product(*elements), m)
