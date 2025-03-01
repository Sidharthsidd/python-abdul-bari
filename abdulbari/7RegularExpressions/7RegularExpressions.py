"""Difference Between match() and search()
Function	Checks the whole string?	Must start at the beginning?
re.match()	 No	                                           Yes
re.search()	 Yes	                                      No



 re.match() only matches from the beginning of the string.
If the pattern is found at the start, it returns a match object; otherwise, it returns None.
Use .group(), .start(), .end(), and .span() to extract match details.
Use re.IGNORECASE for case-insensitive matching.
If you want to search anywhere in the string, use re.search() instead.
"""

# + 1 or more repetition 
#  * 0 or more repetition 
#   ? 0 or 1 repetation
#  exactly  m occurance 
# from m to n ,m defaults to 0 ,n to infinity


# Refer the image Quantifiers
import re

str1=re.match("hello","hello the skajd").group()
print(str1)

str1=re.match("[abc]+","acacabab")
print(str1.group())

# Special Characters
# refer the image the special characters 
# matchs the expect that charcters 
stt2=re.match("[^abcdfe]+","safdsfsdf")     
print(stt2.group())

# this matches every thing in the string  except the new line 
stt2=re.match("[*]+","safdsfsdf")     
print(stt2.group()) 

# refer thee image sequence character for the next topic
# this matches the sequence of characters
# this is used to match the sequence of characters

