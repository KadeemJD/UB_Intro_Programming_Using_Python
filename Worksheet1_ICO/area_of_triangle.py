# -*- coding: utf-8 -*-

"""
Area of a Triangle
Request the base and height of a triangle from the user. Calculate 
and print the area of the triangle
"""

#A = ½ (b × h)

base = input("Please enter the base of your triangle: ")
base = int(base)
height = input("Please enter the height of your triangle: ")
height = int(height)
areaOfTriangle = 0.5 * (base * height)
print(f"The area of your triangle is {areaOfTriangle}.")