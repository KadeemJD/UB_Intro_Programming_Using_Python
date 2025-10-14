# -*- coding: utf-8 -*-

"""
Use  a while loop to print numbers from 1 to 20 except for  those that are
 multiples of 2.
"""

number = 1

while number <= 20:
    if number % 2 != 0:
        print(number)
    number += 1