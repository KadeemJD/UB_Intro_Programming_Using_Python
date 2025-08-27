# -*- coding: utf-8 -*-

"""
Perimeter of a Rectangle
Ask the user to enter the length and width of a rectangle. Compute the perimeter and display it.
"""
#P=2(l+w)

lenghtR = input("Please enter the lenght of your rectangle: ")
lenghtR = int(lenghtR) 
widthR = input("Please enter the width of your rectangle: ")
widthR = int(widthR)
perimeter = 2*(lenghtR+widthR)
print(f"The perimeter of your rectangle is {perimeter}.")

