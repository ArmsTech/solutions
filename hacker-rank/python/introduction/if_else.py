# If-Else Challenge
"""
Given an integer, n, perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird
"""
n = int(raw_input())

if n % 2 != 0:
    print "Weird"
else:
    if 2 <= n <= 5:
        print "Not Weird"
    elif 6 <= n <= 20:
        print "Weird"
    elif n > 20:
        print "Not Weird"
