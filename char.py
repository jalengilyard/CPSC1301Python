
char = int(input("Enter a character: "))

char_ans = chr(char)

if char >= 65 and char <= 90:
    print(char_ans)
elif char >= 65 and char <= 122:
    print(char_ans)
else:
    print("Not a capital letter")


