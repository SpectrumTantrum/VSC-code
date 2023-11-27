def listlength(numbers):
    counter = 0
    for x in numbers:
        counter = counter + 1

    return counter
        
numbers = [3, 4, 5, 9, 7, 2, 1]
listsize = listlength(numbers)
print (listsize)

def newlistlength(nnumbers):
    ncounter = 0
    for x in nnumbers:
        if x > 0:
            ncounter = ncounter + 1

    return ncounter

nnumbers = [-4, 6, -2, 10, 6]
print (newlistlength(nnumbers))



        
