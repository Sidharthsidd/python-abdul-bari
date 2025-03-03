# Function is a piece of code which performs a task 
# It can take arguments and return values


def add3(a,b,c):
    result=a+b+c
    return result


r=add3(1,2,3)
print(r)

# default arguments
# default should be on right side 
# keyword be should be in right 
# defaults are created onlly once 
# where ever you the default it does not create new it continues to add the items 


def add3(item ,L=[]):
    L.append(item)
    return L
l1=[1,2,3,4]
print(add3(5,l1))
print(add3(6,l1))

print(add3(8))

# Variable Length Positional Arguments
# if want to write the function that can accept how much arguments you want to pass 
# it takes as a tuple 
def fun(*args):
    print(type(args),args)

fun()
fun(10)
fun(10,20,30,40)


# to pass the lsit to the positional arguments just set the * before the value 

def fun1(a,b,c,*args):
    print(a,b,c,args)
l1=[1,2,3,4,5,]
fun1(*l1)


# Generators
# yield functioin does not stops it holds the value and continues 
def days():
    l=['sun','mon','tue','wed','thu','fri','sat']
    i=0

    while True:
       x=l[i]
       i=(i+1)%7
       yield x
d=days()
print(next(d))
print(next(d))
print(next(d))  
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

# Global vs Local Variables
# a function cannot modify the global variables 
# it can be mofied by declaring the global under the function

g=10 
def fun():
    global g
    g=g+5
    print(g)
fun()
print(g)


def fun1():
    x,y,z=1,2,3
    print(locals())

fun1()
print(globals())

# recursive functiion 

def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)
r=fun(5)
print(r)

