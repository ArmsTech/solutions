# Mutations Challenge
"""
You have to read a string. change the character at a given index and print
the string.
"""

word = list(raw_input())
index, char = raw_input().split()

word[int(index)] = char
print ''.join(word)
