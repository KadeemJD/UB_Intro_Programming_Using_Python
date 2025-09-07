# -*- coding: utf-8 -*-

"""
Write a program that determines if a year entered by the user is 
a leap year or not. (Do some research to find out about leap years)
"""

#user input of year

userYear = int(input("Enter a year: "))

#conditionals about leap years

if userYear % 4 == 0:
    print("This is a leap year.")
elif userYear % 400 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")