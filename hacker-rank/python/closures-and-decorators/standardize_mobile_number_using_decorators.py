# Standardize Mobile Number Using Decorators Challenge
"""
You are given N mobile numbers. Sort them in ascending order after which
print them in standard format.


+91 xxxxx xxxxx


The given mobile numbers may have +91 or 91 or 0 written before the actual
10 digit number. Alternatively, there maynot be any prefix at all.
"""

import functools


def with_standardized(func):
    """Standardize mobile numbers."""
    @functools.wraps(func)
    def wrapper(numbers):
        prefix = '+91'
        return map(
            lambda n: ' '.join([prefix, n[-10:-5], n[-5:]]), func(numbers))
    return wrapper


@with_standardized
def sort_mobile_numbers(numbers):
    """Sort mobile numbers."""
    return sorted(numbers, key=lambda n: n[-10:])


print '\r\n'.join(
    sort_mobile_numbers([raw_input() for _ in range(int(raw_input()))]))
