# Map And Lambda Expression Challenge
"""
You have to generate a list of the first N fibonacci numbers, 0 being the
first number. Then, apply the map function and a lambda expression to cube
each fibonacci number and print the list.
"""

fibonacci = []

for number in range(int(raw_input())):
    if len(fibonacci) < 2:
        fibonacci.append(number)
    else:
        fibonacci.append(fibonacci[number - 2] + fibonacci[number - 1])

print map(lambda f: f ** 3, fibonacci)
