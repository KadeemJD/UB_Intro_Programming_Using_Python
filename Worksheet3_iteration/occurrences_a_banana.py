# -*- coding: utf-8 -*-

"""
Use a while loop to count the number of occurrences of the letter
 'a' in a string "banana".
"""

user_string = "banana"
occurrences = 0
index=0

#set up the while loop
while index < len(user_string):
    letter = user_string[index]
    if letter == 'a':
        occurrences += 1
        index += 1
    elif letter != 'a':
        index += 1
print(f"The number of a's in {user_string} is {occurrences}.")

