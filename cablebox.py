# Jalen Gilyard
# 15 March 2018
# Assignment 3

##### Prompt 1

number = input("Enter a phone number: ")
new_num = ""
if len(number) == 10:
    for num in number:
        new_num += num
    print("(%s%s%s)-%s%s%s-%s%s%s%s" % (new_num[0], new_num[1], new_num[2],
                                         new_num[3], new_num[4], new_num[5], new_num[6],
                                         new_num[7], new_num[8], new_num[9]) )
else:
    print("Not a valid 10 digit phone number")

##### Prompt 2

### Set up default values. 
power = False
channel = 3
volume = 5
mute = "OFF"

### List named tv that holds all the tv program information and descriptions.
tv = [
    ["The Maury Show", "Veteran TV journalist Maury Povich -- yes, he began his TV career as a news anchor -- tackles volatile issues with his guests and studio audience on this daily, hourlong talk show.Known widely for offering guests the chance to take DNA tests to prove or disprove paternity -- usually with guests breaking out in tears of joy or sorrow -- Povich's show also frequently utilizes lie-detector tests. Cheaters and out-of-control teens are often featured on the show, and episodes occasionally focus on outrageous moments that have been captured on video."],
    ["The View", "Created in 1997 by veteran journalist Barbara Walters, 'The View' is a daytime talk show hosted by women -- including Whoopi Goldberg, Joy Behar, Paula Faris and Sara Haines -- and each offers her take on the day's news during the opening 'Hot Topics' segment. Later, the ladies welcome various celebrities, who join them in a chat or perform for the audience. The program also offers tips on beauty, fashion, diet and relationships. Known for their freewheeling style, the hosts are often lampooned in late-night sketches."],
    ["Saturday Night Live", "After being on the air for more than three decades, the essential format of this show hasn't changed: Get an A-list guest host (or reasonable facsimile) and throw him or her into sketches with the ensemble players, which have included such heavy hitters as Will Ferrell, Jimmy Fallon, Tina Fey, Amy Poehler, Kristen Wiig, Jane Curtin, John Belushi, Chris Rock, Eddie Murphy, Chevy Chase, Bill Murray and Mike Myers. Each week's show also offers two musical numbers from someone at, or aspiring to reach, the top of the charts."],
    ["The Wendy Williams Show", "Radio host and author Wendy Williams joins the daytime syndicated talk-show field, bringing her distinctive personality to television. In addition to celebrity interviews, regular segments include Hot Topics, which usually opens the show and features Williams giving her honest, opinionated and often-unpredictable take on the latest pop-culture and entertainment headlines, and Ask Wendy, in which she offers advice to audience members seeking solutions to their problems. The daily, hourlong program is broadcast from a studio in New York City."],
    ["Power Rangers Mystic Force", "Legend says when the darkness arises, five brave teen sorcerers will be called to fight for the planet's survival - with the guidance from their wise mentor and the ancient Xenotome, book of the unknown. They will embark on magical adventures, befriend mystical dragons, battle dangerous beasts, encounter pure evil... and transform into the Power Rangers Mystic Force."]
    ]

### Function created to display the program guide.
def guide():
    print("           Guide           ")
    print(" Channel         Program           ")
    print("     1.            %s" % (tv[0][0]))
    print("     2.            %s" % (tv[1][0]))
    print("     3.            %s" % (tv[2][0]))
    print("     4.            %s" % (tv[3][0]))
    print("     5.            %s" % (tv[4][0]))

### Prints out the available commands 
def commands():
    print("Commands Available:")
    print("Channels: 1, 2, 3, 4, or 5")
    print("Enter C+ or c+ to flip to the next channel.")
    print("Enter C- or c- to flip back to the last channel.")
    print("Enter V+ or v+ to turn up the volume a bit.")
    print("Enter V- or v- to turn down the volume a bit.")
    print("Enter M or m to mute the volume and V+ to unmute it.")
    print("Enter G or g to print the program guide.")
    print("Enter X or x to turn off the TV.")
    print()

    
## Beginning of power button 
remote = input("Press 'P' or 'p' to power on: \n")

### if statement to turn the power on.
if remote == "P" or remote == "p":
    power = True
    print("Powering ON...Hello WORLD AND ALL WHO INHABIT IT :o")

### Beginning of the remote app. print() statements added for format 
while power != False:
    if volume > 0:
        mute = "OFF"
    else:
        mute = "ON"

    
    print()
    print("Power ON")
    print("Channel: %d" % (channel))
    print("Volume: %d" % (volume))
    print("Mute: %s" % (mute))

    print()
    commands()
    
    print("Now Showing: ")
    print("Program: %s" % (tv[channel - 1][0]))
    print("Description: %s" % (tv[channel - 1][1]))
    
    remote = input("Please enter a command or 'X' or 'x' to power off: \n")
    
    
    if remote == "X" or remote == "x":
        print("Powering OFF... Goodbye Cruel World -~-")
        power = False
    elif remote == "1" or remote == "2" or remote == "3" or remote == "4" or remote == "5":
        channel = int(remote)
    elif remote == "C+" or remote == "c+":
        channel += 1
    elif remote == "C-" or remote == "c-":
        channel -= 1
    elif remote == "V+" or remote == "v+":
        volume += 1
    elif remote == "V-" or remote == "v-":
        volume -= 1
    elif remote == "M" or remote == "m":
        mute = "ON"
        volume = 0
    elif remote == "G" or remote == "g":
        guide()
    elif channel > 5:
        print("Not a reachable channel")
        channel = 3
    else:
        print("Please enter a valid selection please.")

    
    print()


    
    










    
