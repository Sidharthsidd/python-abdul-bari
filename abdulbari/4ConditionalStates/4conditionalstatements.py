#conditional statements 

# 1,Find  diffrence between 2 numbers 
a=int(input("enetrt he value a "))
b=int(input("enter the value b"))
c=a-b
if c>0:
    print(c)
else :
    print("invalid numbers ")




#check for age Eligible for casting a vote 
a=int(input("enter the age"))
if a>=18:
    print("you are eligible for casting a vote ")
else :
    print("you are not eligible for casting a vote ")



# Nested if else conditional 
john=float(input("enetr the age "))
smith=float(input("enetr the age "))
ajay=float(input("enetr the age "))

if john>ajay and john>smith:
    print("john is eldest")
elif smith>ajay:
    print("smith is eldest")
else :
    print('ajay is eldest')



amount=float(input("enter the bill amount"))
if amount<=1000:
    discount=(amount*10)/100
elif amount>1000 and amount<=5000:
    discount=(amount*20)/100
elif amount>5000 and amount<=10000:
    discount=(amount*30)/100
else :
    discount=(amount*50)/100
total=amount-discount
print(total)


# Printing a leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



