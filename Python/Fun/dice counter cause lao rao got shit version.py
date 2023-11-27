import random


#def dice():
    #diceResult = random.randint(1,6)

    #return diceResult

def dice4():
    d4r = random.randint(1,4)

    return d4r

def dice6():
    d6r = random.randint(1,6)

    return d6r

def dice8():
    d8r = random.randint(1,8)

    return d8r

def dice10():
    d10r = random.randint(1,10)

    return d10r

def dice12():
    d12r = random.randint(1,12)

    return d12r

def dice20():
    d20r = random.randint(1,20)

    return d20r

def dice100():
    d100r = random.randint(1,100)

    return d100r

#roll = "go"

#while roll != "stop":

choosedie = "go"

while choosedie != "stop":
    
    counterd4 = 0
    counterd6 = 0
    counterd8 = 0
    counterd10 = 0
    counterd12 = 0
    counterd20 = 0
    counterd100 = 0
    
    print("I am dice bot")
    print("The program made to completly destroy lao rao's shit dice counter")

    #roll = int(input("So how many 6-sided dice you want to roll:"))

    choosedie = input("what dice do you want to use (d4, d6, d8, d10, d12, d20, d100):")

    if choosedie == "d4":
        rolld4 = int(input("So how many 4-sided dice you want to roll:"))
        instantmodifier = input("Do you want the total value of the dice immidiately:")
        if instantmodifier == "yes"
            instantd4 = random.randint(1,4)
        while counterd4 <= rolld4:
            print("the",counterd4,"number is",dice4())
            counterd4 = counterd4 + 1

    elif choosedie == "d6":
        rolld6 = int(input("So how many 6-sided dice you want to roll:"))
        while counterd6 <= rolld6:
            print("the",counterd6,"number is",dice6())
            counterd6 = counterd6 + 1

    elif choosedie == "d8":
        rolld8 = int(input("So how many 8-sided dice you want to roll:"))
        while counterd8 <= rolld8:
            print("the",counterd8,"number is",dice8())
            counterd8 = counterd8 + 1

    elif choosedie == "d10":
        rolld10 = int(input("So how many 10-sided dice you want to roll:"))
        while counterd10 <= rolld10:
            print("the",counterd10,"number is",dice10())
            counterd10 = counterd10 + 1

    elif choosedie == "d12":
        rolld12 = int(input("So how many 12-sided dice you want to roll:"))
        while counterd12 <= rolld12:
            print("the",counterd12,"number is",dice12())
            counterd12 = counterd12 + 1

    elif choosedie == "d20":
        rolld20 = int(input("So how many 20-sided dice you want to roll:"))
        while counterd20 <= rolld20:
            print("the",counterd20,"number is",dice20())
            counterd20 = counterd20 + 1

    else:
        rolld100 = int(input("So how many 100-sided dice you want to roll:"))
        while counterd100 <= rolld100:
            print("the",counterd100,"number is",dice100())
            counterd100 = counterd100 + 1

    #while counter < roll:
        #print(dice())
        #counter = counter + 1
    
