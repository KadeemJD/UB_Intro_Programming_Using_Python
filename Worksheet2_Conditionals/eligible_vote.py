# -*- coding: utf-8 -*-

"""
Create a program that checks (prints) if a person is eligible to vote
 based on their age (must be 18 or older to vote).
"""

#input age

userAge = int(input("Please enter the age: "))

#calculate eligibility

if (userAge >= 18):
    print("You are eligible to vote!")

else:
    (userAge < 18)
    print("You are uneligible to vote!")



