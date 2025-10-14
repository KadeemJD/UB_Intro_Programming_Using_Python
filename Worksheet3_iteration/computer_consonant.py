# -*- coding: utf-8 -*-

"""
Write a while loop to count the number of consonants in the string "Computer".
 (hint: check while not vowel)
"""

word = 'Computer'
index = len(word) - 1
total = 0

while index >= 0:
    if word[index].lower() not in ("a","e","i","o","u"):
        total += 1
    index -= 1
print(f"there are {total} vowels in {word}.") 
    