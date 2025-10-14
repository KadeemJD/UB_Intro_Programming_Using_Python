# -*- coding: utf-8 -*-

"""
Use a while loop to count how many numbers from 1 to 30 are greater than 20.
"""

number = 1
stop = 30
count = 0

    
while number <= stop:
    if number > 20:
        count += 1
    number += 1
print (f" there are {count} numbers greater than 20.")