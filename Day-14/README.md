# 📅 Day 14 – Recursion | #30DaysOfPython

Welcome to Day 14 of the **#30DaysOfPython** challenge by [Indian Data Club](https://indiandataclub.com)!  
Today’s focus is on one of the most important concepts in programming – **Recursion**.

---

## 🔁 What is Recursion?

Recursion is a method of solving problems where a function calls itself as a subroutine.  
It helps to break down complex problems into smaller, more manageable sub-problems.

---

## 🧠 Key Concepts

- **Recursive Function**: A function that calls itself.
- **Base Case**: The condition under which recursion stops.
- **Call Stack**: Tracks each recursive call and returns values once the base case is reached.

---

## 🧪 Example: Factorial Using Recursion

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120

