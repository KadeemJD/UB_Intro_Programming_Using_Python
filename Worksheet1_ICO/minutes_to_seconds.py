# -*- coding: utf-8 -*-

"""
Convert Minutes to Seconds
Ask the user to input a time in minutes. Convert it to seconds and display the result.
"""

timeInMinutes = input("Please enter the time in minutes: ")
timeInMinutes = int(timeInMinutes)
sec = timeInMinutes * 60 
print(f"The conversion of the minutes entered is {sec} seconds.")