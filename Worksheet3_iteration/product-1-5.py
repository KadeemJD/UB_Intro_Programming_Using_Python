# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the product of numbers from 1 to 5.
"""

counter = 0
total = 4
fProduct = 1
# set up the while loop
while counter <= total:
    counter = counter + 1
    current_number= counter
    fProduct = fProduct * current_number
print(f"{fProduct}")