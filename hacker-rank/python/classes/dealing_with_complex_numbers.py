# Dealing With Complex Numbers Challenge
"""
For this challenge, you are given two complex numbers and you have to return
the result of their addition, subtraction, multiplication, divison and
modulus operations.
"""


class ComplexNumber(object):

    """Represent a complex number."""

    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f" % self.real
        elif self.real == 0:
            return '%.2fi' % self.imaginary
        else:
            sign = '+' if self.imaginary > 0 else '-'
            return ' '.join(
                ("%.2f" % self.real, sign, '%.2fi' % abs(self.imaginary)))

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        multiplied = complex(
            self.real, self.imaginary) * complex(other.real, other.imaginary)
        return ComplexNumber(multiplied.real, multiplied.imag)

    def __div__(self, other):
        divided = complex(
            self.real, self.imaginary) / complex(other.real, other.imaginary)
        return ComplexNumber(divided.real, divided.imag)

    def __abs__(self):
        modded = abs(complex(self.real, self.imaginary))
        return ComplexNumber(modded.real, modded.imag)

a = ComplexNumber(*map(float, raw_input().split()))
b = ComplexNumber(*map(float, raw_input().split()))

print a + b
print a - b
print a * b
print a / b
print abs(a)
print abs(b)
