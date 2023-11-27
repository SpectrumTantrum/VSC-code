leap = input("BUT WAIT IS THE YEAR NOW A LEAP YEAR?")

month = "go"

while month != "stop":

    month = input("Enter a month, i'll tell you da amount of days it has")

    if month == "january":
        print("31 Days")

    elif month == "february":
        if leap == "yes":
            print("29 Days")
        else:print("28 Days")

    elif month == "march":
       print("31 Days")

    elif month == "april":
        print("30 Days")

    elif month == "may":
        print("31 Days")

    elif month == "june":
        print("30 Days")

    elif month == "july":
        print("31 Days")

    elif month == "august":
        print("31 Days")

    elif month == "september":
        print("30 Days")

    elif month == "october":
        print("31 Days")

    elif month == "november":
        print("30 Days")

    elif month == "december":
        print("31 Days")

