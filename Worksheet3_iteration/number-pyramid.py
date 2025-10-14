# -*- coding: utf-8 -*-

"""
 Use a nested while loop to print the following number pyramid:
"""

# =============================================================================
# i = 1
# 
# while i <= 4:
#     j = 1
#     while j <= i:
#         print("1", end = "")
#         j += 1
#     print()
#     i += 1
# =============================================================================
    
row = 1

while row <= 4:
    num = 1
    while num <= row:
        print(num, end="")
        num += 1
    print()  # moves to the next line
    row += 1