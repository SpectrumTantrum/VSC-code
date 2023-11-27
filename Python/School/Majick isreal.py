import random

print("Welcome to the magic 8 ball, type a question and i will give you an answer!")

question = input()

answer = random.randint(1, 5)

if answer == 1:
    print("Yas")

elif answer == 2:
    print("Maybe")

elif answer == 3:
    print("You Played ur self")

elif answer == 4:
    print("IDK M8 Go ask google or something man, like y u du dis to mezz man?!")


else:
    print("Nu bish")
