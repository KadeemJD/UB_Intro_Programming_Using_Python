# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the sum of the cubes of the numbers from 1 to 3.
"""

number = 1
sum = 0
cube = 0
while number <= 3:
    cube = number ** 3
    sum += cube
    number += 1
print(sum)