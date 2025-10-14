# -*- coding: utf-8 -*-
"""
Use a for loop to calculate the sum of even numbers from 2 to 20.
"""

sum =0

for i in range(2,21):
    if i % 2 == 0:
        sum += i
print(sum)