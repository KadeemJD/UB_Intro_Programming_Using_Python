# -*- coding: utf-8 -*-

"""
Area of a Square
Write a program that asks the user for the side length of a square. 
Calculate and display the area.
"""

# A=a**2 (area of a square)

#User input for side length of square
side_length = input("Please input the side length of your square: ")
side_length = int(side_length)
#Calculation of area of square
a = side_length ** 2
#print results
print(f"The area of your square is {a}.")