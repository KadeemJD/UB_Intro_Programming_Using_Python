# -*- coding: utf-8 -*-

#User input

x_coord = int(input("Please enter the x coordintate: "))
y_coord = int(input("Please enter the y coordinate: "))

if x_coord > 0 and y_coord > 0:
    print("Quadrant I.")
elif x_coord < 0 and y_coord > 0:
    print("Quadrant II.")
elif x_coord < 0 and y_coord < 0:
    print("Quadrant III.")
elif x_coord > 0 and y_coord < 0:
    print("Quadrant IV.")
else:
    print("You enterd a non-integer")
    