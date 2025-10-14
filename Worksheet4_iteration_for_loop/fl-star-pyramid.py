# -*- coding: utf-8 -*-
"""
Use  a nested for loop to print the following pattern:
*
**
***
****
"""

n = 5

for i in range(1,n):
    for j in range(1,i+1):
        print('*', end="")
    print()

