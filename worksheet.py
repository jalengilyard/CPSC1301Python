# Jalen Gilyard
# 06 March 2018
# 

6 
value = input("Enter a value or 'q' to quit: ")

minimum = int(value)
maximum = int(value)
while value != "q":
    if int(value) > maximum:
        maximum = int(value)
    elif int(value) < minimum:
        minimum = int(value)
    value = input("Enter a value or 'q' to quit: ")

if value == 'q':
    print("Min: %d" % (minimum))
    print("Max: %d" % (maximum))

#7

user_value = int(input("Enter a number: "))

count = 0
positive = 0
negative = 0
num_sum = 0
avg = 0

while user_value != 0:
    count += 1
    
    if user_value > 0:
        positive += 1
    else:
        negative += 1

    num_sum += user_value
    user_value = int(input("Enter a number: "))
    
avg = num_sum / count
print("Count: %d" % (count))
print("Positive: %d"% (positive))
print("Negative: %d" % (negative))
print("Sum of all numbers: %d" % (num_sum))
print("Average: %s" % (avg))
