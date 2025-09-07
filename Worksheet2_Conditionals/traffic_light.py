# -*- coding: utf-8 -*-

# =============================================================================
# Create a program that simulates a traffic light. Based on user input 
# (Red, Yellow, Green), display (print)  the corresponding
# action (Stop, Slow down, Go).
# =============================================================================

#user input
color = (input("Please enter the color: ")).lower()

# determining color
if color == 'red':
    print("Stop!")
if color == 'yellow':
    print("Slow down!")    
if color == 'green':
    print("Go!")

