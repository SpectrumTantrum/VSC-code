#def happybirthday():
   # print("happy birthday to you")
    #print("happy birthday to you")
   # print("happy birthday to whatever name you are")
   # print("happy birthday to you")


def happybirthday(name):
    print("happy birthday to you")
    print("happy birthday to you")
    print("happy birthday to", name)
    print("happy birthday to you")

print("Enter your name:")
name = input()
happybirthday(name)

def poundConversion(hkd):

    pound = hkd / 10

    return pound

print("Enter amount to convert")
value = input()
value = int(value)
print(value,"HKD =", poundConversion(100), "Pound Sterling")

def euroConversion(hkd):

    euro = hkd / 8.6

    return euro

print("Enter amount to convert")
value = input()
value = int(value)
print(value,"HKD =", euroConversion(100), "Euros")

def usdConversion(hkd):

    usd = hkd / 7.8

    return usd

print("Enter amount to convert")
value = input()
value = int(value)
print(value,"HKD =", usdConversion(100), "USDs")
