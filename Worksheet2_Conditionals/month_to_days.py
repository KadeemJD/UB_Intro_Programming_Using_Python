# -*- coding: utf-8 -*-

"""
Write a program that takes the month number as input and displays the
 number of days in that month.
"""

# =============================================================================
# 1 = Jan(31), 2 = Feb(28), 3 = Mar(31), 4 = Apr(30), 5 = May(31), 6 = Jun(30), 7=Jul(31),
# 8=Aug(31), 9=Sep(30) 10= Oct(31), 11=Nov(30), 12=Dec(31)
# =============================================================================



#user input
month = input("Please enter the number of the month: ")
int_month = int(month)

#perform calculation to determine month
if  (int_month == 1 or int_month == 3 or int_month == 5 or int_month == 7 or
    int_month == 8 or int_month == 10 or int_month == 12):
    print(f" your month has 31 days.")
if  (int_month == 4 or int_month == 6 or int_month == 9 or int_month == 11):
    print(f" your month has 30 days.")
if  (int_month == 2):
    print(f" your month has 28 days.")
