#quetion 1
import math
a = int(input("Enter the first coefficient,a :"))
b = int(input("Enter the second coefficient,b :"))
c = int(input("Enter the third coefficient,c :"))
d = b*b - 4*a*c


while(a!=0):
    if d<0:
        print("The equation has no real root.")
    elif d == 0:
        root = -b/(2*a);
        print("The equation has one root.")
        print("Root is :",root)
    else :
        root1 = -b+math.sqrt(d)/(2*a)
        root2 = -b-math.sqrt(d)/(2*a)
        print("The equation has two root.")
        print("Root 1 is:",root1)
        print("Root 2 is:",root2)
    break
