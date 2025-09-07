# -*- coding: utf-8 -*-

"""
Use a while loop to calculate the sum of even numbers from 2 to 20.
"""

#step 1   
counter_even_numbers = 2
stop = 20
current_even_num = 0
totalSum = 0
    
while counter_even_numbers <= stop:
    if counter_even_numbers % 2 == 0:
        current_even_num = counter_even_numbers
        totalSum = totalSum + current_even_num
        print(f"{totalSum}")
    counter_even_numbers = counter_even_numbers + 1
    


