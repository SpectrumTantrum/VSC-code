reject=0
total=0
totalPrice=0
discount=0
cementOrder=int(input("how many cement did the customer order"))
totalPrice=3*cementOrder+totalPrice
for counter in range(0,cementOrder):
    cementWeight=float(input("whts ur cement weight"))
    if cementWeight>=24.9 and cementWeight<=25.1:
        print("okay,your cement weight inputed is", cementWeight)
        total=total+cementWeight
    elif cementWeight>25.1:
        print("bad cuz ur cement is overweight")
        reject=reject+1
    elif cementWeight<24.9:
        print("bad cuz ur cement is underweight")
        reject=reject+1

gravelOrder=int(input("how many gravel did customer order"))
totalPrice=2*gravelOrder+totalPrice
for counter in range(0,gravelOrder):
    gravelWeight=float(input("whts ur gravel weight"))
    if gravelWeight>=49.9 and gravelWeight<=50.1:
        print("okay,your gravel weight inputed is", gravelWeight)
        total=total+gravelWeight
    elif gravelWeight>50.1:
        print("bad cuz ur gravel overweight")
        reject=reject+1
    elif gravelWeight<49.9:
        print("bad cuz ur gravel underweight")
        reject=reject+1
    
sandOrder=int(input("how many sand did customer order"))
totalPrice=2*sandOrder+totalPrice
for counter in range(0,sandOrder):
    sandWeight=float(input("whts ur sand weight"))
    if sandWeight>=49.9 and sandWeight<=50.1:
        print("okay,your sand weight inputed is", sandWeight)
        total=total+sandWeight
    elif sandWeight>50.1:
        print("bad cuz ur sand is overweight")
        reject=reject+1
    elif sandWeight<49.9:
        print("bad cuz ur sand underweight")
        reject=reject+1
while cementOrder >= 1 and gravelOrder >= 2 and sandOrder >= 2:
        cementOrder = cementOrder - 1
        gravelOrder = gravelOrder - 2
        sandOrder = sandOrder - 2
        totalprice = totalPrice + 10
        discount = discount + 1
        
totalPrice = totalPrice + cementOrder * 3 + gravelOrder * 2 + sandOrder * 2-discount*1
print("There have", discount,"discount packs")
print("You save $",discount)
print("The final price is $", totalPrice)
print("the total weight is",total)
print("the amount of reject is",reject)
print("the total price is", totalPrice)
