# Name Directory Challenge
"""
You are given some information about N people. Each person has a first name,
last name, age and sex. You have to print their names in a specific format
sorted by their age in ascending order i.e. the youngest person's name should
be printed first. For two people having the same age, the printing should be
done in the order of their input.
"""

import functools
from operator import itemgetter


def with_honorifics(func):
    @functools.wraps(func)
    def wrapper(people):
        def add_honorific(person):
            first_name, last_name, gender = person
            honorific = 'Mr.' if gender == 'M' else 'Ms.'
            return ' '.join([honorific, first_name, last_name])
        return map(
            add_honorific,
            [itemgetter(0, 1, 3)(person) for person in func(people)])
    return wrapper


@with_honorifics
def get_names(people):
    return sorted(people, key=itemgetter(2))


people = [raw_input().split() for _ in range(int(raw_input()))]
print '\r\n'.join(get_names(people))
