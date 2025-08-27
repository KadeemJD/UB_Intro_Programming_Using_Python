# -*- coding: utf-8 -*-

"""
Total Distance Traveled
Ask the user to enter the distance traveled each day for a week. 
Calculate the total distance traveled over the week (7 days) and print it.
"""

#Get user input for distance traveled each day of the week
day1 = int(input("Please enter distance traveled for day 1 (miles): "))
day2 = int(input("Please enter distance traveled for day 2 (miles): "))
day3 = int(input("Please enter distance traveled for day 3 (miles): "))
day4 = int(input("Please enter distance traveled for day 4 (miles): "))
day5 = int(input("Please enter distance traveled for day 5 (miles): "))
day6 = int(input("Please enter distance traveled for day 6 (miles): "))
day7 = int(input("Please enter distance traveled for day 7 (miles): "))

#Calculate total distance traveled
totalDistance = day1 + day2 + day3 + day4 + day5 + day6 + day7

#print results
print(f"Total distance traveled is {totalDistance} miles.")

