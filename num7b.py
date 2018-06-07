# Jalen Gilyard
# 26 February 2018
# Purpose: to return the lowest number of 3 inputs

## Variables and Inputs
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
lowest_num = 0

## Conditional Statements
if num1 < num2:
    lowest_num = num1
elif num2 < num1:
    lowest_num = num2
elif num3 < num1:
    lowest_num = num3
elif num2 < num2:
    lowest_num: num2

print("Your lowest number is %d" % (lowest_num))
