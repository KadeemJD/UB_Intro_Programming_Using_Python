# -*- coding: utf-8 -*-

"""
Area of a Parallelogram
Request the base length and height of a parallelogram from the user.
 Calculate and display the area.
"""

# Area = base * height

base = input("Please enter the base of your parallelogram: ")
base = int(base)
height = input("Please enter the height of your parallelogram: ")
height = int(height)
areaOfParallelogram = base * height
print(f"The area of your parallelogram is {areaOfParallelogram}.")