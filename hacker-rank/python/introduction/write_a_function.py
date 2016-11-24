# Write a Function Challenge
"""
You are given the year, and you have to write a function to check if the year
is leap or not.

Note that you have to complete the function and remaining code is given as
template.
"""


def is_leap_year(year):
    """Check if a given year is a leap year."""
    is_leap_year = False

    if year % 4 == 0:
        is_leap_year = True

        if year % 100 == 0 and year % 400 != 0:
            is_leap_year = False

    return is_leap_year


year = int(raw_input())
print is_leap_year(year)
