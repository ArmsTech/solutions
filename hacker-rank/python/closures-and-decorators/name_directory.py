# Name Directory Challenge
"""
You are given some information about N people. Each person has a first name,
last name, age and sex. You have to print their names in a specific format
sorted by their age in ascending order i.e. the youngest person's name should
be printed first. For two people having the same age, the printing should be
done in the order of their input.
"""

import functools


def with_honorifics(func):
    @functools.wraps(func)
    def wrapper(names_and_genders):
        def add_honorific(name, gender):
            honorific = 'Mr.' if gender == 'M' else 'Ms.'
            return ' '.join(honorific, name)
        return map(add_honorific, names_and_genders)
    return wrapper


def get_names(people):
    return [person[:2] for person in people]

data = """Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F"""

people = []
for person in data.split('\n'):
    people.append(person.split())

print people
