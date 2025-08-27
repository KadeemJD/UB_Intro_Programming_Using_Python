# -*- coding: utf-8 -*-

"""
Test your learning 1
Write a program that asks the user to enter
two strings. Your program should then
determine whether the two strings are equal
"""

"""
Example :
Enter a string: apple
Enter a string: blue
Are your strings equal? False
"""

# Ask the user for two strings
string1 = input("Please enter first string: ")
string2 = input("Please enter second string: ")

# Compare the user's two strings
answer = string1 == string2

# Print/Ouput the result of the string comparison
print(f"Is {string1} equivalent to {string2}? -> {answer}")