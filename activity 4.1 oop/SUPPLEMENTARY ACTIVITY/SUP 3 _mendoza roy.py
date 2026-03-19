import math

def quad_solve ( a,b,c ):
    d=b**2 - 4*a*c
    
    if d<=0:
        print("cannot be solved")
        return None
    else:
        x1 = (-b + math.sqrt(d))/ (2*a)
        x2 = (-b - math.sqrt(d))/ (2*a)
        return x1, x2
    
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

root1, root2 = quad_solve(a,b,c)
print("The Root 1 is: ", root1)
print("The Root 2 is: ", root2)