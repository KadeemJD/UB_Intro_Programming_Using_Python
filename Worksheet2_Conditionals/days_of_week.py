# -*- coding: utf-8 -*-

# =============================================================================
# Write a program that asks the user for a number between 0 and 6 and
#  displays the corresponding weekday. 0 is Sunday and 6 is Saturday.
# =============================================================================

#User input

weekNum = int(input("Please enter a number between 0 and 6: "))

if weekNum == 0:
    print("Sunday.")
elif weekNum == 1:
    print("Monday.")
elif weekNum == 2:
    print("Tuesday.")
elif weekNum == 3:
    print("Wednesday.")
elif weekNum == 4:
    print("Thursday.")
elif weekNum == 5:
    print("Friday.")
elif weekNum == 6:
    print("Saturday.")
