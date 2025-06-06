################################################## Classes/Objects ##################################################
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

#To create a class, use the keyword class:
class MyClass:
    x = 5
# Create an object named p1 and print the value of x:
p1=MyClass()
print(p1.x)

# The __init__() Function
# The __init__() function is a special method that is automatically called when an object of a class is created.
# It allows you to initialize the attributes of the class.

# Use the __init__() function to assign values to object properties, or other operations that are necessary 
# to do when the object is being created:
class Person:
   def __init__(self,name,age):
    self.name=name
    self.age=age
# Create an object named p1, and print the value of name and age:
p1=Person("John",23)
print(p1.name)
print(p1.age)


# __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:
class student:
    def __init__(self,name,age,classname):
        self.name=name
        self.age=age
        self.classname=classname
    def __str__(self):
       return f"Student name:{self.name},Age:{self.age},classname:{self.classname}"
# Create an object named s1, and print the object:
s1=student("John",23,"BCA")
print(s1)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class student:
    def __init__(self, name, age, classname):
        self.name = name
        self.age = age
        self.classname = classname

    def display(self):
        return f"Student name: {self.name}, Age: {self.age}, Class: {self.classname}"

# Create an object named s1, and call the display method:
s1 = student("John", 23, "BCA")
print(s1.display())

# Modify Object Properties
# You can modify properties on objects like this:
s1.age = 30
print(s1.display())
s1.classname = "MCA"
print(s1.display())
s1.name="Nirbhay"
print(s1.display())

# self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that 
# belong to the class.

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter
#  of any function in the class:

class student:
    def __init__(myself,name,age):
      myself.name=name
      myself.age=age

    def __str__(myself):
        return f"Student name: {myself.name}, Age: {myself.age}"    
    def display(me):
         print(f"Student name: {me.name}, Age: {me.age}")
# Create an object named s1, and print the object:
s1 = student("John", 23)    
s1.display()  # Call the display method
print(s1)  # Print the object using the __str__ method
         