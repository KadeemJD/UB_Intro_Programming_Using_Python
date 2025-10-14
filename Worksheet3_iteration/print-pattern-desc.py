# -*- coding: utf-8 -*-

"""
Use a nested while loop to print the following pattern:
"""

i = 4

while i >= 1:
    j = 1
    while j <= i:
        print("*", end = "")
        j += 1
    print()
    i -= 1