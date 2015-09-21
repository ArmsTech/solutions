# Validating Email Addresses With A Filter Challenge
"""
You are given an integer N followed by N email addresses. Your task is to
print a list containing valid email addresses, in lexicographic order.


A valid email address is of the format username@websitename.extension
Username can only contain letters, digits, dash and underscore. Website name
can have letters and digits. Maximum length of the extension is 3.
"""

import re

EMAIL_RE = re.compile('[-\w]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$')

addresses = []

for _ in range(int(raw_input())):
    addresses.append(raw_input())

print filter(lambda e: EMAIL_RE.match(e) is not None, sorted(addresses))
