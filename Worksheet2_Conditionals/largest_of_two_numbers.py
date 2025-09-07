# -*- coding: utf-8 -*-

"""
Write a program to find (print) the largest of two numbers entered by the user.
"""

#Ask the user for the number

userNum1 = input("Please enter the first number: ")
float_userNum1 = float(userNum1)
userNum2 = input("Please enter the second number: ")
float_userNum2 = float(userNum2)

# Determine which number number is largest
if float_userNum1 > float_userNum2:
    #Print the results
    print(f"{float_userNum1} is larger than {float_userNum2}!")
else:
    print(f"{float_userNum2} is larger than {float_userNum1}!")
