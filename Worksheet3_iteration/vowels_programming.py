# -*- coding: utf-8 -*-
"""
Use a while loop to count the number of vowels in the string "Programming".
"""

word = 'Programming'
index = len(word) - 1
total = 0

while index >= 0:
    if word[index].lower() in ("a","e","i","o","u"):
        total += 1
    index -= 1
print(f"there are {total} vowels in {word}.") 
    