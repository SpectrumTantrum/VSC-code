counter = 1

while counter < 10:
    print("This line of code has been run",counter,"times")
    counter = counter + 1

password = "yayeet"
userInput = input("Enter your password:")
while userInput != password:
    print("Incorrect password provided")
    userInput = input("Enter your password: ")
print("Correct password provided!")

counter = 1

number = input()
result = int(number * counter)
while counter <= 10:
    result = 4 * counter
    print(result)

    counter = counter + 1
