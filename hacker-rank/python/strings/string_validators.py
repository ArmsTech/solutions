# String Validators Challenge
"""
You are given a string S.
Your task is to find if string S contains, alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.
"""

string = list(raw_input())

for string_method in (str.isalnum, str.isalpha, str.isdigit,
                      str.islower, str.isupper):
    print any(map(string_method, string))
