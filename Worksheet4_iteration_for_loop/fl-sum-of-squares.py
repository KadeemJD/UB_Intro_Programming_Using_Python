# -*- coding: utf-8 -*-
"""
Use a for loop to calculate the sum of squares of
 even is from 1 to 20.
"""
n = 21
sum=0
i2 = 0

for i in range(1,21):
    if i % 2 == 0:
        i2 = i ** 2
        sum += i2
print (f"The sum is {sum}.")

