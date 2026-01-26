# ⏱️ SQL Filtering with Numeric & Date/Time Data

---

## 🌍 Overview
SQL filtering is not limited to text (string) data.  
As a security analyst, you will frequently work with:

- **Numeric data** (counts, volumes, totals)
- **Date and time data** (timestamps, patch dates, login times)

Being able to filter using these data types allows you to **detect suspicious behavior, identify vulnerabilities, and support incident response**.

---

## 🧱 Common Data Types in Databases

### 🔤 String Data
String data is an **ordered sequence of characters**:
- Letters
- Numbers
- Symbols

Examples:
- Usernames: `analyst10`
- Office names: `East-120`
- Country codes: `US`, `USA`

---

### 🔢 Numeric Data
Numeric data consists of **numbers** that support math operations.

Examples:
- Number of login attempts
- Count of failed authentications
- Volume of data transferred

📌 Mathematical operations (addition, comparison) can be applied.

---

### ⏰ Date and Time Data
Date and time data represents **when events occur**.

Examples:
- Login timestamps
- Patch installation dates
- Connection durations

📌 Logs almost always include timestamps.

---

### 🧠 SOC Scenario
> During an incident, an analyst filters login attempts  
> to show only activity **after business hours**.

---

## 🎯 Why Filtering Numbers & Dates Matters in Security
Security analysts often need to:
- Identify activity outside normal hours
- Find systems missing recent patches
- Analyze spikes in login attempts
- Track activity within a specific timeframe

---

## 🔧 Comparison Operators
To filter numeric and date/time data, SQL uses **comparison operators**.

| Operator | Meaning |
|--------|--------|
| `<` | less than |
| `>` | greater than |
| `=` | equal to |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |
| `<>` | not equal to |
| `!=` | not equal to (alternative) |

---

## 🧪 Filtering with Comparison Operators
Operators are used inside the **WHERE clause**.

---

### 📌 Example: Filtering by Time
To find login attempts **after 6 PM**:

```sql
SELECT *
FROM log_in_attempts
WHERE time > '18:00';
```

📌 `18:00` represents 6:00 PM in SQL time format.

---

### 🧠 SOC Scenario
> Login attempts after hours may indicate  
> **credential abuse or automated attacks**.

---

## 📌 Inclusive vs Exclusive Operators
Some operators **include** the comparison value, while others **exclude** it.

- **Exclusive operators**: `<`, `>`
- **Inclusive operators**: `<=`, `>=`

---

### 📌 Example
```sql
SELECT firstname, lastname, birthdate
FROM employees
WHERE birthdate > '1970-01-01';
```

📌 Returns employees born **after**, but **not on**, January 1, 1970.

If `>=` were used instead, January 1, 1970 would be included.

---

## 🔁 The BETWEEN Operator
The **BETWEEN** operator filters values **within a range**.

- Works with **numbers**
- Works with **dates and times**
- Is **inclusive** on both ends

---

### 📌 Example: Patch Date Range
To find machines patched between March 1 and September 1, 2021:

```sql
SELECT *
FROM machines
WHERE OS_patch_date BETWEEN '2021-03-01' AND '2021-09-01';
```

📌 Both dates are included in the results.

---

### 🧠 SOC Scenario
> An analyst checks which machines were patched  
> during a specific vulnerability disclosure window.

---

## ⚠️ Important Syntax Rules
- **Strings, dates, and times** → use quotation marks `' '`
- **Numbers** → do **not** use quotation marks

✅ Correct:
```sql
WHERE time > '18:00'
WHERE OS_patch_date BETWEEN '2021-03-01' AND '2021-09-01'
WHERE login_attempts > 5
```

---

## 🎯 Why This Skill Is Powerful
Using numeric and date/time filtering allows you to:
- Detect anomalies quickly
- Narrow investigations precisely
- Reduce noise in massive datasets
- Perform timeline-based analysis

---

## ✅ Key Takeaways
- SQL supports string, numeric, and date/time data
- Numeric data supports mathematical comparison
- Date/time data is critical for log analysis
- Comparison operators filter precise values
- Inclusive (`>=`, `<=`) vs exclusive (`>`, `<`) matters
- BETWEEN filters within a range and is inclusive
- Quotes are required for strings and dates, not numbers

---

*✍️ Notes By Abhishek (Ez Abyss)*
