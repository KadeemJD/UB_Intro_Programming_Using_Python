# -*- coding: utf-8 -*-
"""
Use a for loop to find the maximum value in an array of 5 integers.

"""

numbers = [ 13, 53, 26, 212, 38]
max_value = numbers[0]



for num in numbers:
    if num > max_value:
        max_value = num
print(max_value)