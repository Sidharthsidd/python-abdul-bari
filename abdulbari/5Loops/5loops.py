"""

    loops =>
    1.while and
    2.for 
    3.for each 

    while (condition):
        body

Rules for while loop 
    The condition must be updated within the loop, or it may become an infinite loop.
    If the condition is always True, the loop will never stop unless a break statement is used. 

"""


# Example of a while loop //counting the number to 10 

count=0
while  count<10:
    count=count+1
    print(count,"hello")


# print number as long as the number is 

n=int(input("Enter the numbers "))
while n>0:
    r=n%10
    n=n//10
    print(r)



# print the multiplication table 

number=int(input("enter the number"))
count=1
while count<10:
    count=count+1
    counter =number*count
    print(number,"x",count,"=",counter)



# Challenge 1 : Counting Number of Digits in a Number

number=int(input("Enter the numbers"))

count=0
while number >0:
    number=number//10
    count =count+1
print(count)


# Challenge 2 : To Find Sum of Digits in a Number
number=int(input("Enter the numbers"))
sum =0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r

print(sum)



# Challenge 3 : Reversing a Number
number =int(input())
rev=0
while number>0:
    r=number%10
    number=number//10
    rev=rev*10+r

    print(rev)




# Challenge 4 : To Check if Number is Palindrome or Not

number =int(input())

m=number
rev=0
while number>0:
    r=number%10
    number=number//10
    rev=rev*10+r
if m==rev:
    print("it is the palindrome")
else :
    print("it is not a palindrome")







# Challenge : Positive and Negative Numbers
# Challenge 1  :  To Find Sum of Given Number as Input
number = int(input())
n=abs(number)
sum=0
while n>0:
    r=n%10
    n=n//10
    sum=sum+r
print(sum)




# Challenge 2 :  To Find Sum of Positive and Negative Number
n_of_numbers=int(input())
po_sum=0 
ng_sum=0
count=0
while count<n_of_numbers:
    n=int(input("enter the number"))
    if n<0:
        ng_sum=ng_sum+n
        
    if n>0:
        po_sum=po_sum+n
    count+=1
print("The sum of positive numbers",po_sum)
print("Thhe sum of negative numbers",ng_sum)




# Challenge : Decimal to Binary
# Challenge 1 :  To Find Maximum  Number From the Given Numbers
n_of_numbers=int(input())
max=0 

count=0
while count<n_of_numbers:
    n=int(input("enter the number"))
    if n>max:
        max=n
    else:
        pass 
    count+=1
print("The max number is",max)



# Challenge 2 :  To Convert Decimal Number to Binary Number
decimal_number = int(input("Enter a decimal number: "))
binary_no=""
while decimal_number>0:
    r=decimal_number%2
    binary_no+=str(r)
    decimal_number=decimal_number//2
print("The decimal to binary number is",binary_no)


# Infinite Loop - break - continue - pass
# break statement
    # we can write the else condition in the while loop but it execute only when while condition is false 
    # else condition does not execute if break is given in the body same to the for loop also 


# continue statement
    #  to skip the condition and continnue to do the work 


# pass statement
    #  it is used when we want to do nothing in the code



# for loop 
# for in range(start,stop,step)
msg="hello world "
for x in msg:
    print(x, end=",")



# Challenge 1 : To Display Multiplication Table for a Given Number
n=int(input("Eneter the table number"))

mul=0

for i in range(1,10+1):
    mul=n*i
    print(n,"x",i,"=",mul)
    i+=1




# Challenge 2 : To Find the Factorial of a Given Number.
n=int(input("Eneter the fac number"))
fac=1
for i in range(1,n+1):
    fac=fac*i
    print("Factorial of",n,"is",fac)



# Challenge : AP and Fibonacci Series
# Challenge 1 : To Print n terms of AP series



a=int(input("Enter the initial number "))
d=int(input("Enter the diffrence number "))
n=int(input("Enter the n number "))
end=a+n*d

for i in range(1,end,d):
    print(i)




# Challenge 2 : To Print n terms of Fibonacci series
n=int(input("Enter the number"))
first =0
second =1
third=0
for i in range(0,n+1):
    if n==0 or n==1:
        print(i)
    else :
         print(first)
         third=first+second
         first=second
         second=third




# Challenge : Factors of a Number
# Challenge 1 :  To Find the Factors of a Number
n=int(input("Enter the number"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
    else:
        continue 





# Challenge 2 : To Check if a Number is Prime or Not
# Special Cases:
# 1 is NOT a prime number because it has only one divisor (itself).
# 0 is NOT a prime number because it has infinite divisors.


n=int(input("enter the number"))
count=0 
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)
if n==2:
    print("its a prime number")





#  Challenge : Prime Numbers from 1-100
for n in range(1,100+1):
    count=0
    for i in range(1,n+1):
        if n%i==0:  
            count +=1
    if count==2:
        print(n)


