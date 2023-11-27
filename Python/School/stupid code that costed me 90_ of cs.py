answer = 1
while answer != 0:
    
    print("this program will determine ur grade.")

    answer = input()

    answer = int(answer)

    if answer >= 80:
        print("A")

    elif answer >= 70:
        print("B")

    elif answer >= 60:
        print("C")

    elif answer < 60 and answer > 0:
        print("D")
       
