# Jalen Gilyard
# 22 February 2018
# Purpose: 6 Digit Char

phrase = input("Enter a 6 digit phrase, please. \n")

if len(phrase) == 6:
    print(phrase[0])
    print(phrase[len(phrase) - 1])
else:
    print("Wrong length")
          
