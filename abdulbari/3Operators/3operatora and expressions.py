# Arithemetic operator refer the file Arithematic file for better undersstanding 

a=15
b=4
c=a+b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c=a%b
print(c)

# expressios precedence refer the image 

# examples of precedence of expressions =>

# area of a rectangle =>

"""
print("Options: \n1. Area of a Rectangle \n2. Triangle  \n3. Displacement ")
o = input("Enter the option: ")
result= (
    f"Area of tringle :{(lambda l,b:l*b )(int(input("enetet the value of length")),(int(input("eneter the breadth"))))}" if o=="1" 
    else 
    f"Area of Triangle :{(lambda b,h: 0.5*b*h) (int(input("enetr the value")),int(input("enetr the value of height ")))}" if o=="2" else 
    f"Area of displacement  :{(lambda v,u,a :(v**2-u**2)/(2*a))(int(input("enter the value of final velocity ")),int(input("enter the initial velocity ")),int(input("enter the value accelaration ")))}" if o=="3" else "invalid error "
    )

print(result)

"""
"""
# challenge 2=>Kms to Miles

k=int(input("enter the km value "))
result=f"km to miles{(lambda k:k*0.6)(k)}"
print(result)

# challenge to calculate the area of a cuboid 
result=(
    f"Area of cuboid :{(lambda l,b,h:2*((l*h)+(l*b)+(b*h)))(int(input("enter the value of l")),int(input("enter the value of b")),int(input("enter the value of h")))}"
)

print(result)
"""


"""
# Challenge to find Quadratic equations
# the value can be complex so the eneter the value b greter than 4ac


import math

def quadratic_root(a, b, c):
    if a == 0:
        return "Not a quadratic equation (a cannot be zero)."
    
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "Complex roots (negative discriminant)."
    
    root1 = (-b - math.sqrt(discriminant)) / (2 * a)
    root2 = (-b + math.sqrt(discriminant)) / (2 * a)

    return f"Quadratic equation roots: {root1}, {root2}"

try:
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    c = int(input("Enter the third number (c): "))

    result = quadratic_root(a, b, c)
    print(result)

except ValueError:
    print("Invalid input! Please enter integers only.")

"""
