# -*- coding: utf-8 -*-
"""
Write a function called odd_or_even that takes an integer as a parameter and returns
 "Odd" if the number is odd and "Even" if the number is even.

"""

def odd_or_even(integer):
    if integer % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
result = odd_or_even(6)
print(result)