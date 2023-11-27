print("What is your cars's fuel type?")
fueltype = input()

print("Is the engine size 2 liters or less")
print("or is it 2 liters more or more")
print("Please only type more or less")
enginesize = input()

print("What is the distance you are planning to travel in km")
distance = float(input())

co2 = 0

if fueltype == "Petrol" or "petrol" and enginesize == "less" or "2 liters or less":
    co2 = float(0.000208) * distance

elif fueltype == "Petrol" or "petrol" and enginesize == "more" or "2 liters or less":
    co2 = float(0.000296) * distance

elif fueltype == "Diesel" or "diesel" and enginesize == "less" or "2 liters or less":
    co2 = float(0.000176) * distance

elif fueltype == "Diesel" or "diesel" and enginesize == "less" or "2 liters or less":
    co2 = float(0.000236) * distance

else:
    print("Please restart the program, there was an error")

print("The tonnes of Co2 you will output is", co2)    
