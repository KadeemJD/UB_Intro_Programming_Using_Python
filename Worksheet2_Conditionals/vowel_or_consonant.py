# -*- coding: utf-8 -*-

"""
Create a program that checks(prints) if an entered character is a 
vowel or consonant.
"""

# Ask the user to enter a letter
letter = input("Please enter a letter: ")
letter_lower = str(letter.lower())

#Determine if the letter is a vowel
if (letter_lower == 'a' or letter_lower == 'e' or letter_lower == 'i'
 or letter_lower == 'o' or letter_lower == 'u'):
    print(f"The letter '{letter}' is a vowel.")
elif (letter_lower == 'b' or letter_lower == 'c' or letter_lower == 'd' or 
letter_lower == 'f' or letter_lower == 'g' or letter_lower == 'h' or letter_lower == 'j' or
letter_lower == 'k' or letter_lower == 'l' or letter_lower == 'm' or letter_lower == 'n' or
letter_lower == 'p' or letter_lower == 'q' or letter_lower == 'r' or letter_lower == 's' or
letter_lower == 't' or letter_lower == 'v' or letter_lower == 'w' or letter_lower == 'x' 
or letter_lower == 'z'):
    print(f"The letter '{letter}' is a consonant.")
elif letter_lower == 'y' :
    print(f"The letter '{letter}' sometimes act as a vowel.")
else:
    print("The character entered is not a letter.")

