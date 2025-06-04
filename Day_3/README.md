# 📘 Day 03 – Python Data Structures: Lists, Tuples, Dictionaries & Sets

Welcome to Day 3 of the **30 Days Python Challenge**!  
In this lesson, we explored Python's most commonly used data structures and built a mini **Inventory Management System** using dictionaries.

---

## 📚 Topics Covered

### ✅ Lists
- Ordered and mutable collection
- Indexing, slicing, and negative indexing
- Common methods: `append()`, `insert()`, `remove()`, `pop()`, `clear()`, `sort()`, `copy()`
- List operations: `+`, `*`, `extend()`

### ✅ Tuples
- Ordered and immutable
- Allow duplicate values
- Accessing items using index and negative index
- Converting tuple to list to make changes
- Adding and joining tuples using `+` and `*`
- Methods: `count()`, `index()`

### ✅ Sets
- Unordered, unindexed, and do not allow duplicates
- Methods: `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `update()`
- Joining sets and set operations

### ✅ Dictionaries
- Key-value pair structure
- Methods: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`
- Adding, modifying, and deleting key-value pairs

---

## 🛠️ Mini Project: Inventory Management System

A basic program to manage store inventory using Python dictionaries.

### Features:
- Display current inventory
- Add new items
- Update quantities
- Remove items

### Sample Code:
```python
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

def display_inventory():
    for item, qty in inventory.items():
        print(f"{item}: {qty}")

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item):
    inventory.pop(item, None)

def update_quantity(item, quantity):
    inventory[item] = quantity

