# -*- coding: utf-8 -*-

"""
Write a program that asks the user for their age and prints whether
 they are a child (0-12), teenager (13-19), adult (20-59), or senior (60+).
"""

#Input user age

userAge = int(input("Please enter your age: "))

#conditional for child, teenager, adult, senior

if (userAge >= 0 and userAge <= 12):
    print("you are a child.")
elif (userAge >= 13 and userAge <= 19):
    print("you are a teenager.")
elif (userAge >= 20 and userAge <= 59):
    print("you are an adult.")
else:
    (userAge >= 60)
    print("you are a senior.")