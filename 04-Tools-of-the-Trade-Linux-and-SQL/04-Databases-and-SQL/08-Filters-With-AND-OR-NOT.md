# 🔗 SQL Filters with AND, OR, and NOT

---

## 🌍 Overview
In real-world security investigations, filtering on a **single condition is rarely enough**.  
Security vulnerabilities often depend on **multiple factors**, such as:

- Operating system
- Installed software
- User location
- Account role or privilege level

To handle these situations, SQL provides **logical operators** that allow you to combine conditions in a single query.

These operators are:
- **AND**
- **OR**
- **NOT**

---

## 🧠 Why Logical Operators Matter in Security
As a security analyst, you may need to:
- Identify machines vulnerable due to **both** OS and software version
- Find users affected by **one of several** conditions
- Exclude systems that are **not** impacted by an issue

Logical operators help you **narrow results precisely** and avoid false positives.

---

## 🔹 Logical Operators Overview

| Operator | Purpose |
|--------|--------|
| AND | Requires **all** conditions to be true |
| OR | Requires **at least one** condition to be true |
| NOT | Excludes records matching a condition |

---

## 🔗 AND Operator
The **AND** operator specifies that **both conditions must be met simultaneously**.

### 🧠 Concept
This is similar to selecting:
> “Only apples that are **large AND fresh**”

Anything that fails either condition is excluded.

---

### 📌 SQL Example (Machines Vulnerability Check)
To find machines running **OS 1** *and* using **Email Client 1**:

```sql
SELECT *
FROM machines
WHERE operating_system = 'OS 1'
AND email_client = 'Email Client 1';
```

📌 Only machines meeting **both conditions** are returned.

---

### 🧠 SOC Scenario
> A vulnerability affects systems **only when**  
> a specific email client is installed on a specific OS.

---

## 🔀 OR Operator
The **OR** operator specifies that **either condition can be met**.

### 🧠 Concept
This is like asking for:
> “Any apple that is **large OR fresh**”

Records that meet **one or both** conditions are included.

---

### 📌 SQL Example (Multiple OS Patch Requirement)
To find machines running **OS 1 or OS 3**:

```sql
SELECT *
FROM machines
WHERE operating_system = 'OS 1'
OR operating_system = 'OS 3';
```

📌 Results include machines running **either OS**.

---

### 🧠 SOC Scenario
> A patch applies to **multiple operating systems**,  
> and all affected systems must be identified.

---

## 🚫 NOT Operator
The **NOT** operator **negates a condition**.

It returns all records that **do not match** the condition.

---

### 🧠 Concept
Instead of listing everything you want,  
you exclude what you **don’t want**.

Example:
> “Give me all fruits that are **NOT apples**”

---

### 📌 SQL Example (Exclude OS from Updates)
To find all machines **not running OS 3**:

```sql
SELECT *
FROM machines
WHERE NOT operating_system = 'OS 3';
```

📌 This returns every machine **except** those using OS 3.

---

### 🧠 SOC Scenario
> OS 3 machines are already patched.  
> Analysts need a list of **everything else**.

---

## 💡 Alternative to NOT
You can also use:
- `<>` (not equal)
- `!=` (not equal)

These are equivalent to NOT.

```sql
WHERE operating_system <> 'OS 3'
```

---

## 🔄 Combining Logical Operators
Logical operators can be combined for **more precise filtering**.

---

### 📌 SQL Example (Exclude Multiple Countries)
To find customers **not** located in the USA **or** Canada:

```sql
SELECT firstname, lastname, email, country
FROM customers
WHERE NOT country = 'Canada'
AND NOT country = 'USA';
```

📌 Both exclusions must be true.

---

### 🧠 SOC Scenario
> A security incident affects **all regions except**  
> the USA and Canada.

---

## ⚠️ Important Notes
- Each condition must be written **fully**, even if using the same column
- Logical operators are evaluated **left to right**
- Parentheses can be used for advanced logic (covered later)

---

## ✅ Key Takeaways
- AND requires **all conditions** to be true
- OR allows **any condition** to be true
- NOT excludes records matching a condition
- Logical operators help target **real security risks**
- Combining operators allows **highly precise filtering**
- These skills are essential for SOC investigations and incident response

---

*✍️ Notes by Abhishek (Ez Abyss)*  
