# Jalen Gilyard
# 29 March 2018
# Chapter 18.25

#### Many Functions
def equal(a,b):
    if a == b:
        return True
    else:
        return False

def middle(string):
    returnChar = ""
    if len(string) % 2 == 0:
        char1 = string[int(len(string) / 2 - 1)]
        char2 = string[int(len(string) / 2) ]
        returnChar = char1 + char2
    else:
        returnChar = string[int(len(string) / 2)]
    return returnChar
    
def repeat(string, n, delim):
    output = ""
    for x in range(0, n):
        if x != n-1:
            output += "%s%s " % (string, delim)
        else:
            output += string        
    return output
        




##### Main Functions
def main():
    print("Let's compare two strings to see if they are the same... (press enter after each)")
    input1 = input()
    input2 = input()
    print("Equal: " + str(equal(input1, input2)))

    print("Let's test out your middle string function. What would you like to find the middle of?")
    input3 = input()
    print("Middle character(s): " + middle(input3))

    print("Let's repeat some text now! Give me a string, number, and delimiter (Press enter after each)")
    input4 = input()
    input5 = int(input())
    input6 = input()

    print("Your result: " + str(repeat(input4, input5, input6)))

main()
