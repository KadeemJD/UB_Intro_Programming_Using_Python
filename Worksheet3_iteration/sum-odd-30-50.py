# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the sum of all odd numbers greater than 30 and up to 50.
"""

number = 30
sum = 0

while number <= 50:
    if number % 2 == 1:
        sum += number
    number += 1
print(sum)