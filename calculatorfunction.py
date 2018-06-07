# Jalen Gilyard
# 10 April 2018
# Independent Lab

import math

## Basic Functions
def add(a,b):
    return a + b


def subtract(a,b):
    return a - b


def multiply(a,b):
    return a * b


def divide(a,b):
    return (a/b)

def exponent(a, b):
    return math.pow(a, b)

def sqrt(a):
    return math.sqrt(a)

## Menu Function
def menu():
    print("Options...")
    print("M - Multiply")
    print("D - Divide")
    print("A - Add")
    print("S - Subtract")
    print("E - Exponent")
    print("SQ - Square Root")
    print("Q - Quit")


## Main Driver Function
def main():
    cont = ""
    while cont != "N": ## to continue taking operations until a No is given
        menu() ## Prints menu
        selection = input("Which command would you like to execute?: ").lower() ## User Selection
        if selection != "q":
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number, if square root just type 0: "))

        if n2 == 0:
            print("Error Divide by Zero")
        ## Selection Statements for Operations 
        if selection == "m":
            print("Operation %d * %d = %d" % (n1, n2, multiply(n1,n2)))
        elif selection == "d":
            print("Operation %d / %d = %d" % (n1, n2, divide(n1,n2)))
        elif selection == "a":
            print("Operation %d + %d = %d" % (n1, n2, add(n1,n2)))
        elif selection == "s":
            print("Operation %d - %d = %d" % (n1, n2, subtract(n1,n2)))
        elif selection == "e":
            print("Operation %d raised to the %d power is %d" % (n1, n2, exponent(n1, n2)))
        elif selection == "sq":
            print("Operation, the square root of %d is %d" % (n1, sqrt(n1)))
        elif selection == "q":
            cont = "N"
        else:
            print("Invalid Selection")
        
main()
