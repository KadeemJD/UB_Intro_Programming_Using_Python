# -*- coding: utf-8 -*-
"""
Write a function called is_leap_year that takes a year as a parameter and returns True if the year
 is a leap year, and False otherwise. Remember that a leap year is divisible by 4 but not by 100,
 unless it is also divisible by 400.

"""

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False
    
result = is_leap_year(1900)
print(result)