# Find A String Challenge
"""
In this challenge, the user enters a string and a substring and you have to
print the number of times that substring occurs in that string. String
traversal will take place from left to right, not from right to left.

NOTE : Letters of string are case-sensitive.
"""

index = 0
occurs = 0
string = raw_input()
substring = raw_input()

while True:
    try:
        string.index(substring, index)
    except ValueError:
        print occurs
        break
    else:
        occurs += 1
        index = string.index(substring, index) + 1
