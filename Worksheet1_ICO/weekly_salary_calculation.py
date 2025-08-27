# -*- coding: utf-8 -*-

"""
Weekly Salary Calculation
Prompt the user to enter their hourly wage and the number of hours
worked in a week. Calculate and print the weekly salary.
"""

#User prompts
hourlyWage = input("Please enter hourly wage: ")
int_hourlyWage = int(hourlyWage)
numHoursWorked = input("Please enter the number of hours worked in a week: ")
int_numHoursWorked = int(numHoursWorked)

#Calculate weekly salary
weeklySalary = int_hourlyWage * int_numHoursWorked

#print results
print(f"The weekly salary is ${weeklySalary}")