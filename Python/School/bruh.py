import random

answer = random.randint(1,10)

userInput = "go"

while userInput != "stop":
    
userInput = input("I Have a random number between 1 and 10, Can you guess it:")

if userInput == answer:

    print("You are correct m8!!")

elif userInput > answer:

    print("So close yet so far, Ur answer is bigger than the actual answer")

elif userInput < answer:

    print("Yeh the actual answer is higher m8, try again?")
