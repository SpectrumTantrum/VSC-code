numbers = []
counter = 0

for counter in range(0,5):
    numbers.append(int(input("please enter a number:")))

print(numbers)
if numbers[0] >= numbers[1] and numbers[2] and numbers[3] and numbers[4]:
    print(numbers[0])
elif numbers[1] >= numbers[0] and numbers[2] and numbers[3] and numbers[4]:
    print(numbers[1])
elif numbers[2] >= numbers[1] and numbers[0] and numbers[3] and numbers[4]:
    print(numbers[2])
elif numbers[3] >= numbers[1] and numbers[2] and numbers[0] and numbers[4]:
    print(numbers[3])
else:
    print(numbers[4])

print(max(numbers))
