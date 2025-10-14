# -*- coding: utf-8 -*-
"""
Harvard CS50's Introduction to Programming'
"""

name = input("What is your name?: ").strip().title()

first, last = name.split(" ")
#Capitalize user's name
#name = name.capitalize()

#capitalize user's name
#name = name.title()

#,strip() remove white spaces
# =============================================================================
# print("Hello,")
# print(name)
# =============================================================================
print(f"Hello, {first}")

#print("hello, " + name)
#print("hello,",name)


