# -*- coding: utf-8 -*-

# =============================================================================
# Test your learning 2
# Write a program that asks the user to
# enter a letter. Your program should then
# determine whether the letter is a vowel.
# =============================================================================


# =============================================================================
# Example 1:
# Enter a letter: x
# [x] is not a vowel.
# =============================================================================


# =============================================================================
# Example 2:
# Enter a letter: a
# [a] is a vowel.
# =============================================================================


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
    print(f"The letter '{letter}' is not a vowel.")
elif letter_lower == 'y' :
    print(f"The letter '{letter}' sometimes act as a vowel.")
else:
    print("The character entered is not a letter.")


