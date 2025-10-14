# -*- coding: utf-8 -*-
"""
Write a for loop to count the number of consonants in the string "Computer".
 (hint: check while not vowel)

"""

word = "Computer"
count = 0

for i in word:
    if i not in ("a","e","i","o","u"):
        count += 1
print(f"The total consonants in {word} is {count}")