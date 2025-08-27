# -*- coding: utf-8 -*-

"""
Convert Kilometers to Meters
Write a program that asks the user to enter a distance in kilometers.
 Convert it to meters and print the result.
"""

# 1 kilometer = 1000 meters

#Get user input for kilometers
kilometers = input("Please enter the distance in kilometers: ")
kilometers = float(kilometers)
#Calculate kilometers to meters
meters = kilometers * 1000
#print result
print(f" {kilometers} kilometers is {meters} meters.")