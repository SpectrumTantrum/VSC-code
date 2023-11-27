middaytemp = []
midnighttemp = []

for day in range(1,31):
    middayvali = False
    midnightvali = False
    while middayvali == False:
        middayvalue = int(input("Please input tempearture for midday:"))
        if 0 < middayvalue <= 40:
            middaytemp.append(middayvalue)
            middayvali = True
        else:
            print("Please enter a resonable temperature")    
    while midnightvali == False:
        midnightvalue = int(input("Please input tempearture for midday:"))
        if 0 < midnightvalue <= 40:
            midnighttemp.append(midnightvalue)
            midnightvali = True
        else:
            print("Please enter a resonable temperature")

print(middaytemp)
print(midnighttemp)

totaltempday = 0
totaltempnight = 0
nightavg = 0
dayavg = 0

for count in range(1,31):
    totaltempday = totaltempday + middaytemp[count]

for count in range(1,31):
    totaltempnight = totaltempnight + midnighttemp[count]

dayavg = totaltempday / 30
nightavg = totaltempnight / 30

print(dayavg)
print(nightavg)


minimum = 100
maximum = -99
daydate = 0
nightdate = 0

for count in range(1,31):
    if middaytemp[count] > maximum:
        maximum = middaytemp[count]
        daydate = count
    else:

for count in range(1,31):
    if midnighttemp[count] < minimum:
        minimum = midnighttemp[count]
        nightdate = count
    else:

print("The midday with the highest temperature is", maximum,"the date is",daydate)
print("The midnight with the lowest temperature is", minimum,"the date is",nightdate)

        
    
