numbers = []
counternum = 0
total = 0

for counternum in range(0,6):
    numbers.append(int(input("please enter a number:")))
    total = total + numbers[counternum]

print(total) 
