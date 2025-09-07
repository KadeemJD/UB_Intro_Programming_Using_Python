# -*- coding: utf-8 -*-

# =============================================================================
# Implement a program that calculates and displays the final price after applying 
# a discount:
# 10% discount for amounts between $100-$500.
# 20% discount for amounts above $500.
# =============================================================================

discount_10 = 10/100
discount_20 = 20/100

#user input
originalPrice = float(input("Please enter the price: "))

#perform calculation
if originalPrice >= 100 and originalPrice <= 500:
    discount = discount_10 * originalPrice
    discountedPrice = originalPrice - discount
    print(f"Your final price after applying 10% discount is {discountedPrice:.2f}!")
elif originalPrice > 500:
    discount = discount_20 * originalPrice
    discountedPrice = originalPrice - discount
    print(f"Your final price after applying 20% discount is {discountedPrice:.2f}!")   
else:  
    print("Sorry, discount does not apply!")