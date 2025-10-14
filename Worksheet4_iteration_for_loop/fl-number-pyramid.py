# -*- coding: utf-8 -*-
"""
 Use a nested for loop to print the following number pyramid:
1
12
123     
"""

n = 4

for i in range(1,n):
    for j in range(1,i+1):
        print(j, end="")
    print()