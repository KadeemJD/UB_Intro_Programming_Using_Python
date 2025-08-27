# -*- coding: utf-8 -*-

"""
Test your learning 2
Write a program that asks the user to enter
an integer. Your program should then
determine whether the integer is even (0, 2, 4, 6, etc.)
"""
                                     
"""                                      
Example:
Enter an integer: 5
Is 5 an even integer? False
"""

#Enter integer
integer = input("Please enter an integer: ")
integer = int(integer)
even = integer % 2 == 0
odd = integer % 2 == 1
print(f" {integer} is even? -> {even}, {integer} is odd? -> {odd} ")