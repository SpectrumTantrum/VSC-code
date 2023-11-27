

print("Helloe and welcum to the CCC wildlife park.")
print("The cost for one day at the wildlife park are ass folloes:")
print("The cost for one adult is $20.00")
print("The cost for one child is $12.00 Keep in mind that one adult may only bring up to two children.")
print("The cost for one senior is $16.00")
print("The cost for one family ticket is $60.00 Keep in mind that the family ticket contains addmission for up to two adults or seniors and three children only")
print("The cost of groups of six people or more, price per person is $15.00")
print("The cost for two days at the wildlife park are ass folloes:")
print("The cost for one adult is $30.00")
print("The cost for one child is $18.00 Keep in mind that one adult may only bring up to two children.")
print("The cost for one senior is $24.00")
print("The cost for one family ticket is $90.00 Keep in mind that the family ticket contains addmission for up to two adults or seniors and three children only")
print("The cost of groups of six people or more, price per person is $22.50")
print("The cost for the Extra attraction are ass folloes:")
print("The cost for extra attractions the wildlife park are ass folloes:")
print("The cost for lion feeding is $2.50 per person.")
print("The cost penguin feeding is $2.00 per person.")
print("The cost for evening barbacue is $5.00 per person This option is only avaliable for people who have booked two day tickets only.")

ticketing = "y"
cart = []

oneadult = float(20.00)
twoadult = float(30.00)

onechild = float(12.00)
twochild = float(18.00)

onesenior = float(16.00)
twosenior = float(24.00)

onefamilyticket = float(60.00)
twofamilyticket = float(90.00)

onegroup = float(15.00)
twogroup = float(22.50)

lionfeeding = float(2.50)
penguinfeeding = float(2.00)
eveningbarbacue = float(5.00)

Bookref = 0
BookRefs = []
BookingDays = []
BookingCost = []

TotalGuests = 0
TotalAttractions = 0

DayOptions = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print("Days currently available for bookings")
print("======================================")
print("Monday")
print("Tuesday")
print("Wednesday")
print("Thursday")
print("Friday")
print("Saturday")
print("Sunday")


while ticketing == "y":
    if BookRef in BookRefs:
        BookRef = BookRef + 1
    VisitDay = input("Enter the day/first day of visit:\n")
    while VisitDay not in DayOptions:
        VisitDay = input("ERROR, enter the day/first day of visit:\n")
    VisitLength = int(input("Enter 1 or 2 for 1 day or 2 day ticket options:\n"))
    while VisitLength != 1 and VisitLength != 2:
        VisitLength = int(input("ERROR Enter 1 or 2 for 1 day or 2 day ticket options:\n"))

    Adult = int(input("Enter number of Adult tickets required:\n"))
    Child = int(input("Enter number of Child tickets required:\n"))
    Senior = int(input("Enter number of Senior tickets required:\n"))
    Family = int(input("Enter number of Family tickets required:\n"))
    Group = int(input("Enter number of Group tickets required:\n"))
    Lion = int(input("Enter number of Lion feeding tickets required:\n"))
    Penguin = int(input("Enter number of Penguin feeding tickets required:\n"))

    if VisitLength == 1:
        TotalNormal = (Adult * 20) + (Child * 12) + (Senior * 16)
        TotalOther = (Family * 60) + (Group * 15)
        TotalAttractions = (Lion * 2.5) + (Penguin * 2.5)
        Total = TotalNormal + TotalOther + TotalAttractions

    
    else:
        Bbq = int(input("Enter number of BBQ tickets required:\n"))
        TotalNormal = (Adult*30)+(Child*18)+(Senior*24)
        TotalOther = (Family*90)+(Group*22.5)
        TotalAttractions = (Lion* 2.5)+(Penguin*2.5)+(Bbq*5)
        Total = TotalNormal + TotalOther + TotalAttractions  
              
    
    BookRefs.append(BookRef)
    BookingDays.append(VisitDay)
    BookingCost.append(Total)

    print("\n")
    print("BOOKING DETAILS")           
    print("The unique booking reference number is:",BookRef)
    if VisitLength == 1:
        print("The booking is for",VisitDay)
    else:
        print("The booking starts on",VisitDay, "and includes the following day.")

    print("The total price of the booking is:$",Total)

    ticketing = input("Enter 'y' to start another booking or any other key to quit:\n")

print("\n")
print("Bookings completed in this session")  #Not needed but useful as a check  
for i in range (0, len(BookRefs)):
    print("Booking:",BookRefs[i],"Day/Startday:",BookingDays[i], "Booking cost: $",BookingCost[i])
        
print("PROGRAM TERMINATED")

