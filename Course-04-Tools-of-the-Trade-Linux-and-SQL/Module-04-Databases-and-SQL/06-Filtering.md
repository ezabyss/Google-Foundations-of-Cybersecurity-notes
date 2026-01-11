# 🎯 SQL Filtering: WHERE Clause, LIKE Operator & Wildcards

---

## 🌍 Overview
One of the most powerful features of SQL is its ability to **filter data**. Filtering allows security analysts to extract **specific, relevant records** from large and complex datasets.

Instead of scanning millions of rows, SQL filters let you:
- Focus on suspicious activity
- Investigate incidents efficiently
- Support decisions with accurate evidence

---

## 🔍 How Filtering Helps in Cybersecurity
As a security analyst, you often work with:
- Login attempt logs
- Device inventories
- Patch and update records
- User activity data

Filtering helps you:
- Find login attempts from a specific user
- Identify activity during a specific incident window
- Detect devices running vulnerable software versions

---

### 🧠 SOC Scenario
> During a suspected breach, an analyst filters login attempts  
> to show **only activity during the incident timeframe**.

---

## 🧱 The WHERE Clause
To filter data in SQL, you use the **WHERE** keyword.

- `WHERE` defines the **condition**
- It appears **after FROM**
- It determines which rows are returned

---

### 📌 Example: Exact Match Filtering
If you need to email only employees with the title *IT Staff*:

```sql
SELECT firstname, lastname, title, email
FROM employees
WHERE title = 'IT Staff';
```

📌 This query returns **only rows** where the title column equals `IT Staff`.

⚠️ Remember: The semicolon (`;`) goes **after the filter**.

---

### 🧠 SOC Scenario
> An analyst sends security alerts only to IT staff  
> instead of broadcasting to the entire organization.

---

## 🔧 SQL Operators
An **operator** is a symbol or keyword that performs a comparison.

Common operators used with WHERE:
- `=` → exact match
- `LIKE` → pattern matching

---

## 🔎 Filtering for Patterns
Sometimes, data values are **inconsistent** or **partially known**.

Examples:
- `US` vs `USA`
- `IT Staff` vs `IT Manager`
- Office names like `East-120`, `East-435`

In these cases, pattern filtering is required.

---

## ✨ Wildcards
A **wildcard** is a special character that substitutes for other characters.

SQL commonly uses two wildcards:

| Wildcard | Meaning |
|--------|--------|
| `%` | Matches **any number of characters** |
| `_` | Matches **exactly one character** |

Wildcards can appear:
- At the beginning
- At the end
- In the middle of a string

---

## 🧪 Wildcard Pattern Examples
Applied to the string `'a'`:

| Pattern | Results that could be returned |
|------|-------------------------------|
| `'a%'` | apple123, art, a |
| `'a_'` | as, an, a7 |
| `'a__'` | ant, add, a1c |
| `'%a'` | pizza, Z6ra, a |
| `'_a'` | ma, 1a, Ha |
| `'%a%'` | Again, back, a |
| `'_a_'` | Car, ban, ea7 |

---

## 🔎 The LIKE Operator
To use wildcards, SQL requires the **LIKE** operator.

- `LIKE` replaces `=`
- Used with WHERE
- Searches for **patterns**, not exact matches

---

### 📌 Example: Filtering by Job Title Pattern
To email employees with titles starting with `IT`:

```sql
SELECT lastname, firstname, title, email
FROM employees
WHERE title LIKE 'IT%';
```

📌 This returns:
- IT Staff
- IT Manager

---

### 🧠 SOC Scenario
> A phishing alert is sent only to IT-related roles  
> using a pattern-based filter instead of listing titles manually.

---

## 🧪 Using the Underscore `_` Wildcard
The underscore matches **exactly one character**.

---

### 📌 Example: State Abbreviation Filtering
To find customers in states starting with `N` and having **exactly two letters**:

```sql
SELECT firstname, lastname, state, country
FROM customers
WHERE state LIKE 'N_';
```

📌 This matches:
- NY
- NV
- NS
- NT

---

### 🧠 SOC Scenario
> An analyst filters customer locations  
> to investigate region-specific fraud patterns.

---

## ⚠️ Important Rules
- `=` → exact match only
- `LIKE` → required for wildcards
- `%` → any number of characters
- `_` → exactly one character
- Semicolon ends the query

---

## 🎯 Why This Matters for Security Analysts
SQL filtering allows you to:
- Search millions of records in seconds
- Handle inconsistent data cleanly
- Reduce noise during investigations
- Get precise answers with one query

---

## ✅ Key Takeaways
- Filtering selects only relevant records
- WHERE defines filter conditions
- `=` is for exact matches
- LIKE enables pattern matching
- `%` matches many characters
- `_` matches one character
- Filtering is essential for SOC investigations

---

*✍️ Notes By Abhishek (Ez Abyss)*
