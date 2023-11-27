#To accept two numbers from the user and
#calculate the sum/difference/product/dividend of those numbers

print("This is a program that will add/subtract/multiply/divide 2 numbers.") 
print("For the best result please type in the bigger number first,")
print("then the smaller one next.")

#INPUT a
number_one = float(input("Give me one Number:"))

#INPUT b
number_two = float(input("Give me another Number:"))

#sum <-- INPUT a + INPUT b
result_add = number_one + number_two

#difference <-- INPUT a - INPUT b
result_sub = number_one - number_two

#product <-- INPUT a * INPUT b
result_multi = number_one * number_two

#dividend <-- INPUT a / INPUT b
result_div = number_one / number_two


#sum
print("This is the sum of the 2 numbers", result_add)
#difference
print("This is the difference of the 2 numbers", result_sub)
#product
print("This is the product of the 2 numbers", result_multi)
#dividend
print("This is the dividend of the 2 numbers", result_div)
