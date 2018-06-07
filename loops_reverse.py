##new stuff


def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print(reverse("Hello World!"))


string = 'abcde'
length = len(string)
string_rev = ""
while length>0:
   string_rev += string[length-1]
   length = length-1

print(string_rev)
