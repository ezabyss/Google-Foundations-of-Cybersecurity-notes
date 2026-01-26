# 🧮 Running SQL Queries
* SQL Skills for Security Analysts*

---

## 🌍 Overview
As a security analyst, you will regularly work with **databases** and the tools used to access them. One of the most important of these tools is **SQL**.

In this lesson, you run your **first SQL query**—a task commonly performed in security roles:  
**matching employees to their assigned computers**.

---

## 🔤 What Is SQL?
**SQL (Structured Query Language)** is a programming language used to:
- Create databases
- Interact with databases
- Retrieve and analyze stored data

Most relational databases rely on SQL or a close variation of it.

---

## ❓ What Is a Query?
A **query** is a **request for data** from:
- A single database table
- Or multiple related tables

Queries allow analysts to ask specific questions and receive **consistent, repeatable results**.

---

### 🧠 SOC Scenario
> A security analyst needs to identify which employee is responsible for a compromised device.  
> A single SQL query returns the answer instantly.

---

## 🧱 Basic SQL Query Structure
Every basic SQL query includes **two essential keywords**:

### ✅ `SELECT`
Indicates **which columns** you want returned.

### ✅ `FROM`
Indicates **which table** the data comes from.

---

## 🧪 First SQL Query Example
Suppose the `employees` table contains these columns:
- `employee_id`
- `device_id`
- `username`
- `department`
- `office`

To return only employee IDs and device IDs:

```sql
SELECT employee_id, device_id
FROM employees;
```

📌 Columns are separated by commas.

---

## 🧠 SQL Syntax Notes
- SQL keywords are **not case-sensitive**
- Keywords are capitalized for **readability**
- Queries end with a **semicolon (`;`)**
- Line breaks are optional but recommended

---

## ⭐ Selecting All Columns
To return **every column** in a table, use an asterisk (`*`):

```sql
SELECT *
FROM employees;
```

📌 Known as **“select all”**.

⚠️ Not recommended for very large tables due to performance and readability concerns.

---

## 🧠 SOC Scenario
> During an investigation, an analyst initially views all employee data,  
> then refines queries to focus only on relevant fields.

---

### 📌 Example Query 

```sql
SELECT customerid, city, country
FROM customers;
```

---

## 📐 Organizing Results with `ORDER BY`
Database output is often large and unordered.  
The `ORDER BY` keyword helps organize results.

---

### 🔼 Ascending Order (Default)
```sql
SELECT customerid, city, country
FROM customers
ORDER BY city;
```

- Numbers: smallest → largest
- Text: A → Z

---

### 🔽 Descending Order
Use `DESC` to reverse the order:

```sql
SELECT customerid, city, country
FROM customers
ORDER BY city DESC;
```

- Numbers: largest → smallest
- Text: Z → A

---

### 🧠 SOC Scenario
> An analyst sorts login attempts by timestamp  
> to identify the most recent suspicious activity.

---

## 🧮 Ordering by Multiple Columns
You can sort by more than one column:

```sql
SELECT customerid, city, country
FROM customers
ORDER BY country, city;
```

📌 SQL sorts first by country, then by city within each country.

---

## 🧠 SOC Scenario
> Analysts group activity by country, then city,  
> to identify geographic attack patterns.

---
## ⌨️ Helpful Keyboard Shortcuts
| Shortcut | Action |
|--------|-------|
| CTRL + C | Stop a running command |
| CTRL + V | Paste text |
| CTRL + L | Clear terminal screen |
| CTRL + A | Move cursor to start |
| CTRL + E | Move cursor to end |
| ↑ / ↓ | Navigate command history |
| Tab | Auto-complete |

📌 Inside SQL shells, some shortcuts behave differently.

---
## ✅ Key Takeaways
- `SELECT` and `FROM` are core SQL keywords
- Queries retrieve structured data efficiently
- `ORDER BY` organizes results
- SQL enables fast, repeatable analysis
- These skills form the foundation for advanced SQL queries

---

*✍️ Notes By Abhishek (Ez Abyss)*
