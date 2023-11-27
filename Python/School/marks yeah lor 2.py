#ask user to input marks
#analyze marks to give just conclusion

print("What are your marks?")
marks = int(input())

if marks >= 80:
    print("Congrats you got a Distinction!")

elif marks >= 60:
    print("Congrats you got a Merit!")

elif marks >= 40:
    print("Congrats you Passed!")

else:
    print("Unfortunately you failed!")
