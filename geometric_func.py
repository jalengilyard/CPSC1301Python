# Jalen Gilyard
# 11 April 2018
#Function practice... geometric stuff 


import math

def sphereVolume(r):
    V = (4/3) * math.pi*(r**3)
    return V
def sphereSurface(r):
    A = 4 * math.pi * (r**2)
    return A
def cylinderVolume(r,h):
    V = math.pi * (r**2)* h
    return V
def cylinderSurface(r,h):
    A1 = 2 * math.pi * r * h
    A = A1 + (2 * math.pi * (r **2))
    return A
def coneVolume(r,h):
    Dia = h/3
    V = math.pi * (r**2) * Dia
    return V
def coneSurface(r,h):
    D_1 = (h**2) + (r**2)
    D = r + (math.sqrt(D_1))
    A = (math.pi * r) * D
    return A

#Main function
def main():

    radius = float(input("What is your radius?: "))
    height = float(input("What is the height?: "))

    print("Sphere Volume: ", sphereVolume(radius))
    print("Sphere Surface: ", sphereSurface(radius))
    print("Cylinder Volume: ", cylinderVolume(radius, height))
    print("Cylinder Surface: ", cylinderSurface(radius, height))
    print("Cone Volume: ", coneVolume(radius, height))
    print("Cone Surface: ", coneSurface(radius, height))
    
    (x) = math.pi
    print(f(x))
# main function call
main()
