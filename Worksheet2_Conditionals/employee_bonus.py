# -*- coding: utf-8 -*-

# =============================================================================
# Implement a program that calculates a bonus for employees based on their years 
# of service and their current gross salary:
# 5 years or more: 10% bonus. Less than 5 years: 5% bonus.
# =============================================================================

#input employee year's of service
serviceYear = float(input("Enter your year's of service: "))
#input gross salary
grossSalary = float(input("Enter your gross salary: "))

#conditions

if(serviceYear >= 5):
    bonusValue = grossSalary * 0.10
    print(f"Your bonus is {bonusValue}.")

else:
    (serviceYear < 5)
    bonusValue = grossSalary * 0.05
    print(f"Your bonus is {bonusValue}.")