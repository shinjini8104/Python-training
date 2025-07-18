import math
import sys
print("1. CIRCLE")
print("2. SQUARE")
print("3. TRIANGLE")
print("4. RECTANGLE")
print("5. EXIT")

a=int(input("Enter your Choice:"))
if a==1:
    r = int(input("RADIUS = "))
    area = math.pi * r * r
    print("AREA OF CIRCLE =", area)
elif a==2:
    s = int(input("SIDE = "))
    area =  s*s
    print("AREA OF CIRCLE =", area)
elif a==3:
    base = int(input("BASE = "))
    height = int(input("HEIGHT = "))
    area = 0.5 * base * height
    print("AREA OF TRIANGLE =", area)
elif a == 4:
    length = int(input("LENGTH = "))
    breadth = int(input("BREADTH = "))
    area = length * breadth
    print("AREA OF RECTANGLE =", area)
elif a == 5:
    print("EXIT")

else:
    print("INVALID CHOICE")

    

