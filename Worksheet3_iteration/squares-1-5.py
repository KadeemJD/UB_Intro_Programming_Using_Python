# -*- coding: utf-8 -*-

"""
Use a while loop to print the squares of numbers from 1 to 5.
"""

#step 1   
counter_numbers = 1
stop = 5
num_square = 0
    
while counter_numbers <= stop:
    num_square= counter_numbers ** 2
    print(f"{num_square}")
    counter_numbers = counter_numbers + 1