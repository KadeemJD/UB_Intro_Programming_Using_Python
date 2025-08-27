# -*- coding: utf-8 -*-

"""
Convert Gallons to Liters
Ask the user to input a volume in gallons. Convert it to liters and print the result.
"""

#For UK (Imperial) gallons: Multiply the number of gallons by 4.546

#User input for gallons
imperialGallons = input("Please enter the volume of gallons (UK/Imperial): ")
imperialGallons = float(imperialGallons)
#Convert gallons to liters
liters = imperialGallons * 4.546
#Print your results
print(f"The gallons entered is {liters:.2f} liters.")