---
marp: true
---


# 🐍 Python Scripting Notes – हिंदी में (with Examples)

---

## 1️⃣ Python की शुरुआत (Getting Started)
**🔹 Python क्या है?**  
Python एक high-level, interpreted language है जो automation, web dev, scripting, AI सबमें use होती है।

**🔹 Python चलाने के तरीके:**  
- IDLE (Python का inbuilt editor)  
- VS Code / PyCharm  
- Command Line: `python script.py`

---

## 2️⃣ Variables & Data Types

```python
name = "Tarun"       # String
age = 21             # Integer
price = 99.99        # Float
is_admin = True      # Boolean
```

---

## 3️⃣ Input और Output

```python
name = input("तुम्हारा नाम क्या है? ")
print("Hello,", name)
```

---

## 4️⃣ Conditional Statements (if-else)

```python
age = int(input("Age? "))
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 5️⃣ Loops (for, while)

```python
# For loop
for i in range(5):
    print("Hello", i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 6️⃣ Functions (def keyword)

```python
def greet(name):
    print("Hi", name)

greet("Lucy")
```

---

## 7️⃣ Lists, Tuples, Dictionaries

```python
# List
fruits = ["apple", " "banana", "mango"]
print(fruits[0])

# Tuple (immutable)
colors = ("red", "green", "blue")

# Dictionary
person = {"name": "Tarun", "age": 21}
print(person["name"])
```

---

## 8️⃣ File Handling

```python
# Write to file
with open("data.txt", "w") as f:
    f.write("Hello file!")

# Read from file
with open("data.txt", "r") as f:
    print(f.read())
```

---

## 9️⃣ Error Handling (Try-Except)

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Zero से divide नहीं कर सकते!")
```

---

## 🔟 Modules और Libraries

```python
import math
print(math.sqrt(16))

import datetime
print(datetime.datetime.now())
```

---

## 🔁 Useful Libraries for Scripting

| Library     | Use                             |
|-------------|----------------------------------|
| `os`        | File & folder handling          |
| `sys`       | System commands                 |
| `subprocess`| Terminal commands run करना     |
| `time`      | Time delays                     |
| `json`      | JSON handle करना               |
| `requests`  | HTTP requests भेजना            |

---

## 🧠 Automation Script Example:

```python
import os

def create_folders():
    for i in range(5):
        os.mkdir(f"Folder_{i}")
        print(f"Folder_{i} created")

create_folders()
```

---

## 🛠️ Bonus Tips

- `.py` फ़ाइल बना कर scripts सेव करो  
- `chmod +x script.py` (Linux में executable बनाने के लिए)  
- Shebang line: `#!/usr/bin/env python3`  
- Scripts को schedule करने के लिए cronjob (Linux) या Task Scheduler (Windows) use करो  
