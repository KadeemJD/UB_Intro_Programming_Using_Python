# -*- coding: utf-8 -*-
"""
Write a function called calculate_grade that takes an integer score as a parameter.
 The function should return the grade based on the following criteria:
score >= 90: return "A"
score >= 80: return "B"
score >= 70: return "C"
score >= 60: return "D"
Otherwise, return "F"

"""

def calculate_grade(score):
     if score >= 90:
         return "A"
     elif score >= 80:
         return "B"
     elif score >= 70:
         return "C"
     elif score >= 60:
         return "D"
     else:
         return "F"
    
result = calculate_grade(88)
print(result)