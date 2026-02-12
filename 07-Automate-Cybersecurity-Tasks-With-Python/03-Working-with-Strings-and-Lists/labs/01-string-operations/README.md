# 🔐 Python Strings for Security Automation

## 📌 Overview

Security analysts frequently work with structured string-based data such as:

- Employee IDs  
- Device IDs  
- URLs  
- Network logs  
- System identifiers  

This lab demonstrates practical Python string manipulation skills used in real-world security automation and investigation workflows.

You will standardize an employee ID, extract parts of a device ID, and parse components of a URL.

---

## 🎯 Skills Demonstrated

- Convert integers to strings using `str()`
- Validate formatting using `len()`
- Apply conditional logic using `if`
- Concatenate strings using `+`
- Extract characters using indexing
- Extract substrings using slicing
- Locate substrings using `.index()`
- Parse structured URL components

---

## ▶️ How to Run

```bash
python3 lab_strings.py
```

---

# 🧩 Task Walkthrough

---

## Task 1 — Convert Employee ID to String

```python
employee_id = 4186
print(type(employee_id))

employee_id = str(employee_id)
print(type(employee_id))
```

Expected Output:

```text
<class 'int'>
<class 'str'>
```

---

## Task 2 — Validate Employee ID Length

```python
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")
```

---

## Task 3 — Standardize the ID

```python
print("Before update:", employee_id)

if len(employee_id) < 5:
    employee_id = "E" + employee_id

print("After update:", employee_id)
```

Expected Output:

```text
Before update: 4186
After update: E4186
```

---

## Task 4 — Extract Character from Device ID

```python
device_id = "r262c36"
print(device_id[3])
```

Expected Output:

```text
2
```

---

## Task 5 — Extract Substring from Device ID

```python
print(device_id[0:3])
```

Expected Output:

```text
r26
```

---

## Task 6 — Extract URL Protocol

```python
url = "https://exampleURL1.com"
print(url[0:8])
```

Expected Output:

```text
https://
```

---

## Task 7 — Locate Domain Extension

```python
print(url.index(".com"))
```

Expected Output:

```text
19
```

---

## Task 8 — Store Index for Reuse

```python
ind = url.index(".com")
```

---

## Task 9 — Extract Domain Extension

```python
print(url[ind:ind+4])
```

Expected Output:

```text
.com
```

---

## Task 10 — Extract Website Name

```python
print(url[8:ind])
```

Expected Output:

```text
exampleURL1
```

---

# 🛡 Real-World Security Applications

These string techniques are used in:

- SIEM log parsing  
- Phishing URL inspection  
- IOC extraction  
- Identity normalization  
- Automated validation scripts  

---

# This lab demonstrates:

- Practical Python fundamentals  
- Security-oriented thinking  
- Clean documentation  
- Real-world applicability  

---

**✍️ Notes By Abhishek (Ez Abyss)**
