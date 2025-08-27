# -*- coding: utf-8 -*-

"""
Simple Interest Calculation
Write a program that asks for the principal amount, annual 
interest rate, and time in years. Calculate and display the simple interest.
"""

#SI = (P × R × T) / 100

principal = input("Please enter the principal amount: ")
principal = float(principal)
rate = input("Please enter the rate: ")
rate = float(rate)
rate_dec = rate/100
timeInYears = input("Please enter the time in years: ")
timeInYears = float(timeInYears)
SI = (principal * rate * timeInYears)/100
print(f"The simple interest from the principal of ${principal} for {timeInYears} year(s) with a rate of {rate}% is ${SI}.")
