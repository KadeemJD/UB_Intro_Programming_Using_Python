# -*- coding: utf-8 -*-

"""
Use  a while loop to print all even numbers from 2 to 20.
"""

#step 1   
counter_numbers = 1
stop = 20
num_evens = 0
    
while counter_numbers <= stop:
    if counter_numbers % 2 == 0:
        num_evens = num_evens + 1
        print(f"{counter_numbers}")
    counter_numbers = counter_numbers + 1
    
print(f"There are {num_evens} even numbers from 2 to 20.")
    
