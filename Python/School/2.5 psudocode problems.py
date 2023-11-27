start = int(input("What is the start number:"))
finish = int(input("What is the finish number:"))
number = start

if start >= finish:
    a = start
    b = finish
    finish = a
    start = b
    for number in range (start,finish + 1):
        print(number)
        number = number + 1
else:
    for number in range (start,finish + 1):
        print(number)
        number = number + 1
