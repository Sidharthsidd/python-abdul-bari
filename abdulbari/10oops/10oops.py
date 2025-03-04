"""
 Object-Oriented Programming (OOP) is a paradigm based on the concept of objects, which contain data and methods to operate on that data. Four main principles of OOP are:
1. Abstraction 🏛️
Definition: Abstraction is the process of hiding unnecessary details and only exposing essential features of an object.

Example:
When you drive a car, you use the steering wheel, accelerator, and brakes, but you don’t need to know how the engine works internally.
In programming, you can achieve abstraction using abstract classes and interfaces.

2. Inheritance 🏡
Definition: Inheritance allows one class to inherit properties and behavior from another class (parent-child relationship).

Example:
A Dog is an Animal. So, instead of defining "breathing" for every animal, the Dog class can inherit it from the Animal class.

3. Encapsulation 🔒
Definition: Encapsulation is data hiding by restricting direct access to some of an object’s components and only allowing controlled access through methods.

Example:
Your bank account balance is private, but you can access it via methods like deposit() or withdraw().

4. Polymorphism 🎭
Definition: Polymorphism allows the same method name to have different behaviors based on the object calling it.

Types of Polymorphism:
Method Overriding (Runtime Polymorphism) – When a child class provides a specific implementation of a method defined in the parent class.
Method Overloading (Compile-time Polymorphism) – When multiple methods have the same name but different parameters.
"""

class cuboid:
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h

    def area(self):
        return self.length*self.breadth
    def vollume(self):
        return self.length*self.breadth*self.height



c1=cuboid(3,4,5)
print(c1.area())

c2=cuboid(20,10,5)
print(c2.vollume())


# Self and Constructor
# if init is not declased it create a default constructor 

# Instance Variable and Method
# variables                  methods
# instance variables           instacne methods 
# static /class variables          static methods  




# what is instance
# any thing writing first in the init is the instance 

class test :
    def __init__(s):
        s.a=10
    def fun(s):
        s.b=20
t1=test()
# whenever you call the function the instance is created
t1.fun()
t1.c=30
print(dir(t1))


# Static Methods
class test :
    def __init__(s):
        s.a=10

    def fun(s):
        s.b=20
    @staticmethod
    def fun1(a,b):
        return a==b


print(test.fun1(10,10))


# accessors and mutators means these are the readig and writing of a object 
# accessors are reading the reading a class of an object 
# mutators are writing the class of an object

class rectangle :
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def getlength(self):
        return self.length
    def setlength(self,l):
        self.length=l
    def fun1(self):
        return self.length*self.breadth

r1=rectangle(10,5)
print(r1.getlength())
print(r1.fun1())
r1.setlength(10)
print(r1.getlength())


# Introduction to Inheritance
class cuboid(rectangle,test):
    def __init__(self,h,l,b,a):
        self.height=h
        super().__init__(l,b)
    def volume(self):
        return self.length*self.length*self.height
    def fun1(self):
        return self.a

r1=cuboid(2,3,3,4)
print(r1.volume())

# call the parent costructor by the via super function
# Inheritance is a process where one class can inherit the properties of another class
# Inner class 
# createing the class inside the class 

class customer:
    def __init__(self,name,age,bno,bstreet,bcity,bcountry,dno,dstreet,dcity,dcountry):
        self.name=name
        self.age=age
        self.baddr=self.address(bno,bstreet,bcity,bcountry)
        self.sadr=self.address(dno,dstreet,dcity,dcountry)

    class address:
        def __init__(self,dno,street,city,country):
            self.dno=dno
            self.street=street
            self.city=city
            self.country=country

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)


r1=customer(1,2,3,4,5,6,7,8,9,1)
r1.baddr.display()
r1.sadr.display()


# Method overloading 
# Method overloading is a feature that allows method with same name but different parameters to be defined in

class Arith:
    def sum(self,a,b,c=None):
        s=a+b
        if c is  None:
            return s
        else :
            return s+c
# same methood can be pass 3 arguments and two arguments also     

a=Arith()
print(a.sum(10,5))
print(a.sum("helleo","world"))
print(a.sum(1,2,3))



