# -*- coding: utf-8 -*-

"""
Write a program that finds (prints) the smallest of three numbers
 entered by the user.
"""

#Ask the user for the number

userNum1 = input("Please enter the first number: ")
float_userNum1 = float(userNum1)
userNum2 = input("Please enter the second number: ")
float_userNum2 = float(userNum2)
userNum3 = input("Please enter the third number: ")
float_userNum3 = float(userNum3)

# Determine which number is smallest of the three
if (float_userNum1 < float_userNum2 and float_userNum1 < float_userNum3):
    #Print the results
    print(f"{float_userNum1} is the smallest number!")
elif (float_userNum2 < float_userNum1 and float_userNum2 < float_userNum3):
    print(f"{float_userNum2} is the smallest number!")
elif (float_userNum3 < float_userNum1 and float_userNum3 < float_userNum2):
    print(f"{float_userNum3} is the smallest number!")

