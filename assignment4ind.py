# Jalen Gilyard
# 8 April 2018
# Independent Assignment 4

def maximum(n1, n2, n3):
    largestNum = 0
    if n1 >= n2 and n1 >= n3:
        largestNum = n1
    elif n2 >= n1 and n2 >= n3:
        largestNum = n2
    elif n3 > n1 and n3 >= n2:
        largestNum = n3
    print("The maximium is: %d" % (largestNum))

def sumSmallest(n1, n2, n3):
    if n1 <= n2 and n2 <= n3:
        print("Smallest Sum was:", n1 + n2)
    elif n2 <= n1 and n3 <= n2:
        print("Smallest Sum:", n2 + n3)
    elif n3 <= n1 and n1 <= n2:
        print("Smallest Sum:", n3 + n1)

def printSorted(n1, n2, n3):
    if n1 <= n2 and n2 <= n3:
        print("Smallest to Largest: %d, %d, %d" % (n1, n2, n3))
    elif n2 <= n1 and n3 <= n1:
        print("Smallest to Largest: %d, %d, %d" % (n2, n3, n1))
    elif n3 <= n2 and n1 <= n2:
        print("Smallest to Largest: %d, %d, %d" % (n1, n3, n2))


def contains_word(sentence, word):
    split = sentence.split(word)
    joined = " ".join(split)

    if sentence == joined:
        print("False")
    if sentence != joined:
        print("True")

def replace_word(sentence, target, replacement):
    mystr = sentence.split()
    index = mystr.index(target)

    mystr[index] = replacement

    newString = " ".join(mystr)
    print(newString)

def reverse_sentence(sentence):
    mySent = sentence.split(" ")
    reversedSentence = ""

    for x in range(len(mySent) - 1, -1, -1):
        reversedSentence += mySent[x] + " "
    print(reversedSentence)
    

def main():
    maximum(2,4,6) # Part 1 #1
    sumSmallest(3, 6, 1) # Part 1 #2
    printSorted(-77, 6, -34) # Part 1 #3
    
    sentence = input("Enter a phrase: \n") 
    word = input("Enter a word: \n")
    contains_word(sentence, word) # Part 2 #1
    replace_word("This is a great sentence", "great", "good") # Part 2 #2
    reverse_sentence("I am happy to meet you!") # Part 2 #3
main()
