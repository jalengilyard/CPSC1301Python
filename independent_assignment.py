# Jalen Gilyard
# 15 March 2018
# Independent Programming Assignment 2: Palidrome Checker

cont = False
while cont != True:
    word = input("Enter a word: ")
    wordReverse = ""
    
    for v in range(len(word) - 1, -1, -1):
        wordReverse += word[v]

    if word == wordReverse:
        print("%s is a palidrome" % (word))
    else:
        print("%s is not a palidrome" % (word))

    keep_going = input("Do you want to continue?: ")
    if keep_going == "yes" or keep_going == "Yes":
        cont = False
    else :
        cont = True

