# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# Syntax
# To open a file for reading it is enough to specify the name of the file:

# f = open("demofile.txt")
# The code above is the same as:

# f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.


#To open the file, use the built-in open() function.

#The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())  # Read the entire file

# Using the with statement
# You can also use the with statement when opening a file:

with open("demofile.txt","r")as  f:
    print(f.read())  # Read the entire file

# Close Files
# It is a good practice to always close the file when you are done with it.

# If you are not using the with statement, you must write a close statement in order to close the file:

f = open("demofile.txt", "r")
print(f.read())  # Read the entire file
f.close()  # Close the file

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f=open("demofile.txt", "r")
print(f.read(5))  # Read the first 5 characters of the file

#You can return one line by using the readline() method:
with open("demofile.txt","r") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt","r")as f:
    for x in f:
        print(x)

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

with open("demofile.txt","a") as f:
    f.write("\n My friend my name is nirbhay kumar and I am a software engineer")
with open("demofile.txt","r") as f:
    print(f.read())  # Read the entire file to see the appended content

with open("demofile.txt","w") as f:
    f.write("My name is Nirbhay Kumar and I am a data scientist")
# This will overwrite the entire content of the file
with open("demofile.txt","r") as f:
    print(f.read())  # Read the entire file to see the overwritten content


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

with open("myfile.txt", "w") as f:
    f.write("This is a new file created using the x mode.")
with open("myfile.txt","r") as f:
    print(f.read())  # Read the entire file to see the content of the new file

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
#os.remove("yfile.txt")  # Deletes the file named "myfile.txt"


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")  # Deletes the file named "myfile.txt"
else:
    print("File does not exists")