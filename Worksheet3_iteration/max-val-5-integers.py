# -*- coding: utf-8 -*-

"""
Use a while loop to find the maximum value in an array of 5 integers.
"""

array = [23,45,12,78,35]
index = 0
max_value = 0
current_value=0

while index < 5:
    current_value = array[index]
    if current_value > max_value:
        max_value = current_value
    index += 1
print(max_value)