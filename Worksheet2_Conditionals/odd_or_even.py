# -*- coding: utf-8 -*-

"""
Write a program that asks the user to input an integer and checks (prints) 
 whether  it’s odd or even.
"""



#Ask the user for the number

userNum = input("Please enter integer: ")
int_userNum = int(userNum)

# Determine if the number is even or odd
if int_userNum % 2 == 0:
    #Print the results
    print(f"The integer {userNum} is even!")
elif int_userNum % 2 == 1:
    print(f"The integer {userNum} is odd!")