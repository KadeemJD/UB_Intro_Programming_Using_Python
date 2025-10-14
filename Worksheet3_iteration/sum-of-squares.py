# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the sum of squares of even numbers from 1 to 20.
"""

number = 1
sum=0
number2 = 0

while number <= 20:
    if number % 2 == 0:
        number2 = number ** 2
        sum += number2
    number += 1
print (f"The sum is {sum}.")