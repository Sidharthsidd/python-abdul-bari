"""

Ordered – Items are stored in a specific sequence and can be accessed using an index.
 Mutable – Elements can be changed, added, or removed.
 Allows Duplicates – A list can contain duplicate values.
 Heterogeneous – Can store different data types (e.g., integers, strings, floats, lists).
 Dynamic – The size of a list can grow or shrink dynamically.
"""
"""
# List : Indexing and Slicing
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[3:8]
print(list2)
list2=list1[::-1]
print(list2)
# this will print the number recerse bby step 2
list2=list1[-1:-11:-2]
print(list2)

# slicing can modify the content to  the lsit 
# modifing the same list
list1[0:3]=[30,40,50]
print(list1)

# List: Concatenation and in not in
# the  plus operator  returns the new list but the extend operator modify the exitisting list
list1=[1,2,3,4,5]
list2=[6,7,8,9]
listnew=list1+list2
print(listnew)
list1.extend(list2)
print(list1)

if 1 in  list1:
    print(True)
else :
    print(" false")

if 1 not in  list1:
    print(True)
else :
    print(" false")

# Visiting Elements in a List ( Iterations )
list1=[5,8,9,4,6,]
for i in range(len(list1)-1,-1,-1):
    print(list1[i] ,"for loop")

i=0
while (i<len(list1)):
    print(list1[i],"while loop")
    i+=1


# List Methods : Adding Elements
# append(x)
# extend(iterable)
# insert(i,x)
# copy


list1=[1,4]
n=int(input("Enetr the length"))
for i in range(n):
    num =int(input("Enter the number to append"))
    list1.append(num)
print(list1)


for i in range(n):
    num =int(input("Enter the number to append"))
    list1.extend(num)
print(list1)


for i in range(n):
    num =int(input("Enter the number to append"))
    list1.insert(len(list1),num)
print(list1)


for i in range(n):
    num =int(input("Enter the number to append"))
    list2=list1.copy(num)
print(list2)

"""

# List Methods : Removing Elements

# By default, .pop() removes the last element.
# You can also specify an index to remove a particular element.

# Removes a specific value (not index).
# If the value is not in the list, it raises an error.

# Deletes all items from the list but keeps the list itself.



# Comparison Table
# Method	 Removes By	              Returns Removed Value?	   Raises Error if Not Found?	                
# pop()	     Index (or last element)    Yes	                      Yes (if index is out of range)             
# remove()	 Value	                    No	                      Yes (if value is not in list)	
# clear()  	 All elements	            No	                            No	



l1=[5,1,2,3,4]
l1.pop()
print(l1)

# List Methods : Index & Sorting

l1 =[5,6,75,8,9,6,10,6]
l2=l1.index(6)
print(l2)


l2=l1.count(2)
print(l2)

l1.reverse()
print(l1)


# Nested List
l1=[3,5,7,9,3,4,5,3,7,8,9,]
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)

# Challenge : Concatenating List into Single Number

l2=''
for i in l1:
    l2+=str(i)
print(l2)


# Challenge : Minimum Index in Sum of Two Lists
  
l1=['pizza','nuggets','hotdog','noodles','pasta','burger']
l2=['burger','hotdog','noodles','pasta','nuggets','pizza']

index=10
index2=10
for i in range(len(l1)):
    indx=l2.index(l1[i])

    if i+indx<index+index2:
        index=i
        index2=indx

print(l1[index],index+index2)

# Challenge : Overlapping Elements in Two Lists

l1=[1,2,3,4,5,6,7]
l2=[4,5,6,7,8,9,10]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


# adding the two matrics 
l1=[[1,2,3,4],[5,6,7,8,9],[1,2,3,4]]
l2=[[1,2,3,4],[5,6,7,8,9],[1,2,3,4]]
l3=[]
for i in range(3):
    s=[]

    for j in range(4):
        s.append(l1[i][j]+l2[i][j])
    l3.append(s)
print(l3)


l2=[]
l1=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(4):
    s=[]
    for j in range(3):
        s.append(l1[j][i])
    l2.append(s)
print(l2)


