# Jalen Gilyard
# 15 February 2018
# Purpose: Speeding Calculator

import turtle

print("Welcome to the speed fine calculator!")
print("")
speed_limit = int(input("Enter the speed limit:\n"))
speed = int(input("Enter the clocked speed:\n"))
base_fine = 50
over_speed = (speed - speed_limit) * 5
speeder = 90
total = 0 

wn = turtle.Screen()
samson = turtle.Turtle()

def draw_little_square():
    samson.forward(50)
    samson.right(90)
    samson.forward(50)
    samson.right(90)
    samson.forward(50)
    samson.right(90)
    samson.forward(50)

def draw_big_square():
    samson.forward(200)
    samson.right(90)
    samson.forward(200)
    samson.right(90)
    samson.forward(200)
    samson.right(90)
    samson.forward(200)

def print_ticket():
    samson.pu()
    samson.goto(80, -25)
    samson.write("The speed limit is %d\n" % (speed_limit))
    samson.goto(80, -35)
    samson.write("Your clocked speed was %d\n" % (speed))
    samson.goto(80, -45)
    samson.write("Your fine is $%d" % (total))
    
if speed > 90:
    total += base_fine + speeder + over_speed
    draw_big_square()
    print_ticket()
    print("Fine: $%d" % (total))

elif speed > speed_limit:
    total += base_fine + over_speed
    draw_big_square()
    print_ticket()
    print("Fine: $%d" % (total))

else:
    total += 0
    draw_little_square()
    print("No fine for legal speeds.")
