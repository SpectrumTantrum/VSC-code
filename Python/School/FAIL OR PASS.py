#To ask user for mark
#Depending on mark, present Fail or pass
#50 minimum for pass
#fail fo less than 50

#OUTPUT
print("What is your mark?")

#Score <- USERINPUT
Score = float(input())

#IF Score >= 50.0 THEN OUTPUT Congrats you passed the test.
if Score >= 50.0:

    print("Congrats you passed the test.")

#ELSE OUTPUT Unfortunately you failed the test.
else:

    print("Unfortunately you failed the test.")

#ENDIF
