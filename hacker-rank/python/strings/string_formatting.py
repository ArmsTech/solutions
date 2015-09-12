# String Formatting Challenge
"""
Read N and print the decimal, octal, hexadecimal, and binary values from 1
to N with space padding so that all fields take the same width as the binary
value.
"""

n = int(raw_input())
padding = len("{0:b}".format(n))

for number in range(1, n + 1):
    decimal, octal, hexadecimal, binary = '{0:d}', '{0:o}', '{0:X}', '{0:b}'
    print ' '.join([
        decimal.format(number).rjust(padding),
        octal.format(number).rjust(padding),
        hexadecimal.format(number).rjust(padding),
        binary.format(number).rjust(padding)])
