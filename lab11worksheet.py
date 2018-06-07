# Jalen Gilyard
# 8 March 2018
# Lab 11 Worksheet

## Part 1 Number 1
print("Part 1 Number 1:")
numbers = [15, 19, 47, 90, 75, 32, 129, 105, 55, 38, 2, 1, 94, 62, 81, 67, 166, 29, 121, 115, 89,
           14, 28, 16, 114, 58, 13, 74, 24, 72, 36, 25, 111, 150, 20, 83, 132, 97, 168, 145, 51,
           169, 27, 65, 6, 80, 112, 61, 33, 69, 167, 134, 159, 40, 85, 149, 71, 135, 34, 141, 161,
           103, 84, 93, 45, 86, 21, 73, 37, 106, 50, 126, 99, 138, 124, 2, 101, 17, 136, 89, 59, 133,
           41, 141, 66, 73, 4, 19, 9, 28, 171, 120, 105, 79, 63, 42, 113, 127, 11, 61, 157, 83, 98, 71,
           77, 78, 144, 30, 68, 137, 95, 159, 143, 146, 6, 57, 8, 136, 168, 1, 142, 67, 2, 47, 91, 101, 134,
           23, 79, 48, 114, 154, 111, 50, 172, 35, 55, 38, 135, 158, 170, 107, 115, 58, 45, 3, 174, 139, 34,
           97, 94, 160, 26, 74, 127]

max_value = numbers[0]
min_value = numbers[0]
num_sum = 0
num_avg = 0

for num in numbers:
    if num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num
    num_sum += num
    num_avg = num_sum / len(numbers)

print("The max value is %d" % (max_value))
print("The min value is %d" % (min_value))
print("The sum of all numbers is %d" % (num_sum))
print("The average is %d" % (num_avg))


## Part 1 Number 1
print("Part 2 Number 1:")
menu = ["coffee", "tea", "coke", "latte", "water"]
prices = [1.50, 1.00, 1.75, 4.25, 1.25]

print()

print("The menu is:")
bullet = 1
for item in range(len(menu)):
    print("%d. %s - $%.2f" % (bullet, menu[item], prices[item]))
    bullet += 1


print()


## Part 2 Number 2
print("Part 2 Number 2")

item = int(input("Which item would you like?: \n"))
quantity = int(input("How many would you like?: \n"))

choice = 0
if item == 1:
    choice = 0
elif item == 2:
    choice = 1
elif item == 3:
    choice = 2
elif item == 4:
    choice = 3
elif item == 5:
    choice = 4

subtotal = prices[choice] * quantity
tax = subtotal * 0.08
        ## Provide Reciept
print("Reciept")
print("Item: %s - $%.2f x %d" % (menu[choice], prices[choice], quantity ) )
print("Subtotal = $%.2f" % (subtotal) )
print("Total = $%.2f" % (subtotal + tax) )
