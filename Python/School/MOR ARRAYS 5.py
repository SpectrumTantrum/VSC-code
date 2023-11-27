reverse = []

word = input("enter a word:")
for count in range(len(word)-1,-1,-1):
    reverse.append(word[count])

word = ""
for letter in reverse:
    word = word + letter

print(word)
