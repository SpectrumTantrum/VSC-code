highscore = [125,63,35,12]
print(highscore)
print(highscore[1])
print(highscore[3])
highscore[0] = 127
print(highscore[0])
highscore.append(8)
print(highscore)
del(highscore[2])
print(highscore)
print(len(highscore))
print(min(highscore))
print(max(highscore))

heroes = ["Batman", "Wonder Woman", "Superman", "Spiderman"]
print(heroes)
print("Current pilot: ", heroes[0])
print("Current co-pilot: ", heroes[1])
heroes[2] = ("Hit girl")
print(heroes)
heroes.append("Your Mom")
print(heroes)
heroes.append("Donald Trump")
print(heroes)

counter = 1
numbers = []
for counter in range(1,11):
    numbers.append(input("Please enter the "+str(counter)+ " number:"))
    
print(sum(int(numbers)))
