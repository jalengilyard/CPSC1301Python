# Jalen Gilyard
# 8 March 2018
# Worksheet 2

avengers = ["Iron Man", "Captain America", "Thor", "Hulk", "Hawkeye", "Black Widow"]

prices = [1.75, 2.15, 3.50, 9.00]

desserts = ["brownies", "cookies", "pies"]
for treat in desserts:
    print(treat)

print("")
print("")

print(desserts[0])
print(desserts[1])
print(desserts[2])

print("")
print("")
counts = [43, 12, 5, 63, 34, 7]
for num in counts:
    print(num)

is_valid = [True, False]
for val in is_valid:
    print(val)

print("")
print("The avengers are: ")
for avenger in avengers:
    print(avenger)

print("")
print("")

for index in range(len(avengers)):
    print(avengers[index])

print("")
print("")

### Create a list called 'products'
products = ["keyboard", "mouse", "tower", "monitor"]
for product in range(1):
    print("The available products are... %s ... %s ... %s ... %s " % (products[0], products[1], products[2], products[3]))

print("")
print("")

print("The prices are: ")
prices = [10, 5, 250, 125]
for price in prices:
    print("$%d" % (price))


print("")
print("")

print("The available products are:")
bullet = 1
for product, price in zip(products, prices):
    print("%d. %s - $%d" % (bullet, product, price))
    bullet += 1 
