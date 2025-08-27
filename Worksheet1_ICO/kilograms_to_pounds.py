# -*- coding: utf-8 -*-

"""
Convert Kilograms to Pounds
Prompt the user to enter a weight in kilograms. Convert it to pounds 
and print the result.
"""

#Get user input for weight in kilograms
weight_kilograms = input("What is your weight in kilograms? ")
weight_kilograms = float(weight_kilograms)
#Calculate weight in pounds
weight_pounds = weight_kilograms * 2.2
#print result
print(f"Your weight is {weight_pounds:.2f} pounds.")
