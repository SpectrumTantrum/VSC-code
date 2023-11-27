from datetime import datetime
from datetime import timedelta
from datetime import date
repeat=1
#Task-1: displaying the ticket options 
print("Ticket Type\t\t\t\t\t\t\tCost for one day\tCost for two days")
tickettype=["One Adult     ", "one child     ", "one senior   ", "family ticket", "Group/person"]
costoneday=[20,12,16,60,15]
costtwoday=[30,18,24,90,22.50]
ticketnumber=0
extatt=["Lion feeding    \t\t", "Penguin Feeding \t\t", "Evening Barbecue       "]
extcost=[2.50,2.00,5.00]  
#repeat of program till user's wish
while repeat==1:
  for i in range(0,5):
    print(tickettype[i],"\t\t\t\t\t\t\t\t",costoneday[i],"\t\t\t\t",costtwoday[i])

  #Task-1 contd..displaying the extra attractions available
  print("\n\nExtra Attraction\t\t\tCost per person")
  for i in range(0,3):
    print(extatt[i],"\t\t\t",extcost[i])
  #************
  #Task-1 contd...show the days available for booking; assume that there are tickets available for any valid day.
  print("\n\nSelect the date for booking (1-7): ")
  Begindatestring = date.today()
  print("1 :",Begindatestring) 
  for i in range(1,7):
    nextdate=Begindatestring + timedelta(days=i)
    print(i+1,":",nextdate) 
  datechoice=0
  while datechoice<1 or datechoice>7:
    datechoice=int(input("\nEnter date of booking (1-7)"))
  noofdays=0
  while noofdays<1 or noofdays>2:
    noofdays=int(input("Enter number of days :"))
    if datechoice==7 and noofdays==2:
      print("For 7th day,two days booking not allowed")
      noofdays=0

  adult=int(input("\n\nEnter total adults :"))
  senior=int(input("Enter total seniors :"))
  child=int(input("Enter total children :"))
  totaltickets=adult+child+senior
  lf=-1
  pf=-1
  eb=-1
  print("\nTotal Members :",totaltickets)
  while lf>totaltickets or lf<0:
    lf=int(input("\n\nEnter number of lion-feeding tickets,0 for none: "))
  while pf>totaltickets or pf<0:
    pf=int(input("Enter number of penguin-feeding tickets, 0 for none: " ))
  if noofdays==2:
    while eb>totaltickets or eb<0:
      eb=int(input("Enter number of evening barbecue tickets,0 for none: "))
  if eb==-1:
    eb=0
  #storing these numbers in temporary variables
  
  family=0
  #finding total families possible
  total=adult+senior
  #each family can be upto two adults or seniors and upto 3 children
  opt1=int(total/2)
  opt2=int(child/3)
  if opt1<opt2:
    family=opt1
  else:
    family=opt2
  #reduce adults, senior and children after family allocations.
  if family>0:
    child=child-(family*3)
    total=total-(family*2)
    if total==0 and child>0:
      family=family-1
      child=child+3

    adultneeded=0
    lessas=family*2
    calc=0
    if child>=3:
      calc=(adult+senior)-family*2-2
      if calc>=0:
        adultneeded=2 #two adults can be retained only if there are enough adults to reduce family*2 from adult+senior 
      else:
        adultneeded=1
    elif child>=1:
      adultneeded=1
    #reduce adults according to family number
    while(adult>adultneeded and lessas>0):
      adult=adult-1
      lessas=lessas-1
    #reduce seniors
    while lessas>0:
      senior=senior-1
      lessas=lessas-1
    #reducing adults and seniors as per total
    #considering 1 adult 2 children clause.
  group=0
  #Finding the groups - first look for number of groups out of children the seniors and finally adults alone.
  while child>6:
    group=group+1
    child=child-6

  adultneeded=0
    
  if child>=3:
    adultneeded=2
  elif child>=1:
    adultneeded=1

  while (adult-adultneeded)>=6:
    group=group+1
    adult=adult-6

  seniorneeded=0
  if child>0:
    if adult<adultneeded:
      seniorneeded=1
  while (senior-seniorneeded)>=6:
    senior=senior-6
    group=group+1  
  #to check if (adult+senior) is more than 6 after all above reductions, group will be increaed by 1 and adults and seniors reducted by 6.
  total=adult+senior-adultneeded
  if total>=6:
    total=6
    while((adult-adultneeded)>0 and total>=0):
      adult=adult-1
      total=total-1
    while(total>0):
      senior=senior-1
      total=total-1
    group=group+1

  if adult==0 and senior==0 and child>0:
    group=group+1
    child=0

  #Task-3: Calculation of the ticket cost
  #Case-1: Adult & Child combination

  if senior==0 and adult==0 and child>0:
    family=family+1
    child=0
  totalsc=0
  totalac=0
  #Case 1: Adult is 0
  if adult==0:
    totalsc=senior+child
    if totalsc>=6:
      family=family+1
      senior=senior-(6-child)
      child=0
    elif senior==1 and child==4:
      group=group+1
      senior=0
      child=0
    elif (senior==1 or senior==2) and (child>0 and child<=3):
      family=family+1
      senior=0
      child=0
  #case 2: When senior is 0
  elif senior==0:
    totalac=adult+child
    if (adult==2 and child==6):
        
      family=family+2
      adult=0
      child=0
    elif (adult==2 and child==5):
      child=0
      adult=1
      group=group+1
    elif totalac>6:
      print("\nTotal AC: ",totalac)
      adult=adult-(6-child)
      child=0
      family=family+1
    elif adult==1 and child==3:
      family=family+1
      adult=0
      child=0
    elif adult==1 and (child==5 or child==4):
      group=group+1
      adult=0
      child=0
  #Case three, he
  elif senior>0 and adult>0:
    totalas=senior+adult
    if child==0:
      if totalas>=6:
        senior=senior-(6-adult)
        adult=0
        group=group+1
    elif (totalas+child)==6:
      group=group+1
      child=0
      adult=0
      senior=0
    elif (totalas==2 and child==6):
      family=family+2
      child=0
      adult=0
      senior=0
    elif (adult+child+senior)>6:
      less=6
      while(less>0 and child>0):
        child=child-1
        less=less-1
      while(less>0 and adult>0):
        adult=adult-1
        less=less-1
      while(less>0 and senior>0):
        senior=senior-1
        less=less-1
      group=group+1
      child=0
      adult=0
  #printing of tickets
  totalcost=0
  ticketnumber=ticketnumber+1
  print("\n\n\nSummary of Ticket")
  print("===============================")
  print("\nTicket Number: ", ticketnumber)
  print("\n\nDate(s) Reserved ")
  for i in range(datechoice,(datechoice+noofdays)):
    nextdate=Begindatestring + timedelta(days=i)
    print(nextdate)
  print("Total days :",noofdays)
  print("\nAttractions: ")
  lfcost=0
  pfcost=0
  ebcost=0
  if lf>0:
    lfcost=extcost[0]*noofdays*lf
    totalcost=totalcost+lfcost
    print(extatt[0],lf,"\t$",lfcost)
  if pf>0:
    pfcost=extcost[1]*noofdays*pf
    totalcost=totalcost+pfcost
    print(extatt[1],pf,"\t$",pfcost)
  if eb>0:
    ebcost=extcost[2]*noofdays*eb
    totalcost=totalcost+ebcost
    print(extatt[2],eb,"\t$",ebcost)
  #print("\nGroups :",group,"\nFamily: ",family,"\nAdult: ",adult,"\nSenior: ",senior,"\nChild :",child)
  groupcost=0
  familycost=0
  adultcost=0
  seniorcost=0
  childcost=0
  if noofdays==1:
    if group>0:
      groupcost=group*costoneday[4]*6
      print("\nGroup Tickets: ", group,"\t\t\t$",groupcost)
      totalcost=totalcost+groupcost    
    if family>0:
      familycost=family*costoneday[3]
      print("\nFamily Tickets: ", family,"\t\t\t$",familycost)
      totalcost=totalcost+familycost   
    if adult>0:
      adultcost=adult*costoneday[0]
      print("\nAdult Tickets:  ", adult,"\t\t\t$",adultcost)
      totalcost=totalcost+adultcost   
    if senior>0:
      seniorcost=senior*costoneday[2]
      print("\nSenior Tickets: ", senior,"\t\t\t$",seniorcost)
      totalcost=totalcost+seniorcost   
    if child>0:
      childcost=child*costoneday[1]
      print("\nChildren Tickets: ", child,"\t\t\t$",childcost)
      totalcost=totalcost+childcost 
  elif noofdays==2:
    if group>0:
      groupcost=group*costtwoday[4]*6
      print("\nGroup Tickets: ", group,"\t\t\t$",groupcost)
      totalcost=totalcost+groupcost    
    if family>0:
      familycost=family*costtwoday[3]
      print("\nFamily Tickets: ", family,"\t\t\t$",familycost)
      totalcost=totalcost+familycost   
    if adult>0:
      adultcost=adult*costtwoday[0]
      print("\nAdult Tickets: ", adult,"\t\t\t$",adultcost)
      totalcost=totalcost+adultcost   
    if senior>0:
      seniorcost=senior*costtwoday[2]
      print("\nSenior Tickets: ", senior,"\t\t\t$",seniorcost)
      totalcost=totalcost+seniorcost   
    if child>0:
      childcost=child*costtwoday[1]
      print("\nChildren Tickets: ", child,"\t\t\t$",childcost)
      totalcost=totalcost+childcost 
  print("Total Cost :\t\t\t\t$",totalcost)
  
  repeat=int(input("\nWish to repeat? (1/0): "))
print("\nEnd of the program")
