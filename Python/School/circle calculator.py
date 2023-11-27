#To accept Radius of circle for user
#calculate circumerence and area of circle

#INPUT A
radius = float(input("Give me the radius:"))

#Defining Pi
pi = float(3.14)

#Area = Pi * INPUT A ^ 2
area = float(pi * radius ** 2)

#Circumference = 2 * Pi * INPUT A
circumference = float(2 * pi * radius)

#Presenting Area
print("The area is", area)

#Presenting Circumference
print("The circumference is", circumference)
