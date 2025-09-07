# -*- coding: utf-8 -*-

"""
Use a while loop to print all odd numbers from 1 to 19.
"""


#step 1   
counter_numbers = 1
stop = 19
num_odds = 0
    
while counter_numbers <= stop:
    if counter_numbers % 2 == 1:
        num_odds = num_odds + 1
        print(f"{counter_numbers}")
    counter_numbers = counter_numbers + 1
    
print(f"There are {num_odds} even numbers from 1 to 19.")