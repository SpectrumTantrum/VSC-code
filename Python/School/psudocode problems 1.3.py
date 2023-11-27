print("Please input the length of the square")
length = input("Length:")
if int(length) < 0:
    print("Error, the length is negative")
else:
    area = int(length) * int(length)
    print("The area is", area)
    
