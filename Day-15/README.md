# 🚀 Day 15 – Python Decorators

📅 **Date**: June 11, 2025  
🔖 **Challenge**: #30DaysOfPython by [Indian Data Club](https://indiandataclub.com)

---

## 🧠 Topics Covered

- What are **Decorators** in Python?
- Creating and applying function decorators
- Use cases of decorators:
  - Logging
  - Timing function execution
  - Access control
  - Memoization

---

## 🎯 Challenge

**Create a decorator to log function execution time**

### ✅ Example:

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    return "Done!"

print(slow_function())

