# -*- coding: utf-8 -*-

"""
Convert Inches to Centimeters
Ask the user to enter a length in inches. Convert it to centimeters and print the result.
"""

# 1inch = 2.54cm

lenghtInInches = input("Please enter a lenght in inches: ")
lenghtInInches = int(lenghtInInches)
cm = lenghtInInches * 2.54
print(f"The lenght in inches you entered converted to centimeters is {cm}.")

