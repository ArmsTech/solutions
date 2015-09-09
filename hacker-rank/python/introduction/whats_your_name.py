# What's Your Name Challenge
"""
You are given the first name and the last name of a person. Your task is to
read them and print the following:

Hello firstname lastname! You just delved into python.
"""

first_name = raw_input()
last_name = raw_input()

print "Hello {0} {1}! You just delved into python.".format(
    first_name, last_name)
