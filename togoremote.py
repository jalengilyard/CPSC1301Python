## name
## Date
## Assignment

# Prompt 1
number =  input("Enter the phone number: ")
formatted = ""

for num in number:
    formatted += num
print("(%s%s%s)-%s%s%s-%s%s%s%s" % (formatted[0], formatted[1], formatted[2], formatted[3], formatted[4], formatted[5], formatted[6], formatted[7], formatted[8], formatted[9]) )


# Prompt 2
power = False
channel = 3
volume = 5
mute = "off"

controller = input("Press 'P' or 'p' to turn on: \n")

if controller == "P" or controller == "p":
    power = True

while power != False:
    print()
    print("Power ON")
    print("Channel: ", channel)
    print("Volume: ", volume)
    print("Mute: ", mute)

    print("Commands: ")
    print("Channel Jump to: 1, 2, 3, 4, or 5")
    print("Enter C+ or c+ for next channel.")
    print("Enter C- or c- for the last channel.")
    print("Enter V+ or v+ to turn up the volume.")
    print("Enter V- or v- to turn down the volume.")
    print("Enter M or m to mute the volume.")
    print("Enter X or x to power off")

    controller = input("Enter a command or 'X' or 'x' to power off")

    
    if controller == "X" or controller == "x":
        power = False
    elif controller == "1" or controller == "2" or controller == "3" or controller == "4" or controller == "5":
        channel = int(controller)
    elif controller == "C+" or controller == "c+":
        channel += 1
    elif controller == "C-" or controller == "c-":
        channel -= 1
    elif controller == "V+" or controller == "v+":
        volume += 1
    elif controller == "V-" or controller == "v-":
        volume -= 1
    elif controller == "M" or controller == "m":
        mute = "ON"
    else:
        print("Please enter a valid command.")

