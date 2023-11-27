presents = []

while presents != "stop":

    add = input("Hello, what present do you want from Santa?")

    presents.append(add)

    print(presents)

    amount = int(input("and how many of that item do you desire, pls only type numbers"))

    presents.append(amount)

    print(presents)

    if stop != "stop":
        presents.append(stop)

print(presents)
