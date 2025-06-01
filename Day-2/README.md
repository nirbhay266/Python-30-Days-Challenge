# 📘 Day 02: Variables and Data Types – 30-Day Python Challenge

🗕️ **Date:** May 29, 2025
👨‍💻 **Challenge:** Day 2 of 30

---

## 🔥 What I Learned

On **Day 2** of my Python journey, I focused on one of the most essential foundations of any programming language: **Variables and Data Types**.

---

## 🧹 Topics Covered

### 1. ✅ **Variables**

A variable is a container for storing data values.

📝 **Example:**

```python
x = 5
name = "Nirbhay"
```

You don’t need to declare the type of variable in Python — it automatically detects the type.

---

### 2. 🔢 **Data Types in Python**

Python has several built-in data types. The most common are:

#### a) **Integers (`int`)**

Whole numbers without decimal points.

```python
age = 25
print(type(age))  # Output: <class 'int'>
```

#### b) **Floating Point Numbers (`float`)**

Numbers with decimal points.

```python
cgpa = 8.5
print(type(cgpa))  # Output: <class 'float'>
```

#### c) **Strings (`str`)**

Text data enclosed within quotes (`' '` or \`" ").

```python
name = "Nirbhay"
print(type(name))  # Output: <class 'str'>
```

#### d) **Booleans (`bool`)**

Used to represent `True` or `False`.

```python
is_student = True
print(type(is_student))  # Output: <class 'bool'>
```

---

### 3. 🔄 **Type Conversion (Type Casting)**

Sometimes, we need to convert data from one type to another.

```python
age = 25
print(float(age))  # Converts int to float
```

Common functions:

* `int()`: Convert to integer
* `float()`: Convert to float
* `str()`: Convert to string

---

### 4. 🧾 **Formatted Strings (f-strings)**

Used to display variables inside strings more cleanly and professionally.

```python
name = "Nirbhay"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

---

### 5. ✂️ **String Indexing and Slicing**

Strings are like arrays of characters. You can access parts of a string using slicing.

```python
name = "Nirbhay Kumar"
print(name[0])      # N
print(name[2:6])    # rbha
print(name[:7])     # Nirbhay
print(name[8:])     # Kumar
```

---

### 6. 🧠 **Boolean Logic and Conditions**

Booleans are often used with conditionals (`if`, `else`).

```python
age = 18
if age > 18:
    print("You are above 18")
else:
    print("You are 18 or below")
```

---

## ✅ Sample Practice Code

```python
# Integer Example
age = 25
family = 6
print(f"My age is {age}")
print("Family members:", family)
print(float(age))  # Type conversion

# Float Example
cgpa = 8.5
percentage = 80.2
print(f"My CGPA is {cgpa}")
print(int(cgpa))  # Casting float to int

# String Example
fname = "Nirbhay"
lname = "Yadav"
print(fname + " " + lname)
print(fname[0:4])  # String slicing

# Boolean Example
age = 18
if age > 18:
    print("Age is greater than 18")
else:
    print("Age is less than or equal to 18")
```

---

## 📌 Key Takeaways

* Python automatically identifies data types.
* `type()` is used to check the data type of a variable.
* f-strings are very helpful for writing readable output.
* Type conversion helps when working with different data types.
* Booleans are very useful for logical conditions.
* String slicing lets you extract specific parts of a string.

---

## 🎯 What's Next?

🔜 Moving on to **Day 03: Python Operators and Expressions**
There, I will explore how to perform calculations and comparisons using variables.

---

## 🏷️️ Hashtags

`#30DayPython` `#Day02` `#PythonChallenge` `#LearnPython` `#Variables` `#DataTypes` `#CodeNewbie` `#SystumOfCoding` `#PythonBasics`

