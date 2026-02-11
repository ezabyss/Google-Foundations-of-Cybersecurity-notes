# 🤖 Python Conditionals for Security Automation

---

## 🧠 Big Idea: Automation Needs Decision-Making

Automation is:
> Using technology to reduce human effort for repetitive tasks.

But automation without logic is useless.

Computers must decide:
- Should I lock this account?
- Should I block this IP?
- Should I escalate this alert?

That’s where **conditional statements** come in.

---

# 🔎 What Is a Conditional Statement?

A conditional statement:
> Evaluates a condition and executes code only if that condition is True.

Structure:

    if condition:
        action

Python evaluates the condition as:
- True → runs the indented code
- False → skips it

Indentation is mandatory.

---

# 🧪 Real-World Example (Account Lock)

Security Rule:
> Lock account if failed logins exceed 5.

    failed_attempts = 7

    if failed_attempts > 5:
        print("Account locked")

Output:
Account locked

Why?
7 > 5 → True

---

# 📊 Comparison Operators (Core Tools)

| Operator | Meaning |
|-----------|---------|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |
| `==` | equal to |
| `!=` | not equal |

⚠ Important:
`=` assigns  
`==` compares  

This is a common mistake.

---

# 🖥️ Checking Operating System (String Comparison)

    operating_system = "OS 2"

    if operating_system == "OS 2":
        print("Updates needed")

Output:
Updates needed

Python compares strings using `==`.

---

# 🔄 Adding an `else` Statement

If first condition fails, run something else.

    operating_system = "OS 3"

    if operating_system == "OS 2":
        print("Updates needed")
    else:
        print("No updates needed")

Output:
No updates needed

Logic Flow:
1. Check if condition
2. If False → move to else

---

# 🧩 Using `elif` for Multiple Conditions

Useful when handling multiple outcomes.

    status = 400

    if status == 200:
        print("OK")
    elif status == 400:
        print("Bad Request")
    elif status == 500:
        print("Internal Server Error")
    else:
        print("Check other status")

Python stops at the first True condition.

Important:
- `elif` only runs if previous conditions are False
- `else` runs if ALL conditions fail

---

# 🧠 Real SOC Example: HTTP Response Monitoring

    if status >= 200 and status <= 226:
        print("Successful response")

This checks:
- status >= 200
AND
- status <= 226

Both must be True.

---

# 🔗 Logical Operators

## `and` → both must be True

    if failed_attempts > 3 and failed_attempts <= 5:
        print("Warning")

## `or` → only one must be True

    if status == 100 or status == 102:
        print("Informational response")

## `not` → reverses condition

    if not(status >= 200 and status <= 226):
        print("Check status")

Parentheses matter here.
Python evaluates inside parentheses first.

---

# 🏗️ Structure of a Conditional

Every conditional has:

1️⃣ Header  
2️⃣ Colon `:`  
3️⃣ Indented body  

Example:

    if status == 200:
        print("OK")

Without colon → syntax error  
Without indentation → error  

Python is strict about structure.

---

# ⚠ Difference: Multiple `if` vs `elif`

Multiple `if`:

    if status == 200:
        print("OK")

    if status == 400:
        print("Bad Request")

Python checks BOTH.

Using `elif`:
Stops after first True condition.

In automation, this matters for efficiency.

---

# 🔐 Cybersecurity Automation Scenarios

## 🔒 Lock Account

    if failed_attempts > 5:
        print("Account locked")

## 🚫 Block Suspicious IP

    if suspicious_ip == "192.168.1.10":
        print("Block IP")

## ⚠ High Severity Alert

    if severity >= 8:
        print("Escalate to Level 2")

## 🛡 Malware Detection

    if malware_detected == True:
        print("Isolate device")

---

# 🎯 Why Conditionals Matter in SOC

Without conditionals:
- Scripts are static
- No decision-making
- No automation

With conditionals:
- Intelligent response
- Faster triage
- Reduced manual workload
- Scalable security operations

Automation = Logic + Conditionals

---

# 🧠 Mental Model

If statement = Security rule  
Condition = Detection criteria  
Body = Response action  

Example:
Detection rule:
> If login failures > 5 → lock account

That is literally:

    if failed_attempts > 5:
        lock_account()

You are writing detection logic.

---

# 🚀 Key Takeaways

✔ `if` starts conditional  
✔ `else` handles fallback  
✔ `elif` handles multiple branches  
✔ `==` compares values  
✔ Indentation is required  
✔ `and`, `or`, `not` create complex logic  

Conditionals are the foundation of:
- Automation
- Incident response scripting
- Detection logic
- Security tooling

Master conditionals →
You start thinking like a detection engineer.

---

**✍️ Notes By Abhishek (Ez Abyss)**
