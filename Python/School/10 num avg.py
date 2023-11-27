counter = 0
total = 0
for counter in range(0,10):
    value = int(input("Please enter a number:"))
    total = total + value
    counter = counter + 1
    
average = total / 10
print(average)
