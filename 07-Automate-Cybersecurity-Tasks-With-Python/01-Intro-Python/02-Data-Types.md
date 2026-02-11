# 🧠 Python Data Types for Security Analysts

---

## 🔎 Big Idea: Why Data Types Matter

In a kitchen:
- Carrots & peppers → vegetables  
- Chicken & mutton → meat  

We categorize them because **how we handle them differs**.

In Python:
- Strings, integers, Booleans, lists, etc.  
are categories of data.

👉 **Data type = category of information that determines how Python treats it.**

If you misunderstand the type → your logic breaks.

---

# 🧵 1. String (str)

## What is it?
An ordered sequence of characters:
- letters
- numbers
- symbols
- spaces

Must be inside quotes:
- "text"
- 'text'

Examples:

    print("updates needed")
    print('20%')
    print("5.0")
    print("")

"" → empty string

⚠ Important:
"35" is NOT a number.
It cannot be used for calculations.

## Security Scenario
You extract an IP from logs:
    ip = "192.168.1.10"

It’s text — not something you can mathematically calculate.

---

# 🔢 2. Integer (int)

Whole numbers.
No decimal point.

Examples:
-100
-1
0
1
500

Example:

    print(5)
    print(5 + 2)

Output:
7

## Security Scenario
Counting failed login attempts:

    failed_attempts = 7

Integers are perfect for:
- counters
- thresholds
- event totals

---

# 🌊 3. Float (float)

Numbers with decimals.

Examples:
-2.2
0.0
3.14

Example:

    print(1.2 + 2.8)

Output:
4.0

## Division Rules

Normal division `/` returns float:

    print(1/4)

Output:
0.25

Floor division `//` rounds down:

    print(1//4)

Output:
0

## Security Scenario
Risk scoring system:
- Risk score = 7.5
- Confidence score = 0.82

Floats are used for:
- probabilities
- percentages
- scoring models

---

# ✅ 4. Boolean (bool)

Only two values:
- True
- False

Examples:

    print(True)
    print(9 > 10)

Output:
False

## Security Scenario
Access check:

    is_admin = True
    is_authenticated = False

Booleans power:
- conditional logic
- decision making
- access control rules

Think:
IF condition is True → do something.

---

# 📦 5. List (list)

Ordered collection of items.
Uses square brackets [].

Examples:

    print([12, 36, 54])
    print(["Abhishek", "Ravi", "Om"])
    print([])

[] → empty list

Lists can contain:
- strings
- integers
- floats
- Booleans
- mixed types

Example:

    users = ["abhishek", "ravi", "om"]

## Security Scenario
Store usernames with access to a confidential file:

    authorized_users = ["abhishek", "ravi", "om"]

Lists are perfect for:
- user collections
- IP lists
- hash lists
- IOC storage

---

# 🔒 6. Tuple (tuple)

Like a list — but cannot change (immutable).
Uses parentheses ().

Example:

    software_ids = ("AV01", "FW02", "IDS09")

🔐 Why useful in security?
When you want to ensure:
- configuration values cannot be modified
- baseline identifiers stay constant

Tuples are memory efficient.

---

# 📘 7. Dictionary (dict)

Stores key-value pairs.
Uses curly braces {}.

Format:
key: value

Example:

    building_map = {
        1: "East",
        2: "West",
        3: "North"
    }

## Security Scenario
Mapping user to role:

    user_roles = {
        "abhishek": "admin",
        "ravi": "analyst",
        "om": "viewer"
    }

Perfect for:
- structured log data
- configuration settings
- mapping IDs to values

---

# 🧩 8. Set (set)

Unordered collection of UNIQUE values.
No duplicates allowed.

Example:

    suspicious_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.1"}

Duplicate removed automatically.

## Security Scenario
Storing unique compromised IP addresses.
Sets automatically remove duplicates.

Great for:
- deduplication
- fast membership checks

---

# 🎯 Real-World SOC Mapping

| Security Task | Best Data Type |
|---------------|---------------|
| Store usernames | list |
| Count failed attempts | integer |
| Risk score | float |
| Access allowed? | Boolean |
| Map user → role | dictionary |
| Fixed baseline values | tuple |
| Unique IPs | set |
| Raw log message | string |

---

# 🧠 Memory Tricks

- String = text
- Integer = whole number
- Float = decimal
- Boolean = True/False decision
- List = ordered collection (editable)
- Tuple = ordered collection (locked)
- Dictionary = key → value mapping
- Set = unique items only

Think:
👉 "Type determines behavior."

If you choose the wrong data type:
- math fails
- logic breaks
- automation becomes unreliable

---

# 🚀 Why This Matters in Cybersecurity

Every log.
Every alert.
Every user.
Every score.

Is stored in a specific data type.

Understanding types means:
- writing cleaner automation
- preventing logic errors
- building reliable security tools

Master data types → master automation.

---

**✍️ Notes By Abhishek (Ez Abyss)**
