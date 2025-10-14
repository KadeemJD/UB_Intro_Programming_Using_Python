# -*- coding: utf-8 -*-

"""
for loop
"""

# =============================================================================
# for ____ in _____ :
    action
    
 for i in [1,2,3,4,5]:
     print("hello")
     
     range(1,6) #this prints up to 5, it ends just before the number for the last digit
# =============================================================================

# =============================================================================
# nums = [1,2,3,4,5]
# nums
# 
# sum_odd = 0
# =============================================================================
sum_odd = 0

for i in range(1,51):
    if i % 2 == 1:
        sum_odd += i
print(sum_odd)


values = [-11,23.5,100,39.5]
smallest = values[0]

for i in values:
    if i < smallest:
        smallest = 1
print(f"the smallest is {smallest}")


word = "banana"
counr = 0
for i in word:
    if i == 'a':
        count = count + 1

print(count)



for i in range(1,6):
    for j in range(1, i + 1):
        print("*", end = "")
    print()
