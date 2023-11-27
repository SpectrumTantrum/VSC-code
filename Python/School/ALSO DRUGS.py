print("How fast were they going?")
speed = int(input())

if (70 <= speed < 75):
    print("Issue Warning")
elif speed >= 75:
    print("Issue Fine")
else:
    print("No action")
