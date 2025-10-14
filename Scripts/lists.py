# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 08:12:57 2025

@author: Kadee
"""

# =============================================================================
# list()
# 
# values = [1,2,3]
# 
# fruits = ["Apple", "Plum", "Guava"]
# 
# fruit
# 
# #dir() then 

#with len you can see how many characters in a string, or to check the lenght of items in a list
# =============================================================================


total = 0
values = []
while (True):
    val = float(input("Please enter the cost or -1 to quit: "))
    if val == -1:
        break
    values.append(val)

if len(values) == 0:
    print("You did not enter any values!")
else:
    #find the sum
    total = sum(values)
    print(f"The sum of the values is {total}")



# range (start, end, step) three arguments
# if going backwards you gotta 
#list(range(5,1,-1))

#for odd numbers range(1,1,2)