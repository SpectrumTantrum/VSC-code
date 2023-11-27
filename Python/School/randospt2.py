def listlength(numbers):
    counterpos = 0
    for x in numbers:
        if x > 0:
            counterpos = counterpos + 1

    return counterpos

def neglistlength(numbers):
    counterneg = 0
    for x in numbers:
        if x < 0:
            counterneg = counterneg + 1

    return counterneg
   
numbers = [-3, 4, -5, 9, -7, 2, -1]
print (listlength(numbers))
print (neglistlength(numbers))


