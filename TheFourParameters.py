## Jalen Gilyard
## 27 March 2017
## 18.24 Functions Are So Much Fun

########## Initial Variables
w = int(input("W-> "))
x = int(input("X-> "))
y = int(input("Y-> "))
z = int(input("Z-> "))

# Function average
def average(w, x, y, z):
    tot = w + x + y + z
    return tot/4

# function same
def alltheSame(w, x, y, z):
    if w == x and w == y and w == z and x == y and x == z:
        return True
    else:
        return False
# function diff
def allDifferent(w, x, y, z):
    if w != x and w != y and w != z and x != y and x != z:
        return True
    else:
        return False
# main function
def main():
    print("Average -> %.1f" % (average(w,x,y,z)))
    print("All the same -> %s" % (alltheSame(w,z,y,z)))
    print("All Different -> %s" % (allDifferent(w, x, y, z)))

# function main call
main()
