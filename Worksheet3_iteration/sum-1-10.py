# -*- coding: utf-8 -*-

"""
Use  a while loop to calculate the sum of the numbers from 1 to 10.
"""

counter = 0
total = 9
totalSum = 0
#set up the while loop
while counter <= total:
    counter = counter + 1
    current_number= counter
    totalSum = totalSum + current_number
print(f"{totalSum}")