import tkinter as tk

def addition():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    answer = num1 + num2
    #Update text in labelAnswer
    labelAnswer.configure(text = "Answer: " + str(answer))

def subtraction():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    answer = num1 - num2
    #Update text in labelAnswer
    labelAnswer.configure(text = "Answer: " + str(answer))

def multipication():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    answer = num1 * num2
    #Update text in labelAnswer
    labelAnswer.configure(text = "Answer: " + str(answer))

def division():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    answer = num1 / num2
    #Update text in labelAnswer
    labelAnswer.configure(text = "Answer: " + str(answer))

def returnbig():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    if num1 > num2:
        labelAnswer.configure(text = "Answer: " + str(num1))
    else:
        labelAnswer.configure(text = "Answer: " + str(num2))

def vowelsinaword():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = str(num1)
    vowcount = 0
    for letter in num1:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
           vowcount = vowcount + 1
    labelAnswer.configure(text = "Answer: " + str(vowcount))
    
def amtofdiffletters():

    num1 = entry1.get()#Gets the text typed into entry box 1
    num1 = int(num1)
    num2 = entry2.get()#Gets the text typed into entry box 2
    num2 = int(num2)
    letters = []
    for letter in num1:
        
    
    
            
#Create an empty screen    
screen = tk.Tk()
screen.title("Calculator")

#Create a label
labelAnswer = tk.Label(screen, text= "Answer: ")
labelAnswer.pack()

#Create two text entry boxes
entry1 = tk.Entry (screen)
entry1.pack()
entry2 = tk.Entry (screen)
entry2.pack()

#Create a button
btnAddition = tk.Button(text=' Addition', command=addition)
btnAddition.pack()

btnSubtraction = tk.Button(text=' Subtraction', command=subtraction)
btnSubtraction.pack()

btnMultiplication = tk.Button(text=' Multiplication', command=multipication)
btnMultiplication.pack()

btnDivision = tk.Button(text=' Division', command=division)
btnDivision.pack()

btnReturnbig = tk.Button(text=' Returnbig', command=returnbig)
btnReturnbig.pack()

btnVowelsinaword = tk.Button(text=' Vowels in a word', command=vowelsinaword)
btnVowelsinaword.pack()



screen.mainloop()


#1. Largest of 2 numbers
#2. amt of vowels in word
#3. amt of diff letters in a word
#4. Month in the first box amount of days are displayed
