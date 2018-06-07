# Jalen Gilyard
# 26 February 2018
# Purpose: num 10

c =  int(input("Enter a number: "))
c_ans = chr(c)

if c >= 65 and c <= 90:
    print(c_ans)
elif c >= 97 and c <= 122:
    print(c_ans)
else:
    print("Not a letter")
