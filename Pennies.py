# Jalen Gilyard
# 13 March 2018
# Paying with pennies

print("Welcome to the change maker!")

print("")

amount_due = int(input("Enter the amount due in pennies: \n"))
amount_recieved = int(input("Enter the amount recieved from the customer in pennies: \n"))

print("")

total_change = amount_recieved - amount_due

dollars = 0
quarters = 0
dimes = 0
nickels = 0 
pennies = 0

while total_change != 0:
    if (total_change -100) >= 0:
        dollars += 1
        total_change -= 100
    elif (total_change - 25) >= 0:
        quarters += 1
        total_change -= 25
    elif (total_change - 10) >= 0:
        dimes += 1
        total_change -= 10
    elif (total_change - 5) >= 0:
        nickels += 1
        total_change -= 5
    elif (total_change - 1) >= 0:
        pennies += 1
        total_change -= 1
        
print("Give the following change to the customer:")
print("%d dollars, %d quarters, %d dimes, %d nickels, and %d pennies." % (dollars, quarters, dimes, nickels, pennies)) 
