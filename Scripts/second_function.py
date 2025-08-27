# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 22:39:53 2025

@author: Kadee
"""
"""
Write a program that asks the user to enter
two numbers. One number represents feet and the
next number represents inches.
Your program is then print out the feet and
inches in terms of centimeters
Note that I inch 2.54 cm
Example:
Enter feet: 4
Enter inches: 9
4 ft and 9 inch(es) is 144.78 cm. I
Ask the user to enter the feet value
Ask the user to enter the inches value
Convert the feet to inches
Convert the inches to cm
Output the result to the console in a nicety
formatted string
"""

feet = float(input('Please enter feet: '))
inches = float(input ('Please enter inches: '))
feet_2 = feet * 12
cm = (feet_2 + inches)*2.54
print( '{} feet and {} inches is equal to {} centimeters.'.format(feet,inches,cm))