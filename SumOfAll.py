# Jalen Gilyard
# 06 March 2018
# 18.19 
import math
# The sum of all even numbers between 2 and 100 (inclusive)
sum_total = 0 
for num in range(2, 101, 2):
    sum_total += num
print(sum_total)

# The sum of all squares between 1 and 100 (inclusive)
squares_total = 0
for s in range(1, 11):
    squares_total += math.pow(s, 2)
print(squares_total)

# All powers of 2 from 2^0 up to 2^20
sq_total = 0
for sq in range(0, 21):
    sq_total = 2 ** sq
    print(sq_total, end=" ")
odd_total = 0

# The sum of all odd numbers between a and b (inclusive), where a and b are inputs
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
for odd in range(a, b + 1):
    if odd % 2 != 0:
        odd_total += odd
print(odd_total)

# The sum of all odd digits of an input
odd_input = input("Enter a number: ")
tot = 0 
for o in odd_input:
    if int(o) % 2 != 0:
        tot += int(o)
print(tot)
