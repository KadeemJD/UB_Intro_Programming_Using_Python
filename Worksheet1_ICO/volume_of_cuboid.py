# -*- coding: utf-8 -*-

"""
Volume of a Cuboid
Write a program that prompts the user for the length, width, and height of a 
cuboid. Calculate the volume and print it.
"""

#Volume = Length × Width × Height

lengthCuboid = input("Please enter the lenght of your cuboid: ")
lengthCuboid = int(lengthCuboid)
widthCuboid = input("Please enter the width of your cuboid: ")
widthCuboid = int(widthCuboid)
heightCuboid = input("Please enter the height of your cuboid: ")
heightCuboid = int(heightCuboid)
volume = lengthCuboid*widthCuboid*heightCuboid
print(f"The volume of your cuboid is {volume}.")
