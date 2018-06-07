# Jalen Gilyard
# 15 February 2018
# Purpose: Assignment #1

import math

## Welcome and Start of Program
print("Welcome to the area calculator.")
print("Let's start by calculating the area of a sqare.")

## Variables for input of height and width
height = int(input("Enter the height of the rectangle:\n"))
width = int(input("Enter the width of the rectangle:\n"))
area = width * height

print("The area of the %d x %d rectangle is %d" % (width, height, area))

print("")

## Calculate the area of a circle
print("Let's now calculate the area of a circle.")
radius = float(input("Enter the radius of the circle:\n"))
area_circle = math.pi * math.pow(radius, 2)
print("The area of the circle is %.2f" % (area_circle))
