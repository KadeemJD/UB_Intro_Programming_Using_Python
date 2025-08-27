# -*- coding: utf-8 -*-

"""
Area of a Circle
Request the user to input the radius of a circle. Calculate and display
 the area of the circle.
"""
#radius=A=πr2

pi = 3.14

radius = input("Please enter the radius of your circle: ")
radius = int(radius)
area = pi*(radius ** 2)
print(f"The area of your circle is {area}.")