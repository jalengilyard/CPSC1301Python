
num1 = int(input("Number 1: "))
num2 = int(input("Number 2:" ))
num3 = int(input("Number 3:"))
lowest_num = 0
if num1 < num2:
    lowest_num = num1

elif num2 < num1:
    lowest_num = num2

elif num3 < num1:
    lowest_num = num3

elif num1 < num3:
    lowest_num = num1
    
elif num2 < num3:
    lowest_num = num2
print(lowest_num)
