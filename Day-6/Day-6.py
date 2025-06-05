import mymodule as mx
# mymodule.greeting("Nirbhay")
# mymodule.greeting("Satya")
# mymodule.greeting("Satyam")
# # # # The module name is the filename without the .py extension.

# a= mymodule.person1["age"]
# b= mymodule.person1["name"]

# print(a)
# print(b)

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Example
# Import and use the platform module:

import platform

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
x = dir(platform)
print(x)

#################################################### Dates Module ################################################
# A date in Python is not a data type of its own, but we can import a module named datetime to work
# with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))  # Prints the current day of the week
print(x.strftime("%B")) 
print(x.strftime("%a"))  # Prints the abbreviated weekday name
print(x.strftime("%b"))  # Prints the abbreviated month name
print(x.strftime("%d"))  # Prints the day of the month
print(x.strftime("%H"))  # Prints the hour (24-hour clock)
print(x.strftime("%M"))  # Prints the minute
print(x.strftime("%S"))  # Prints the second
print(x.strftime("%y"))  # Prints the year without century
print(x.strftime("%Y"))  # Prints the year with century
print(x.strftime("%p"))  # Prints AM or PM
print(x.strftime("%I"))  # Prints the hour (12-hour clock)
print(x.strftime("%j"))  # Prints the day of the year
print(x.strftime("%W"))  # Prints the week number of the year (Monday as the first day of the week)
print(x.strftime("%x"))  # Prints the date in a locale-specific format
print(x.strftime("%X"))  # Prints the time in a locale-specific format
print(x.strftime("%c"))  # Prints the date and time in a locale-specific format

#################################################### Math function ################################################
# Python has a set of built-in math functions, including an extensive math module, that allows you to
# perform mathematical tasks on numbers.
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)

print(x)

#The pow(x, y) function returns the value of x to the power of y (xy).
# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)
print(x)
################################################## Math Module ################################################
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

import math
# When you have imported the math module, you can start using methods and constants of the module.
# The math.sqrt() method for example, returns the square root of a number:
x=math.sqrt(64)
print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() 
# method rounds a number downwards to its nearest integer, and returns the result:
x=math.ceil(1.4)
y=math.floor(1.4)
# print(x)
# print(y)

#################################################### Random Module ################################################
#Python has a built-in module that you can use to make random numbers.
import random
#1. random.random()
print(random.random())  # Returns a random float number between 0.0 and 1.0
#2. random.randint(a, b)
print(random.randint(1, 10))    # Returns a random number between 1 and 10 (both included)
#3. random.choice(sequence)
names=["Nirbhay", "Satya", "Satyam","Aniket","Ramu","Radhe","Radha","Subhay","Deepu","Priya"]
print(random.choice(names))
#4. random.choices(sequence, k=n)
print(random.choices(names, k=5)) # Give Multiple random choices (duplicates allowed)

#5. random.sample(sequence, k=n) 
print(random.sample(names, k=2))  # e.g., ['Aman', 'Shreya']
## Give Multiple random choices (duplicates not allowed)

 #6. random.shuffle(list)
# The shuffle() method takes a list as an argument and shuffles the elements of the list in place.
print(random.shuffle(names))  # Shuffles the names list in place

#7. random.uniform(a, b)
#a aur b ke beech koi bhi float number deta hai
print(random.uniform(1, 10))  # Returns a random float number between 1 and 10




# #The randrange() method returns a randomly selected element from the specified range.
# print(random.randrange(1, 10))  # Returns a random number between 1 and 9

# numbers=[2,4,5,86,4,2,67,53,21,1.1,1.2,5.3]
# print(random.choice(numbers))  # Returns a random element from the list
# print(random.sample(numbers, k=8))  # Returns a list of 3 random elements from the list