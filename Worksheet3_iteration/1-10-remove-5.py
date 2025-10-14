# -*- coding: utf-8 -*-

# =============================================================================
# Use a while loop that calculates the sum of the numbers from 1 to 10,
#  but skips the number 5.
# =============================================================================

number = 1
sum=0

while number <= 10:
    if number != 5:
        sum += number
    number += 1
print (f"The sum is {sum}.")
