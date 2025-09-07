# -*- coding: utf-8 -*-

"""
Use a while loop to print multiples of 3 from 3 to 30.
"""

#step 1   
counter_numbers = 3
stop = 30
num_evens = 0
    
while counter_numbers <= stop:
    if counter_numbers % 3 == 0:
        print(f"{counter_numbers}")
    counter_numbers = counter_numbers + 1
    

