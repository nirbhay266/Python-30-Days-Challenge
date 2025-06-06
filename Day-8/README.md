# 🐍 Day 08 - Object-Oriented Programming in Python

**Date:** June 4, 2025  
**Challenge:** [#30DaysOfPython](https://indiandataclub.com) by [Indian Data Club](https://indiandataclub.com)

---

## 🔍 What I Learned Today

Today was all about understanding how Python implements **Object-Oriented Programming (OOP)**.  
OOP is one of the most powerful concepts in modern programming, and Python makes it super beginner-friendly.

---

## 📚 Topics Covered

✅ Classes and Objects  
✅ The `__init__()` Constructor  
✅ Defining Methods  
✅ Using the `self` Parameter  
✅ The `__str__()` Function  
✅ Modifying Object Properties  
✅ Deleting Objects with `del`  
✅ Empty Class using `pass`

---

## 🧠 Key Concepts

### ▶️ Creating a Class & Object
```python
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)  # Output: 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 23)
print(p1.name, p1.age)

▶️ Adding __str__() for Readable Output
class Student:
    def __init__(self, name, age, classname):
        self.name = name
        self.age = age
        self.classname = classname

    def __str__(self):
        return f"Student name: {self.name}, Age: {self.age}, Class: {self.classname}"

Challenge
✅ Task:
Create a Car class with the following:

Attributes: brand, model, year

Method: display_info() to print car details

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Tesla", "Model S", 2022)
print(car1.display_info())

