# Datetime module, formatting, time differences
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as
# date objects
import datetime

x = datetime.datetime.now()
print(x)
#---------------------------------------------------------------------------------------------------------------
# Date Output
# When we execute the code from the example above the result will be:

# 2025-06-08 13:07:49.844793
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

# Here are a few examples, you will learn more about them later in this chapter:

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
date= datetime.datetime(1999, 12, 31)
print(date)
print(date.month)
print(date.strftime("%B"))  # Prints the full month name
print(date.strftime("%b"))  # Prints the abbreviated month name
print(date.strftime("%d"))  # Prints the day of the month
print(date.strftime("%Y"))  # Prints the year with century
print(date.strftime("%y"))  # Prints the year without century
print(date.strftime("%A"))  # Prints the full weekday name
print(date.strftime("%a"))  # Prints the abbreviated weekday name
print(date.strftime("%j"))  # Prints the day of the year
print(date.strftime("%W"))  # Prints the week number of the year (Monday as the first day of the week)
print(date.strftime("%H"))  # Prints the hour (24-hour clock)
print(date.strftime("%I"))  # Prints the hour (12-hour clock)
print(date.strftime("%M"))  # Prints the minute
print(date.strftime("%S"))  # Prints the second
# Print the date in a locale-specific format
print(date.strftime("%x"))  # Prints the date in a locale-specific format
# Print the time in a locale-specific format
print(date.strftime("%X"))  # Prints the time in a locale-specific format
# Print the date and time in a locale-specific format
print(date.strftime("%c"))  # Prints the date and time in a locale-specific format
#---------------------------------------------------------------------------------------------------------------

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))






