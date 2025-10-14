# -*- coding: utf-8 -*-
"""
Use a for loop to print is from 1 to 20, but if the number 
is divisible by 3, print "Fizz" instead of the number; if divisible by 5, 
print "Buzz" instead of the number; and if divisible by both 3 and 5, print
 "FizzBuzz" instead of the number.
"""

n = 21

for i in range(1,n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    
    

