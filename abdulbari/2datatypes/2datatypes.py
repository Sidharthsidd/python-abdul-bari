"""python datatypes 
Numeric types 
Variables 
Literals 
Conversions 


what is variables:
program contains the two things 
1.data
2.instructions 
age=15   =>age is the variable annd the 15 is the data 
in pyhton can store the value directly without assigning the declaration of datatype 
declarration and the initialization done symantaniouly 

"""

a=10 
print(a)
#can be declare multiple variables at onces 
name,price,weight='toothpaste',200,60
print(name,price,weight)

# one more method is to declase all at once
x=y=1 
print(x,y)

# How Python  is Dynamically Typed
# python programming is a dynamically typed you can directly write any data type example 
#   every value in the python is the object so int ,float and all are the classes 

# How to Know the Type of Any Variable
x=25
print(type(x))


# Rules for declaring Variable Names
# Name can contain alpha numeric characters and underscore 
# Name should not start with numeric ony stat with the letter or underscore 
# Reversed words/ keywords should ot be used like ,while ,for ,print 
# variables are case -sensitive  Rollno=17 and rollno =14 are diffrent 

# Numeric datatypes =>int ,float,bool,complex
# =>int :
a=125  
# there is no fixed size in the python 
x=1234567890987654321
print(x)
print(x.__sizeof__())  
# most dataytpes are immmutable i pytho jjust it target to the new value if you change the value 

# floating point value 
# image floating point 


# boolean datatypes 
# for the complex refer the image of complex.png
# can use only j for this comlex number  
x=3+5j
print(type(x))
a=1.22+3j
print(a.real)
print(a.imag)


# Literals or Constants   =>if the data is directly written from the inside program is called lirerals 
price=250 
# data =>
price=input("")
# examples of literals in diffrent datatypes 

b=1_2
print(b)
f=123_45.66
print(f)
# f=12_.34
print(f)
# f=123_
f=1_2.4_5
print(f)

c=5_4+1_2j
print(c)
# can mention in the single cote and double 
name='john'
print(name)
name="john"

# Continuation of Literals ( Decimal , Binary , Octal , Hexa)
# Discussion on int , float , complex
# the binary and other is not allowed for the float 

# A Glance on TypeCasting and User Input
a=10
a=0b1010
print("finding the value in binary ",a)
a=0o10
print("finding the value in octal ",a)
a=0xB
print(type(a))
print("finding the value in hexa",a)
print
# this cant be used for the imaginary part 
c=5+0b101
print(c)

# can be used for the real parts only ex=>
c=0o10+5j
print(c)



# base conversion 
# How Base Conversions Works by Using bin( )  oct( ) and hex( )
# all will return the string 
a=10
b=bin(a)
print(b)

c=oct(a)
print(c)

c=hex(a)
print(c)


"""How  One Data Type is Converted to Another Data Type  
Types of Type Conversion  :
1. Implicit    
2. Explicit

refer the pdf type conversion"""
