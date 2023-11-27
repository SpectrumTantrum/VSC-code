#code program that give you vowels in word


def vowinword():
    
    word = input("write a word here bruh:")
    
    vowrep = []

    vowcount = 0

    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowcount = vowcount + 1
            if letter == "a":
                vowrep.append(" a,")
            elif letter == "e":
                vowrep.append(" e,")
            elif letter == "i":
                vowrep.append(" i,")
            elif letter == "o":
                vowrep.append(" o,")
            else:
                vowrep.append(" u,")


    print(word,"has", vowcount,"vowels")
    print("The word has the following vowels", vowrep)

vowinword()
