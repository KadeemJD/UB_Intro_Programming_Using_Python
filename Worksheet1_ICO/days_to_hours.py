# -*- coding: utf-8 -*-

"""
Convert Days to Hours
Request the user to input a number of days. Convert this to hours and print the result.
"""

#User input of days
days = input("Please enter a number of days: ")
int_days = int(days)
#Conversion
hours = int_days * 24
#print results
print(f"{days} days is {hours} hours.")