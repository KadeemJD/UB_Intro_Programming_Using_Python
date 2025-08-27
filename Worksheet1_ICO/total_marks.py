# -*- coding: utf-8 -*-

"""
Total Marks Calculation
Request the user to enter marks obtained in three subjects. 
Compute the total marks and print the result.
"""

mark1 = input("Please enter the first mark: ")
mark1 = int(mark1)
mark2 = input("Please enter the second mark: ")
mark2 = int(mark2)
mark3 = input("Please enter the third mark: ")
mark3 = int(mark3)

totalMarks = mark1 + mark2 + mark3 
print(f"The total mark is {totalMarks}.")