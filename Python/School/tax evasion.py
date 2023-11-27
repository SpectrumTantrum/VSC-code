#accept raw price of product
#calculate 2% tax
#output tax and total price


print("What is the raw price of the product?")

#Raw Price
raw_price = float(input())

#Tax = INPUT A / 100 * 2
tax = raw_price / 100 * 2

#Total Price = INPUT A + Tax
total_price = raw_price + tax

#Rounding off 2% Tax to 2 decimal place and Presenting
print("The 2% of tax will be", round(tax, 2))

#Rounding off Total Price to 2 decimal place Presenting
print("So the total price will be", round(total_price, 2))
