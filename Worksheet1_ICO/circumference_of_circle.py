# -*- coding: utf-8 -*-

"""
Circumference of a Circle
Request the radius of a circle from the user. Calculate and display
 the circumference of the circle.
"""

#C=2πr (formula for circumference of a circle)

#Request user input for radius
radius = input("Please enter radius: ")
radius = int(radius)
#calculate circumference
c = 2 * 3.14 * radius
#print results
print(f"The circumference of the circle is {c}.")
