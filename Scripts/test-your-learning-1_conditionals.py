# -*- coding: utf-8 -*-

"""
Test your learning 1
Write a program that asks the user to enter
a number and then states whether the number
is even or odd
"""

"""
Example 1:
Enter an integer: 9
9 is an odd number.
Example 2:
Enter an integer: 2
2 is an even number.
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




