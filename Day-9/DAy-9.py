#  Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# 🔹 Types of Inheritance in Python:
# Single Inheritance – 1 child inherits from 1 parent.

# Multiple Inheritance – 1 child inherits from multiple parents.

# Multilevel Inheritance – Child of a child class.

# Hierarchical Inheritance – Multiple children from one parent.

# Hybrid Inheritance – Combination of more than one type.

#Example: Single Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
# Create an object of the Dog class and call its methods
my_dog = Dog()
print(my_dog.speak())  # Output: Animal speaks`
print(my_dog.bark())   # Output: Dog barks

# What is Multiple Inheritance in Python?

# In Multiple Inheritance, a child class inherits properties and methods from two or more parent classes.

# In simple words, the child class acquires the knowledge or features of multiple parent classes within itself.

class father:
    def __init__(self):
        self.father_name = "John"

    def father_info(self):
        return f"Father's Name: {self.father_name}"
class mother:
    def __init__(self):
        self.mother_name = "Jane"

    def mother_info(self):
        return f"Mother's Name: {self.mother_name}"
class child(father, mother):
    def __init__(self):
        father.__init__(self)
        mother.__init__(self)
        self.childname="NIRBHAY"
    def child(self):
        return f"Child name is :{self.childname}"
c=child()
print(c.father_info())
print(c.child())
print(c.mother_info())

#  What is Multilevel Inheritance in Python?
# In Multilevel Inheritance, one class inherits from another class, and that class itself inherits from a third class.

# In simple terms:
# Grandparent → Parent → Child
# The child class indirectly inherits the features of the grandparent class as well.
    # Grandfather
    #     ↓
    #    Father
    #     ↓
    #    Child

class Grandfather:
    def __init__(self):
        self.grandfathername="KanhaeYadav"
        self.grandfatherAge= 80
        self.grandfatherCountry="India"
    def grandfather_info(self):
        return f"Grandfather's Name: {self.grandfathername}, Age: {self.grandfatherAge}, Country: {self.grandfatherCountry}"
class Father(Grandfather):
    def __init__(self):
        Grandfather.__init__(self)
        self.fathername="Sonalal yadav" 
        self.fatherage= 50
        self.fathervillege="Godhiya"
    def father_info(self):
        return f"Father's Name: {self.fathername}, Age: {self.fatherage}, Village: {self.fathervillege}"
class Child(Father):
    def __init__(self):
        Father. __init__(self)
        self.childname="Nirbhay Yadav"
        self.childage= 23
    def child_info(self):
        return f"Child's Name: {self.childname}, Age: {self.childage}"

c = Child()
print(c.grandfather_info())  # Output: Grandfather's Name: KanhaeYadav, Age: 80, Country: India
print(c.father_info())       # Output: Father's Name: Sonalal yadav, Age: 50, Village: Godhiya
print(c.child_info())         # Output: Child's Name: Nirbhay Yadav, Age: 23


# What is Hierarchical Inheritance in Python?
# Jab ek parent class se multiple child classes inherit karti hain, to usse Hierarchical Inheritance kehte hain.

# Yaad raho:
# 1 Parent → Many Children

# 🔸 Diagram:
# markdown
# Copy
# Edit
#         Parent
#        /   |   \
# Child1  Child2  Child3

class animal:
    def speak(self):
        return "Animals can make sounds"
class dog(animal):
    def bark(self):
        return "Dog barks Woof!"
class cat(animal):
    def meow(self):
        return "Cat meows Meow!"
class cow(animal):
    def moo(self):
        return "Cow moos Moo!"
# Create objects of each child class and call their methods
my_dog = dog()
my_cat = cat()
my_cow = cow()
print(my_dog.speak())  # Output: Animals can make sounds
print(my_dog.bark())   # Output: Dog barks Woof!    
print(my_cat.speak())  # Output: Animals can make sounds

# Polymorphism in Python:
# Polymorphism is the ability of a function, method, or operator to behave differently based on the object or data it is working with.

# In simple terms:

# "One name, many forms."

# It allows different classes to implement methods with the same name in their own way.

class car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def activity(self):
        print("Drive the car")
class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def activity(self):
        print("Sail the boat")
class Plane:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def activity(self):
        print("Fly the plane")
# Function to demonstrate polymorphism
def perform_activity(vehicle):
    vehicle.activity()
# Create instances of each class
my_car = car("Toyota", "Camry")
my_boat = Boat("Yamaha", "242X")
my_plane = Plane("Boeing", "747")
# Call the perform_activity function with different objects

