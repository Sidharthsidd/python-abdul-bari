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
"""

"""
# print the multiplication table 

number=int(input("enter the number"))
count=1
while count<10:
    count=count+1
    counter =number*count
    print(number,"x",count,"=",counter)
"""

"""
# Challenge 1 : Counting Number of Digits in a Number

number=int(input("Enter the numbers"))

count=0
while number >0:
    number=number//10
    count =count+1
print(count)
"""
"""
# Challenge 2 : To Find Sum of Digits in a Number
number=int(input("Enter the numbers"))
sum =0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r

print(sum)
"""

"""
# Challenge 3 : Reversing a Number
number =int(input())
rev=0
while number>0:
    r=number%10
    number=number//10
    rev=rev*10+r

    print(rev)

"""

"""
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


"""

# Challenge : Positive and Negative Numbers
# Challenge 1  :  To Find Sum of Given Number as Input





# Challenge 2 :  To Find Sum of Positive and Negative Number

