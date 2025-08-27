# -*- coding: utf-8 -*-

"""
Total Payment After Discount
Ask the user to input the original price and the discount percentage. 
Calculate and display the price after the discount.
"""

#User input
originalPrice = input("Please enter the original price: ")
float_originalPrice = float(originalPrice)
discountPercentage = input("Please enter discount percentage(%): ")
float_discountPercentage = float(discountPercentage)
#Calculation
discount = (float_discountPercentage / 100) * float_originalPrice
priceAfterDiscount = float_originalPrice - discount
#Print results
print(f"The price after discount in ${priceAfterDiscount:.2f}.")