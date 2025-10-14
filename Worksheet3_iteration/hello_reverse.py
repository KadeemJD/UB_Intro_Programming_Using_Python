# -*- coding: utf-8 -*-
"""
Use a while loop to print the characters of the string "hello" in reverse order.
"""

word = "hello"
index = len(word)-1

while index >= 0:
    print(word[index])
    index -= 1