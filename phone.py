# Jalen Gilyard
# 18 March 2018
# Cell phone project: independent

power = False
provider = "AT&T"
data = "LTE"
battery = 100


contacts = {}

def new_contact():
    contact = input("Name: ")
    number = input("Phone: ")

    contacts[contact] = number

def contacts():
    
selection = input("Enter P or p to power on: \n")

if selection == "P" or selection == "p":
    power = True

while power != False:
    print("Power ON")

    selection = input("What would you like to do? Enter X or x to power off: \n")
    
    if selection == "X" or selection == "x":
        power = False
    ##elif 
