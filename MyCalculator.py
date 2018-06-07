# Jalen Gilyard
# 15 February 2018
# Independent Lab Test: Simple Calculator from Dollar General

## Create Variables for user input
first_num = float(input("Enter the first number: \n"))
operand = input("Enter an operand (+, -, /, *): \n")
second_num = float(input("Enter the second number: \n"))
total = 0

## Operation Conditional Statements
if operand == "/" and second_num == 0:
    print("Can not divide by 0")
elif operand == "+":
    total = first_num + second_num
elif operand == "-":
    total = first_num - second_num
elif operand == "*":
    total = first_num * second_num
elif operand == "/":
    total = first_num / second_num

## Output to the user
print("%d %s %d = %.2f" % (first_num, operand, second_num, total))
