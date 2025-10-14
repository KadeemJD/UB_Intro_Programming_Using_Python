# -*- coding: utf-8 -*-

"""
Use a for loop to count the number of vowels in the string "Programming".
"""
word = "Programming"
count = 0

for i in word:
    if i not in ("a","e","i","o","u"):
        count += 1
print(f"The total consonants in {word} is {count}")
