# -*- coding: utf-8 -*-

"""
Use a while loop to print numbers from 1 to 20, but if the number 
is divisible by 3, print "Fizz" instead of the number; if divisible by 5, 
print "Buzz" instead of the number; and if divisible by both 3 and 5, print
 "FizzBuzz" instead of the number.
"""

number = 1

while number <= 20:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    
    number += 1