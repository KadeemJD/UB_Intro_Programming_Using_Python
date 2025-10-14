# -*- coding: utf-8 -*-
"""
Use a for loop to calculate the sum of odd numbers from 1 to 19.
"""

sum = 0

for i in range(1,20):
    if i % 2 == 1:
        sum += i
print(sum)