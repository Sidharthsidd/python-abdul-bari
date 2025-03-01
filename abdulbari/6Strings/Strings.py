# Strings have many built-in methods for modification, searching, and formatting.
# Strings are immutable, meaning they cannot be changed directly.
# A string in Python is a sequence of characters enclosed in single ('), double ("), or triple (''' or """) quotes. Python provides several built-in string methods to manipulate and process strings easily.


"""
# Methods : s.find , s.rfind , s.index , s.count
# find and index are the same but the find continues to find and if sub string is is there returns -1 
# s.find(sub[start,[end]])  start and end are the optional 
s="hello world"
r=s.find("o")   
print(r)

r=s.rfind("o")
print(r)

r=s.index("o")
print(r)

r=s.rindex("o")
print(r)


r=s.count("o")
print(r)
"""
"""

# String Methods : Removing Spaces
# Continuation Methods :
s='python'
r=s.ljust(10)
print(r)

r=s.rjust(10)
print(r)
r=s.center(10,"*")
print(r)
"""
"""
# removing from the string 
# strip is thee method to removing spacing or any chars  from the string 

s="python programming is fun"
r=s.lstrip("p")
print(r)

r=s.rstrip("p")
print(r)
"""



# String Methods : Changing Cases
# capatilize makes first letter capital 
s="hello dear"
r=s.capitalize()
print(r)


# s.lower makes all character to lower case 
s="hello dear"
r=s.lower()
print(r)


# upper makes all character to upper case 
s="hello dear"
r=s.upper()
print(r)

# swapcase thisc converts upper to to lower and lower case to upper 
s="hello dear"
r=s.swapcase()
print(r)


# to make every word first letter as capital 
s="hello dear"
r=s.title()
print(r)



# String Methods : Inquiry Methods 1
# 
s="Hello Dear"
r=s.isupper()
print(r)

# Use .lower() if you just need to change letters to lowercase.
text = "Helloß"
print(text.lower())  # Output: "helloß"


# Use .casefold() if you need to perform case-insensitive comparisons, especially when dealing with different languages.
text = "Helloß"
print(text.casefold())  # Output: "helloss"







# other methods 
# islower 
# istile
# isalnum
# isalpha
# ispace
# isacii
# isidentifier
# isprintable
# isdecimal
# isdigit
# isnumeric

# String Methods : Starts with and Ends with
# s.startwith(prefix,[start,[end]])
# s.endswith(prefix,[start[end]])
# s.removesuffix(suffix,/)     if any substring is present in the sentence it will remove it otherwise returns the originak string not modify the existing string 
# s.removeprefix(prefix,/)     removes the beginning of the string
# s.partition(sep)              it partition the string after and before of the string given and forms like a tuple 
# s.rpartition(sep)                partition from the right side 



# String Methods : Joining and Splitting
# s.replace(old,new,[count])

s="a-b-c-d"
r=s.replace("-",",")
print(r)

# s.join(iterable) takes the s2 character and concatenate with s1 all characters 
# the inside the braket should be iterable only it joins if it is single return the single char 

s2="abc"
s1="/"
r=s1.join(s2)
print(r)

# s.split([sep[,max split]])
# return the list splits if there is space 

s="hi hello world "
r=s.split()
# can be split by the comma or any other character 
print(r)

# s.rsplit([sep[,maxsplit]])
# s.splitlines([keepends]) like \n \f \c




# Challenge : Sorting Letters of a String
# returns the list 

ss="asgsagsgsg"
s=sorted(ss)
# to convert the list to the string 
str2="".join(s)
print(s)
print(str2)

""""
# Display the Data within 25 Letters in a given Format
product=input()
price=input()
total_len=len(product) +len(price)
print(total_len)
dots="."* (25-total_len)
print(f"{product} {dots} {price}")
"""

"""
# Challenge : Confirming Password
pass1=input()
pass2=input()
if pass1==pass2:
    print("Password Matched")
else :
    if pass1.casefold()==pass2.casefold():
        print("Password Matched")
    else:
        print("Password Not Matched")

"""

"""
# Challenge : Credit Card Details 
cardno=input()
lastdigit=cardno[15::]
dot ="*"*4+" "
carddigit=dot*3+lastdigit
print(carddigit)
"""

"""
# Challenge : Domain Name from Email
email=input()
domain=email.find("@")
domainname=email[domain+1:]
usename=email[:domain]
print(usename, "  ", domainname )
"""

"""
# Challenge : Converting String to Palindrome
palindrome=input()
rev=palindrome[::-1]
if palindrome==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#given string palindrome 
print(palindrome +rev)
"""
"""
date=input()
date1=date.split("/")
day=date1[0]
print(day,"day")
month=date1[1]
print(month,"month")
year=date1[2]
print(year,"year")


"""

"""
# Challenge : Anagram String
s1=input("enetert he first string")
s2=input("entert he second string")


if len(s1)==len(s2):
    print("Anagram")
else :
    for x in s1:
        if x in s2:
            print("the string si anagram")
        else :
            print("not anagram")

"""

"""
# Challenge : Rearranging Case
str1=input("enter the string ")
lower =''
upper =''
for x in str1:
    if x.islower():
        lower = lower + x
    else:
        upper = upper + x
"""

"""
# Challenge : Removing Punctuations
def remove_special_characters(s):
    return ''.join(char for char in s if char.isalnum() or char.isspace())

# Example usage
text = "Hello!@# How's $%your day?"
print(remove_special_characters(text))  # Output: "Hello Hows your day"
"""