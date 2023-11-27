counter = 0

number = int(input("please input a number"))

biggest = number

while counter != 10:
    number = int(input("please input a number"))
    counter = counter + 1
    if number > biggest:
        biggest = number
        

print(biggest)
