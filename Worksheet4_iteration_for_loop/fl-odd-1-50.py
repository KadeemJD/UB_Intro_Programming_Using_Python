# -*- coding: utf-8 -*-

"""
Use a for loop to calculate the sum of all odd numbers from 1 to 50.
"""

sum = 0

for i in range(1,51):
    if i % 2 == 1:
        sum += i
print(sum)

