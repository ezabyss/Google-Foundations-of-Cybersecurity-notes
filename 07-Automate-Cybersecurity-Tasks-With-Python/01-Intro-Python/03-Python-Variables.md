# 📦 Python Variables for Security Analysts

---

## 🧠 Big Idea: Variables = Smart Containers

In the kitchen:
- A container might hold rice today
- Pasta tomorrow
- Soup later

The container stays the same.
The contents change.

👉 In Python, a **variable** works exactly the same way.

A variable is:
> A named container that stores data.

---

# 🏷️ Variable Assignment (Creating a Variable)

To create a variable:

    variable_name = value

This is called **assignment**.

Example (Security context):

    device_id = "h32rb17"

Breakdown:
- `device_id` → variable name
- `=` → assignment operator
- `"h32rb17"` → string value stored inside

Python automatically assigns the correct data type.

---

# 📤 Calling (Using) a Variable

To use a variable:

    print(device_id)

⚠️ Important:
When calling a variable, do NOT use quotation marks.

This works:

    print(device_id)

This prints the literal word:

    print("device_id")

🔍 Difference:
- Without quotes → prints stored value
- With quotes → prints the string itself

---

# 🎯 Why Variables Matter in Cybersecurity

Imagine manually typing the same IP address 20 times in a script.

Instead:

    suspicious_ip = "192.168.1.10"

Then reuse:

    print(suspicious_ip)
    block_ip(suspicious_ip)

Cleaner.
Faster.
Less error-prone.

✔ Variables reduce repetition  
✔ Improve readability  
✔ Enable automation  

---

# 🔎 Checking Data Types with `type()`

If unsure what a variable contains:

    device_id = "h32rb17"
    print(type(device_id))

Output:
<class 'str'>

This helps prevent type errors.

---

# ⚠️ Type Errors (Common Beginner Mistake)

Python cannot combine incompatible data types.

Example:

    device_id = "h32rb17"
    number = 5
    print(device_id + number)

❌ ERROR → string + integer

Python can:
- add string + string
- add number + number

But not:
- string + number

SOC Reality:
Log fields often come as strings.
You must convert them before calculations.

---

# 🔄 Reassignment (Changing the Contents)

Variables can change.

    device_id = "h32rb17"
    print(device_id)

    device_id = "n73ab07"
    print(device_id)

Output:
h32rb17  
n73ab07  

The label stays the same.
The contents change.

💡 Think:
Variable name = container label  
Value = contents inside  

---

# 🔁 Assigning Variables to Variables

Example:

    username = "nzhao"
    old_username = username
    username = "zhao2"

    print("Previous:", old_username)
    print("Current:", username)

Output:
Previous: nzhao  
Current: zhao2  

Why this matters:
- Track previous state
- Maintain audit history
- Preserve baseline values

Very common in:
- Account updates
- Configuration changes
- Incident tracking

---

# 🧾 Best Practices for Naming Variables

## ✅ Allowed:
- Letters
- Numbers
- Underscores

Good examples:
- login_attempts
- device_id
- failed_count
- suspicious_ip

## ❌ Avoid:
- Python keywords (True, False, if, print)
- Special characters
- Spaces

## ⚠️ Case Sensitive

These are different:
- time
- Time
- TIME

Python treats them separately.

---

# 🎨 Style Guidelines 

✔ Use underscores between words:
    login_attempts
    invalid_usernames

✔ Make names descriptive:
    num_failed_logins
    is_authenticated
    firewall_status

❌ Avoid:
    x
    data1
    variable_that_equals_3
    start_time, starting_time, time_starting (confusing)

Good naming = readable automation.

---

# 🔐 Real-World Security Examples

## Example 1: Tracking Login Attempts

    failed_attempts = 5
    threshold = 3
    is_locked = failed_attempts > threshold

## Example 2: Managing Access List

    allowed_users = ["ezabyss", "abhishek"]
    user = "ravi"
    is_allowed = user in allowed_users  

## Example 3: Updating Device ID

    device_id = "h32rb17"
    device_id = "n73ab07"

Reassignment helps reflect real-time system changes.

---

# 🧠 Mental Model for Mastery

Variable = Labeled Box  
Data Type = Category of Item Inside  
Assignment = Put item in box  
Reassignment = Replace item  
Type error = Wrong item in wrong operation  

If your automation fails:
80% chance → wrong data type.

---

# 🚀 Why This Matters in SOC Work

Every script you write:
- Stores log entries
- Counts alerts
- Tracks users
- Flags malicious activity

All of that depends on variables.

Master variables →
You master automation.

---

# 🎯 Final Takeaways

✔ Variables store data  
✔ Variables can change  
✔ Python assigns data types automatically  
✔ Use `type()` to verify  
✔ Good naming = clean, professional code  

Clean variables → clean logic → clean investigations.

---

**✍️ Notes By Abhishek (Ez Abyss)**
