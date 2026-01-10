# 🗄️ Databases & Relational Database Basics

---

## 🌍 Overview
Our modern world is driven by **data**. Almost every important decision—business, security, or operational—is guided by data analysis.

When working with **large amounts of data**, we need a way to:
- Store it efficiently
- Keep it organized
- Access and process it quickly

The solution is **databases**.

---

## 📊 What Is a Database?
A **database** is an **organized collection of data** designed for efficient storage, retrieval, and processing.

Databases are often compared to **spreadsheets**, but they serve very different purposes.

---

## 📈 Databases vs Spreadsheets
| Spreadsheets | Databases |
|-------------|-----------|
| Designed for individuals or small teams | Designed for many users |
| Limited data size | Can store massive datasets |
| Manual analysis | Supports automated queries |
| Limited concurrency | Multiple users simultaneously |

📌 Spreadsheets are convenient, but databases are **built for scale and performance**.

---

### 🧠 SOC Scenario
> A security analyst needs to review millions of login attempts.  
> A spreadsheet crashes—but a database handles the query instantly.

---

## 🔐 Why Databases Matter in Security
As a security analyst, you will frequently work with databases that store:
- Login attempts
- Software update records
- Endpoint and asset inventories
- User-device relationships

📌 Databases allow analysts to **quickly identify threats and patterns**.

---

## 🧱 Types of Databases
There are many ways to structure databases, but in this course, the focus is on:

### ✅ Relational Databases
A **relational database** is a structured database that stores data in **tables that relate to one another**.

---

## 📋 Tables in Relational Databases
A **table** organizes data into:
- **Columns (fields)**
- **Rows (records)**

---

### 📌 Columns (Fields)
Columns define **what kind of data** is stored.

Example fields in an `employees` table:
- `employee_id`
- `device_id`
- `username`
- `department`

---

### 📌 Rows (Records)
Rows store **actual data values** for each column.

Example:
```text
employee_id: 1000
department: marketing
```

Each row represents **one unique entity**, such as an employee or device.

---

### 🧠 SOC Scenario
> Each row in a login table represents a **single authentication attempt**.  
> Analysts investigate suspicious rows, not entire tables.

---

## 🔗 Relationships Between Tables
Relational databases usually contain **multiple tables**.

Tables can be connected if they share a **common column**.

Example:
- `employees` table
- `machines` table

Both contain:
```text
employee_id
```

This shared column allows data to be **linked across tables**.

---

## 🔑 Keys in Relational Databases
The columns used to connect tables are called **keys**.

There are **two main types** of keys.

---

## 🗝️ Primary Key
A **primary key**:
- Uniquely identifies each row in a table
- Must contain **unique values**
- Cannot contain **NULL or empty values**
- Only **one primary key per table**

Example:
```text
employee_id
```

Each employee has a unique ID.

---

### 🧠 SOC Scenario
> During an investigation, an analyst uses the primary key to  
> **identify one exact user record** without ambiguity.

---

## 🔗 Foreign Key
A **foreign key**:
- Exists in a different table
- References a **primary key** in another table
- Can contain duplicates
- Can contain NULL values
- A table can have **multiple foreign keys**

Example:
```text
employee_id (in machines table)
```

This links each machine to its assigned employee.

---

### 🧠 SOC Scenario
> A compromised device is identified.  
> The foreign key allows analysts to trace the device **back to its owner**.

---

## 🧠 Primary Key vs Foreign Key
| Primary Key | Foreign Key |
|------------|------------|
| Unique | Can repeat |
| Cannot be NULL | Can be NULL |
| Identifies rows | Connects tables |
| One per table | Multiple allowed |

---

## 🔐 Security Importance of Relationships
Relational structure allows analysts to:
- Correlate users with devices
- Link logins to machines
- Trace activity across systems

📌 This is essential for **incident response and threat hunting**.

---

## 🚀 Preparing for SQL
Now that you understand:
- Databases
- Tables
- Rows and columns
- Primary and foreign keys

You are ready to learn **SQL**, the language used to interact with databases.

SQL allows you to:
- Query data
- Filter results
- Combine tables
- Analyze security events efficiently

---

## ✅ Key Takeaways
- Databases store large amounts of structured data
- Relational databases use tables
- Columns define fields; rows store records
- Tables connect through keys
- Primary keys uniquely identify rows
- Foreign keys link related tables
- Relational structure supports security investigations

---

*✍️ Notes By Abhishek (Ez Abyss)*
