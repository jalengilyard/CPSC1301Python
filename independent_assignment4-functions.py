# Jalen Gilyard
# 17 April 2018
# Independent Assignment 4

import math
### Math functions
def triangleArea(base, height) :
    area = ((1/2) * base * height)
    return area
def rectangleArea(length, width):
    area = (length * width)
    return area

def circleArea(radius):
    area = (math.pi * (math.pow(radius, 2)))
    return area

### Main function 
def main():
    cont = True
    ## While loop to continue
    while cont != False:
        print("Welcome to the area calculator!")
        shape = input("Would you like the area of a triangle, rectangle, or circle (Enter t, r, c, or q to quit)? ")

        ### Conditional Statements 
        if shape == "t":
            base = int(input("Enter the base: "))
            height = int(input("Enter the height: "))
            print("The area is", triangleArea(base, height))
        elif shape == "r":
            length = int(input("Enter the length: "))
            height = int(input("Enter the height: "))
            print("The area is", rectangleArea(length, height))
        elif shape == "c":
            radius = float(input("Enter the radius: "))
            print("The area is %.2f" % (circleArea(radius)))
        elif shape == "q": 
            print("Have a nice day!")
            cont = False
main() ## Running the program 
