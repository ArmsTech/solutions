# OrderedDict Challenge
"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on
a particular day. Your task is to print each item_name and net_price in order
of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
"""

from collections import OrderedDict

manager_list = OrderedDict()

for _ in range(int(raw_input())):
    items = raw_input().split()

    item_price = int(items.pop())
    item_name = ' '.join(items)

    manager_list[item_name] = manager_list.get(item_name, 0) + item_price

for item_name, net_price in manager_list.iteritems():
    print ' '.join([item_name, str(net_price)])
