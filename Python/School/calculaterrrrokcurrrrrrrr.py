#ask user for operation +, -, *, /
#ask user for 2 numbers
#show result with chosen operation

print("What operation whould you like? (+)(-)(*)(/)")
operation = input()

print("What is your first number?")
a = float(input())

print("What is your second number?")
b = float(input())

addition = a + b
subtraction = a - b
multiply = a * b
divide = a / b


if operation == "+":
    print ("The sum is", addition)

elif operation == "-":
    print ("The difference is", subtraction)

elif operation == "*":
    print ("The product is", multiply)
    
elif operation == "/":
    print ("The result is", divide)

        

