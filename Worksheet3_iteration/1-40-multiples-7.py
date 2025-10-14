# -*- coding: utf-8 -*-

"""
Use a while loop to print numbers from 1 to 40 except for  multiples of 7.
"""

number = 1
stop = 40

    
while number <= stop:
    if number % 7 != 0:
        print(number)
    number += 1