# -*- coding: utf-8 -*-
"""
Write a function called triangle_type that takes three integers representing the lengths
 of the sides of a triangle as parameters. The function should return "Equilateral" if all sides are equal, 
 "Isosceles" if exactly two sides are equal, and "Scalene" if all sides are different.
"""

def triangle_type(int1,int2,int3):
    if int1 == int2 == int3:
        return "Equilateral"
    elif int1 == int2 :
        return "Isosceles"
    elif int1 != int2 != int3:
        return "Scalene"
    
result = triangle_type(2, 2, 3)
print(result)