# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
import re
#When you have imported the re module, you can start using regular expressions:
#Example
#Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x=re.search("^The.*Spain", txt)
if x:
    print("Yes, we have a match!")
else:
    print("No match")

#RegEx Functions
#The re module offers a set of functions that allows us to search a string for a match:
# findall() Function
# The findall() function returns a list containing all matches.
txt="The rain in Spain"
x=re.findall("ai", txt)
print(x)  # Output: ['ai', 'ai']

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

#Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#If no matches are found, the value None is returned:

txt = "The rain in Spain"
x = re.search("Portugal", txt)
if x:
    print("Yes, we have a match!")
else:
    print("No match")
# split() Function
# The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:
#Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#You can control the number of replacements by specifying the count parameter:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

