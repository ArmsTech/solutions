# Collections Counter Challenge
"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing size of each shoe he has in his shop.
There are N number of customers, who are willing to pay xi amount of money
only if they get the shoe of their desired size.

Your task is to compute, how much money Raghu earned.
"""

from collections import Counter

raw_input()
inventory = Counter(raw_input().split())
total_sales = 0

for _ in range(int(raw_input())):
    size, price = raw_input().split()

    if inventory.get(size, 0) > 0:
        total_sales += int(price)
        inventory[size] -= 1

print total_sales
