number = int(input("pls enter a number:"))
counter = 0
for x in range(1,number):
    print(x)
    counter = counter + x

print(number)
print(counter + number)


presents = []

for x in range(0,5):
    gift = input("bruh make a shopping list:")
    presents.append(gift)

for present in presents:
    print("you get", present)



word = input("please type a word:")
vowcount = 0
for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowcount = vowcount + 1

print(word,"has",vowcount,"vowels")
