# -*- coding: utf-8 -*-

"""
Create a simple calculator that asks the user for two numbers and an 
operation (+, -, *, /), then performs  the calculation and displays the result.
"""

#user input
userNum1 = input("Please enter the first number: ")
float_userNum1 = float(userNum1)
userNum2 = input("Please enter the second number: ")
float_userNum2 = float(userNum2)
operation = input("Please enter the operation: ")

#perform calculation
if operation == '+':
    result = float_userNum1 + float_userNum2
    print(f"{float_userNum1} + {float_userNum2} = {result}")
if operation == '-':
    float_userNum1 - float_userNum2
    result = float_userNum1 - float_userNum2
    print(f"{float_userNum1} - {float_userNum2} = {result}")
if operation == '*':
    float_userNum1 * float_userNum2
    result = float_userNum1 * float_userNum2
    print(f"{float_userNum1} * {float_userNum2} = {result}")
if operation == '/':
    float_userNum1 / float_userNum2
    result = float_userNum1 / float_userNum2
    print(f"{float_userNum1} / {float_userNum2} = {result}")
    
