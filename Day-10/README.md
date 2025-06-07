
# 🚀 Day 10 – Exception Handling | #30DaysOfPython

Welcome to Day 10 of the **#30DaysOfPython** challenge by [Indian Data Club](http://indiandataclub.com)!  
Today’s focus was one of the most important topics in real-world coding: **Exception Handling** 🧠

---

## 📚 Topics Covered

- `try` and `except` blocks
- Catching **specific exceptions** like:
  - `ValueError`
  - `ZeroDivisionError`
  - `FileNotFoundError`
- `finally` clause to execute cleanup code (like closing files)
- Writing **safe & robust** code that doesn't crash when things go wrong

---

## 🎯 Challenge

**Task**:  
Read numbers from a file and divide 100 by each number, while gracefully handling errors.

### ✅ Requirements:
- If the file has invalid data (e.g., text), handle `ValueError`
- If the number is zero, handle `ZeroDivisionError`
- If the file doesn't exist, handle `FileNotFoundError`
- Use `finally` to ensure file is properly closed

---

## 💻 Example Code

```python
file_name = "numbers.txt"

try:
    file = open(file_name, "r")
    lines = file.readlines()

    print("Processing numbers...\n")

    for line in lines:
        line = line.strip()

        try:
            number = float(line)
            result = 100 / number
            print(f"100 divided by {number} is {result}")
        
        except ValueError:
            print(f"Invalid input: '{line}' is not a number.")
        
        except ZeroDivisionError:
            print(f"Cannot divide by zero. Skipping: {line}")
    
    file.close()

except FileNotFoundError:
    print(f"File '{file_name}' not found.")

finally:
    print("\nFinished processing the file.")
