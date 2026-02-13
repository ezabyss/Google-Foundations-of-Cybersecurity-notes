# 🛡 User-to-Device Access Verification Algorithm (Python)

## 📌 Overview

Security analysts often need simple but reliable access verification logic, such as:

- Is the user approved to access the system?
- Did they bring the device assigned to them?

This lab builds a Python algorithm that automates that process using synchronized lists, indexing, and nested conditionals.

---

## 🎯 Skills Demonstrated

- List indexing (positions start at 0)
- Synchronized lists (mapping one list to another by index)
- List operations: `.append()`, `.remove()`, `.index()`
- Membership testing with `in`
- Conditional logic (`if`, `elif`, `else`)
- Nested conditionals for decision trees
- Functions to automate security workflows

---

## 🧪 Scenario

You are a security analyst responsible for connecting approved users to their assigned devices.

The lists are synchronized:

- `approved_users[i]` corresponds to `approved_devices[i]`

That alignment allows you to verify whether a username and device ID match.

---

## ▶️ How to Run

```bash
python3 login_algorithm.py
```

## 🧩 What This Lab Does
1) Explore List Indexing

Displays the username and device at the same index.

## 2) Add a New Approved User

Uses .append() to add a new username and device ID while keeping lists synchronized.

## 3) Remove a Departed User

Uses .remove() to revoke access by removing the user and device from the approved lists.

## 4) Verify User Approval

Checks membership with username in approved_users.

## 5) Find Assigned Device Using .index()

Finds the index of the username and uses that index to pull the matching device ID.


## 6) Automated Login Function

Implements login(username, device_id) using nested conditionals:
If the user is not approved → deny access
If approved → verify device matches the assigned one

## ✅ Sample Test Cases

- The script runs these scenarios:
- Approved user + correct device
- Approved user + incorrect device
- Unapproved user + any device


## 🛡 Real-World Security Relevance

This logic supports workflows like:
- Front-desk security validation for issued laptops
- SOC triage playbooks (identity + asset validation)
- Inventory-based access checks
- Basic identity/device pairing used in automation scripts

## 🧠 Key Takeaways

- Indexing starts at 0 in Python.
- .append() adds to the end of a list.
- .remove() deletes a specific value from a list.
- .index() finds where a value is located.
- Synchronized lists can represent mappings (user → device).
- Functions turn repeated logic into reusable security automation.
---

✍️ Notes By Abhishek (Ez Abyss)
