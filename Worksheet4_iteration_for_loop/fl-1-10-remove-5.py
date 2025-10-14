# -*- coding: utf-8 -*-
# =============================================================================
# Use a for loop that calculates the sum of the is from 1 to 10,
#  but skips the number 5.
# =============================================================================


n = 11
sum=0

for i in range(1,n):
    if i != 5:
        sum += i
print (f"The sum is {sum}.")

