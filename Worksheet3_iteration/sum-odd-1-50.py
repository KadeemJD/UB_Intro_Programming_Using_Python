# -*- coding: utf-8 -*-
"""
Use  a while loop to calculate the sum of all odd numbers from 1 to 50.
"""

number = 1
sum = 0

while number <= 50:
    if number % 2 == 1:
        sum = sum + number
    number += 1
print(sum)