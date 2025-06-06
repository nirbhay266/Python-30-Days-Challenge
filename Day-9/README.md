# 🔥 Day 0️⃣9️⃣ – Inheritance & Polymorphism | #30DaysOfPython

Welcome to Day 9 of the **#30DaysOfPython** challenge hosted by [Indian Data Club](https://indiandataclub.com)!  
Today’s focus: Dive deep into the powerful concepts of **Object-Oriented Programming (OOP)** — *Inheritance* and *Polymorphism* — that make Python truly modular and reusable. 🐍

---

## 📌 Topics Covered

🔹 Single Inheritance  
🔹 Multiple Inheritance  
🔹 Multilevel Inheritance  
🔹 Hierarchical Inheritance  
🔹 Hybrid Inheritance  
🔹 `super()` Function  
🔹 Polymorphism (Method Overriding & Operator Overloading)

---

## 🎯 Challenge of the Day

> 🛠️ **Task:** Extend a basic `Car` class into an `ElectricCar` subclass by adding a battery capacity attribute.

---

## 💻 Code Implementation

```python
# Parent Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"Car: {self.brand} {self.model}"

# Child Class (ElectricCar)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def electric_info(self):
        return f"{self.car_info()}, Battery: {self.battery_capacity} kWh"

# Object creation
my_ev = ElectricCar("Tesla", "Model 3", 75)

# Output
print(my_ev.car_info())        # Output from parent
print(my_ev.electric_info())   # Output from child

