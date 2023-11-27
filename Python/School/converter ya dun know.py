#ask user for an amount in pounds
#give choice to convert to HKD or Chinese yuan
import sys

print("How many pounds do you have?")
pounds = float(input())

print("Your options are:")
print("1 for converting to HKD")
print("2 for converting to Chinese yuan")
print("0 to exit")

choice = input()

if choice == 1:
    print("The value in HKD is", pounds * 9.99)

elif choice == 2:
    print("The value in Chinese yuan is", pounds * 8.75)

elif choice == 0:
    sys.exit("Thank you for using this service")

else:
    print("Please enter 1, 2 or 0")

