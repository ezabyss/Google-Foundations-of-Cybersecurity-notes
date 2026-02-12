# 🔎 String Indexing, Slicing & Searching in Python  

---

# 🧠 Why This Matters in Cybersecurity

In security, strings represent:

- Usernames
- IP addresses
- URLs
- Email addresses
- File paths
- Device IDs
- Log entries

If you can index and search strings,
you can extract indicators from logs efficiently.

---

# 📌 What Is an Index?

An index is:
→ The position number of a character in a sequence  
→ Starts at 0 in Python  

Example string:

    "HELLO"

Index positions:

    H  E  L  L  O
    0  1  2  3  4

---

# 🔹 Accessing Characters (Bracket Notation)

Syntax:

    string[index]

Example:

    print("HELLO"[1])

Output:
E

Because indexing starts at 0.

---

🔐 Security Example

Device ID:

    device_id = "h32rb17"
    print(device_id[0])

Output:
h

Useful when:
- First character represents device type
- Prefix identifies department
- Certain position stores environment code

---

# 🔹 Negative Indexing

Python allows reverse indexing.

Example:

    device_id = "h32rb17"
    print(device_id[-1])

Output:
7

Negative index reference:

    h  3  2  r  b  1  7
   -7 -6 -5 -4 -3 -2 -1

🔐 Useful when:
- Extracting file extensions
- Getting last digit of ID
- Checking final character of hash

---

# ✂️ String Slicing

Slice = Extract multiple characters.

Syntax:

    string[start:end]

✔ Start index is included  
❌ End index is excluded  

Example:

    print("HELLO"[1:4])

Output:
ELL

Because:
- Start at index 1
- Stop before index 4

---

🔐 Security Scenario: Extract Part of IP

    ip = "192.168.10.45"
    print(ip[0:3])

Output:
192

Could be used to:
- Identify network class
- Separate subnets
- Extract region code

---

# 🔎 Searching with .index()

Method:

    string.index("value")

Returns:
→ Index of first occurrence  
→ Error if not found  

Example:

    print("HELLO".index("E"))

Output:
1

---

# 🔁 Multiple Occurrences

    print("HELLO".index("L"))

Output:
2

Even though "L" appears twice,
only the first occurrence is returned.

⚠ Important in log investigations.

---

🔐 Security Example: Find @ in Email

    email = "admin@company.com"
    at_position = email.index("@")
    print(at_position)

Output:
5

You can now:
- Extract username
- Extract domain

Example:

    username = email[0:at_position]
    print(username)

Output:
admin

---

# 🔍 Searching for Substrings

.index() also works with substrings.

    log = "tsnow, tshah, bmoreno - updated"
    print(log.index("tshah"))

Output:
7

⚠ Be careful:

    print(log.index("ts"))

Output:
0

Because "ts" appears earlier in "tsnow".

Precision matters in threat hunting.

---

# ⚠ What Happens If Not Found?

    print("h32rb17".index("a"))

Result:
Error (ValueError)

In real scripts, always handle this carefully.

---

# 🔒 Strings Are Immutable

Immutable means:
→ Cannot change characters directly

Example:

    my_string = "HELLO"
    my_string[1] = "A"

❌ Error

You cannot modify string characters using index notation.

---

# 🔄 Correct Way to “Modify” a String

You must create a new string.

Example:

    my_string = "HELLO"
    new_string = "H" + "A" + my_string[2:]
    print(new_string)

Output:
HALLO

Strings never change.
You create new versions.

---

# 🔧 Useful String Functions Recap

Convert to string:

    string_id = str(19329302)

Get length:

    len("h32rb17")

Convert case:

    "admin".upper()
    "ADMIN".lower()

---

# 🏆 Security Insight

When analyzing logs:

You will:
✔ Extract IP segments
✔ Separate username from domain
✔ Validate ID format
✔ Detect malicious patterns
✔ Parse URLs
✔ Search suspicious substrings

All of that starts with:
→ Indexing  
→ Slicing  
→ Searching  

Mastering strings = mastering log parsing.

---

# 🎯 Summary

✔ Indices start at 0  
✔ Negative indices count from end  
✔ Slicing excludes end index  
✔ .index() returns first occurrence  
✔ Strings are immutable  
✔ Substring matching requires precision  

---

**✍️ Notes By Abhishek (Ez Abyss)**
