#see if user is elligible to vote
#over 18 is elligible
#under 18 is not
#represent the results

print("What is your age?")
age = int(input())

if age >= 18:
    print("Elligible to vote.")

else:
    print("Not elligible to vote.")
