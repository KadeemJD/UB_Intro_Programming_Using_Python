# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the sum of odd numbers from 1 to 19.
"""

#step 1   
counter_odd_numbers = 1
stop = 19
current_odd_num = 0
totalSum = 0
    
while counter_odd_numbers <= stop:
    if counter_odd_numbers % 2 == 1:
        current_odd_num = counter_odd_numbers
        totalSum = totalSum + current_odd_num
        print(f"{totalSum}")
    counter_odd_numbers = counter_odd_numbers + 1