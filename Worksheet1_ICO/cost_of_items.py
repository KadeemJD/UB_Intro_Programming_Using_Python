# -*- coding: utf-8 -*-

"""
Total Cost of Items
Prompt the user to enter the cost of three items. Calculate the total cost and print it.
"""

#input cost of three items
item1 = input("Please enter cost of item 1: ")
item2 = input("Please enter cost of item 2: ")
item3 = input("Please enter cost of item 3: ")
#convert stings to floats
float_item1 = float(item1)
float_item2 = float(item2)
float_item3 = float(item3)
#calculate the total cost
totalCost = float_item1 + float_item2 + float_item3
#print the result
print(f"The total cost of your items is ${totalCost:.2f}!")