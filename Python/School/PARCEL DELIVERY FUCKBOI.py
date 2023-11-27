print("How heavy is this parcel in kg")
weight = float(input())

print("Is this local or international delivery?")
delivery = input()

if delivery == "local" or "Local":
    if weight > 5:
        cost = 20
        r_weight = weight - 5
        e_cost = cost + round(r_weight)
        print("The cost is", e_cost)
    else:
        cost = 20
        print("The cost is", cost)
elif delivery == "International" or "international":
    cost = 40
    print("The cost is", cost)
else:
    print("You have input something wrongly, please try again")
