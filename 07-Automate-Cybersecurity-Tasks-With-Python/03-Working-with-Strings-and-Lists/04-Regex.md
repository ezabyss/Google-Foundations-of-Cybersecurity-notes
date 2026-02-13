# 🔍 Regular Expressions for Security Analysts (Top 1% Notes)

## 🎯 Why Regex Matters in Cybersecurity

As a security analyst, you rarely search for exact values. You search
for patterns.

Examples: 
- All IP addresses from a suspicious network 
- All email addresses in a compromised log
- All failed login attempts with more than 3 digits
- All device IDs matching a specific structure

Regular expressions (regex) allow you to detect patterns at scale.

------------------------------------------------------------------------

# 🧠 What is a Regular Expression?

A regular expression (regex) is a sequence of characters that defines a
search pattern.

------------------------------------------------------------------------

# 📦 Importing the Regex Module

    import re

To search for patterns:

    re.findall(pattern, text)

------------------------------------------------------------------------

# 🔤 Core Regex Building Blocks

## Character Types

## 📘 Regular Expression Symbols Reference

| Symbol | Meaning |
|--------|---------|
| `\w` | Alphanumeric character (`A–Z`, `a–z`, `0–9`, `_`) |
| `\d` | Digit (`0–9`) |
| `\s` | Whitespace (space, tab, newline) |
| `.` | Any character except newline |
| `\.` | Literal period (`.`) |


Example:

    re.findall(r"\d", "h32rb17")

------------------------------------------------------------------------

## Quantifiers

  Symbol   Meaning
  -------- -----------------------
  \+       One or more
  \*       Zero or more
  {n}      Exactly n times
  {m,n}    Between m and n times

Example:

    re.findall(r"\d+", "h32rb17")

------------------------------------------------------------------------

# 🔎 Scenario 1: Detect Network 184 IPs

Pattern:

    r"184\.\d+\.\d+\.\d+"

Example:

    import re
    log = "184.45.23.1 192.168.1.5 184.200.45.3 10.0.0.1"
    print(re.findall(r"184\.\d+\.\d+\.\d+", log))

------------------------------------------------------------------------

# 📧 Scenario 2: Extract Emails

Pattern:

    r"\w+@\w+\.\w+"

Example:

    import re
    email_log = '''
    User login from user1@email.com
    Failed attempt from admin@test.net
    '''
    print(re.findall(r"\w+@\w+\.\w+", email_log))

------------------------------------------------------------------------

# 🏢 Scenario 3: Extract Username + Login Attempts

Pattern:

    r"\w+:\s\d+"

Example:

    import re
    pattern = r"\w+:\s\d+"
    employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
    print(re.findall(pattern, employee_logins_string))

------------------------------------------------------------------------

# 🎓 Key Takeaways

-   Regex enables scalable log analysis
-   Use re.findall() to extract matches
-   Combine character classes + quantifiers
-   Always test patterns carefully

------------------------------------------------------------------------

**✍️ Notes By Abhishek (Ez Abyss)**
