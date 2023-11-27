start = int(input("What is the start number:"))
finish = int(input("What is the finish number:"))
number = start

if start >= finish:
    print("error: the start is bigger than the finish")
else:
    for number in range (start,finish + 1):
        print(number)
        number = number + 1
