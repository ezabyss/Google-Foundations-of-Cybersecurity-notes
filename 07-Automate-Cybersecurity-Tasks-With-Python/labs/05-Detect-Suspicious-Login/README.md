# 🚨 Detecting Suspicious Login Attempts with Python  
*Log Parsing + Algorithm + Automation*

---

## 🎯 Objective

Build a Python program that:

- Imports a log file (`.txt`)
- Parses usernames (each line = one failed attempt)
- Counts failed attempts per user
- Triggers an **alert / lockout** if failures **≥ 3**

This is foundational SOC automation logic.

---

## 🧠 Scenario

We have a `.txt` log file where:

- Each line = one failed login attempt
- Each line contains a username

Example `failed_logins.txt`:

```
elarson
eraab
eraab
tshah
eraab
bmoreno
```

### Rule:
If a user appears 3 or more times, we lock the account.

### 🗂 Step 1: Import and Parse the File
```
with open("failed_logins.txt", "r") as file:
    log_data = file.read()

usernames = log_data.split()
print(usernames)

```

## Why this works:
- .read() → loads the file as one string
- .split() → splits into a list using whitespace (newlines count as whitespace)

Result: usernames becomes structured data you can analyze.

## 🧱 Strategy Before Coding

We need:
- A counter starting at 0
- Loop through the list
- Count matches for current_user
- If counter >= 3 → alert / lock

Think like an analyst, then code.

## 🔁 Core Algorithm Logic

For each username in the log:
    If it matches current_user:
        counter += 1

After loop:
    If counter >= 3:
        ALERT / LOCK
    Else:
        Allow login

### 🧑‍💻 Step 2: Function (Simple + Clear)
def login_check(login_list, current_user):
    counter = 0

    for user in login_list:
        if user == current_user:
            counter += 1

    if counter >= 3:
        print("🚨 ALERT: Account Locked")
    else:
        print("✅ Login Allowed")

### 🧪 Step 3: Test the Function
```
login_check(usernames, "elarson")
login_check(usernames, "eraab")
```

Possible output:

✅ Login Allowed
🚨 ALERT: Account Locked


## 🛡 Real Security Impact
This logic scales into:
- Brute force detection
- Account lockout policies
- SOC alert triggers
- SIEM detections
- Automated response playbooks

---
**Abhishek (ezabyss)**
