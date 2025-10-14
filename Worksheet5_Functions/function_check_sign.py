# -*- coding: utf-8 -*-
"""
Write a function called check_sign that takes an integer as a parameter and returns
 "Positive" if the number is positive, "Negative" if the number is negative, and "Zero" if
 the number is zero.

"""

def check_sign(integer):
    if integer > 0:
        return "Positve"
    elif integer < 0:
        return "Negative"
    else:
        return "Zero"
    
result = check_sign(0)
print(result)
    