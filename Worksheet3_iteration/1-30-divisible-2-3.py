# -*- coding: utf-8 -*-
"""
Use  a while loop to print numbers from 1 to 30 that are divisible by both 2 and 3.
"""

number = 1

while number <= 30:
    if number % 2 == 0 and number % 3 == 0:
        print(number)
    number += 1

    