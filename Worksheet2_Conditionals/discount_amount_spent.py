# -*- coding: utf-8 -*-

"""
Implement a program that calculates a discount based on the amount spent:
No discount for amounts less than $50.
5% discount for amounts between $50 and $200.
10% discount for amounts above $200.
"""


#User input
originalPrice = float(input("Please enter the original price: "))

#Calculation
if(originalPrice >= 50 and originalPrice <= 200):
    discountP1 = originalPrice * 0.05
    print(f"The discount is ${discountP1:.2f}")
    
elif(originalPrice > 200):
    discountP2 = originalPrice * 0.05
    print(f"The discount is ${discountP2:.2f}")
 
else:
    (originalPrice < 50)
    print("Sorry no discount!")    
    
