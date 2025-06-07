# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:
#Example:-
try:
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code
# for a special kind of error:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") 
#Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print("Hello")
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

f=None
try:
    with open("demfile.txt", "r") as f:    
        print(f.read())
except FileNotFoundError:
     print("Something went wrong when writing to the file")
finally:
    if f:
        f.close()
    print("Done")
        






# try:
#     a=float(input("Enter First Number"))
#     b=float(input("Enter Second Number"))
#     c=a/b
#     print("OUtput is:",c)
# except ValueError as e:
#     print("Please enter a valid number", e)
# except ZeroDivisionError as e:
#     print("Can not divide by zero", e)
# finally:
#     print("Thank for using safe calculater.")