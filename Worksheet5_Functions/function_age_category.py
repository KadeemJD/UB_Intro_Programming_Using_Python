# -*- coding: utf-8 -*-
"""
Write a function called age_category that takes an integer age as a parameter and returns
 "Child" if the age is less than 13, "Teenager" if the age is between 13 and 19, "Adult" if the age is 20 or above.

"""

def age_category(integer):
    if integer < 13:
        return "Child"
    elif integer >== 13 and <==19:
        return "Teenager"
    else:
        return "Adult"
    
result = age_category(17)
print(result)