# Validating And Parsing Email Addresses Challenge
"""
You are given N names and email addresses. Your task is to print the names and
email addresses if they are valid.

A valid email address follows the rules below:
- Email must have three basic components: username @ website name . extension.
- The username can contain: alphanumeric characters, -,. and _.
- The username must start with an English alphabet character.
- The website name contains only English alphabet characters.
- The extension contains only English alphabet characters, and its length can
  be 1, 2, or 3.
"""

import re

EMAIL_RE = re.compile('<[a-zA-Z][-.\w]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>')

for _ in range(int(raw_input())):
    name, email = raw_input().split()
    if EMAIL_RE.match(email):
        print ' '.join([name, email])
