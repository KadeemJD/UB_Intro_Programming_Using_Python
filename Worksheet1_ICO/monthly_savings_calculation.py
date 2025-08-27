# -*- coding: utf-8 -*-

"""
Monthly Savings Calculation
Request the user to enter their monthly savings amount and the number of months. 
"""

#Input from user
monthlySavings = input("Please enter the monthly savings amount: ")
monthlySavings = int(monthlySavings)
nMonths = input("Please enter the number of months:  ")
nMonths = int(nMonths)
#Calculate total saved
totalSaved = monthlySavings * nMonths
#Print results
print(f"Your total saved is ${totalSaved}.")