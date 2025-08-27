# -*- coding: utf-8 -*-

"""
Price with Tax
Prompt the user to enter the price of an item and the sales tax rate. 
Calculate the total price including tax and display it.
"""

#The standard sales tax rate in Belize is 12.5%. The tax is officially
#called the General Sales Tax (GST) and applies to most goods and services.
 
priceOfItem = input("Please enter the price of your item: ")
priceOfItem = float(priceOfItem)
salesTaxRate = input("Please enter the sales tax rate: ")
salesTaxRate= float(salesTaxRate)
salesTaxRate_dec= (salesTaxRate / 100) * priceOfItem
totalPrice= priceOfItem + salesTaxRate_dec
print(f"The total cost of your item of ${priceOfItem} with a sales tax rate of {salesTaxRate}% is ${totalPrice}.")
