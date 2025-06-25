# 🔁 Day 16 – Generators and Iterators in Python

📅 **Date**: June 12, 2025  
🔖 **Challenge**: #30DaysOfPython by [Indian Data Club](https://indiandataclub.com)

---

## 🧠 Topics Covered

- `yield` keyword and lazy evaluation
- Difference between **iterators** and **generators**
- Creating custom generator functions
- Benefits of generators for memory-efficient programming

---

## 🎯 Challenge

**Generate the first `n` Fibonacci numbers using a generator**

### ✅ Example:

```python
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci_gen(10):
    print(num, end=' ')

