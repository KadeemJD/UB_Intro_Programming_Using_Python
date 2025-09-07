# -*- coding: utf-8 -*-

"""
Write a program that checks if an entered integer is divisible by both 3 and 5.
"""

#enter integers
userInteger = int(input("Enter an integer: "))

#calculate if they are divisible by BOTH 3 AND 5!
if userInteger % 3 == 0 and userInteger % 5 == 0:
    print(f"{userInteger} is divisible by both 3 and 5.")
else:
    print(f"Sorry, {userInteger} is NOT divisible by both 3 and 5!")