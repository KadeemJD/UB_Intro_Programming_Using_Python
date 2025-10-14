# -*- coding: utf-8 -*-

"""
Use a for loop to count the number of occurrences of the letter 'a' in a string "banana".
"""

word = "banana"
count = 0

for i in word:
    if i == 'a':
        count += 1
print(f"The total a's in {word} is {count}")

