#!/usr/bin/env python3
"""
lab_strings.py
Python Strings for Security Automation
Employee ID Standardization • Device ID Parsing • URL Extraction
"""

# ----------------------------
# Task 1: Convert employee_id to string
# ----------------------------
employee_id = 4186
print("Task 1 — Convert Employee ID to String")
print("Original data type:", type(employee_id))

employee_id = str(employee_id)
print("Converted data type:", type(employee_id))
print()

# ----------------------------
# Task 2: Validate employee_id length
# ----------------------------
print("Task 2 — Validate Employee ID Length")
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")
print()

# ----------------------------
# Task 3: Standardize employee_id (prefix if 4 digits)
# ----------------------------
print("Task 3 — Standardize Employee ID")
print("Before update:", employee_id)

if len(employee_id) < 5:
    employee_id = "E" + employee_id

print("After update:", employee_id)
print()

# ----------------------------
# Task 4: Extract 4th character from device_id
# ----------------------------
device_id = "r262c36"
print("Task 4 — Extract 4th Character from Device ID")
print("Device ID:", device_id)
print("4th character:", device_id[3])
print()

# ----------------------------
# Task 5: Extract first 3 characters from device_id
# ----------------------------
print("Task 5 — Extract First 3 Characters from Device ID")
print("First three characters:", device_id[0:3])
print()

# ----------------------------
# Task 6: Extract protocol from URL
# ----------------------------
url = "https://exampleURL1.com"
print("Task 6 — Extract URL Protocol")
print("URL:", url)
print("Protocol:", url[0:8])
print()

# ----------------------------
# Task 7: Locate ".com" using index()
# ----------------------------
print("Task 7 — Locate Domain Extension")
ind = url.index(".com")
print("Index of '.com':", ind)
print()

# ----------------------------
# Task 9: Extract domain extension using slicing
# ----------------------------
print("Task 9 — Extract Domain Extension")
print("Domain extension:", url[ind:ind+4])
print()

# ----------------------------
# Task 10: Extract website name using slicing + ind
# ----------------------------
print("Task 10 — Extract Website Name")
website_name = url[8:ind]
print("Website name:", website_name)
