# -*- coding: utf-8 -*-

"""
Create a program that checks (prints) if an entered integer
 is positive, negative, or zero.
"""

#Ask the user for the integer

userNum = input("Please enter integer: ")
int_userNum = int(userNum)

# Determine if the number is positive, negative or zero
if int_userNum > 0:
    #Print the results
    print(f"The integer {userNum} is positive!")
elif int_userNum < 0:
    print(f"The integer {userNum} is negative!")
else:
    print(f"The integer is zero!")
