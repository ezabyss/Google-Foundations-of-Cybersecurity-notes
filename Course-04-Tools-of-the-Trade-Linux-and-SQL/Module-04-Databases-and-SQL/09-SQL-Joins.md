# 🔗 SQL Joins: Combining Tables for Security Analysis

---

## 🌍 Overview
As a security analyst, the data you need is often **spread across multiple tables**.  
SQL joins allow you to **combine related tables** so you can answer real security questions.

For example:
- One table lists **employees**
- Another lists **machines and operating systems**
- Joining them lets you identify **which employees are using vulnerable machines**

---

## 🧠 Why Joins Matter in Security
Joins help answer questions like:
- Which users are using **vulnerable operating systems**?
- Which machines are **unassigned**?
- Which employees **don’t have a device**?
- Which devices **aren’t linked to a user**?

Without joins, this information would be fragmented.

---

## 🧩 Table and Column Qualification
When querying **multiple tables**, column names can appear in more than one table.

To avoid ambiguity, SQL uses this format:

```
table_name.column_name
```

**Example:**
- `employees.employee_id`
- `machines.employee_id`

This tells SQL **exactly which column** you mean.

---

## 🔑 Keys Used in Joins
Joins rely on shared columns:

- **Primary key**: uniquely identifies each row in a table  
  - Example: `employee_id` in the `employees` table
- **Foreign key**: references a primary key in another table  
  - Example: `employee_id` in the `machines` table

---

## 🔹 INNER JOIN
### What it does
`INNER JOIN` returns **only rows where there is a match in both tables**.

If there is **no matching value**, the row is excluded.

### 📌 Syntax
```sql
SELECT username, office, operating_system
FROM employees
INNER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### 🧠 SOC Scenario
You want to identify which employees are actively using machines  
so you can check their systems for vulnerabilities.

Only employees with assigned machines appear.

### ⚠️ NULL Values in Joins
If a value does not exist, SQL uses `NULL`.

Examples:
- A machine not assigned to an employee
- An employee without a machine

`INNER JOIN` excludes these rows.

---

## 🔹 LEFT JOIN
### What it does
`LEFT JOIN` returns:
- All rows from the **left (first) table**
- Only matching rows from the **right table**
- `NULL` where no match exists

### 📌 Syntax
```sql
SELECT *
FROM employees
LEFT JOIN machines
ON employees.employee_id = machines.employee_id;
```

### 🧠 SOC Scenario
You want a list of **all employees**,  
including those who don’t yet have a machine assigned.

Employees without machines appear with `NULL` machine fields.

---

## 🔹 RIGHT JOIN
### What it does
`RIGHT JOIN` returns:
- All rows from the **right (second) table**
- Only matching rows from the **left table**
- `NULL` where no match exists

### 📌 Syntax
```sql
SELECT *
FROM employees
RIGHT JOIN machines
ON employees.employee_id = machines.employee_id;
```

### 🧠 SOC Scenario
You want a list of **all machines**,  
including machines not assigned to any employee.

Unassigned machines appear with `NULL` employee data.

---

## 🔁 LEFT vs RIGHT JOIN (Important Tip)
`LEFT JOIN` and `RIGHT JOIN` can return the **same result**  
if you reverse the table order.

### Example
```sql
SELECT *
FROM machines
RIGHT JOIN employees
ON employees.employee_id = machines.employee_id;
```

⬆️ This produces the same result as a `LEFT JOIN` with `employees` first.

---

## 🔹 FULL OUTER JOIN
### What it does
`FULL OUTER JOIN` returns:
- All rows from **both tables**
- `NULL` wherever no match exists

This is like **fully merging** two tables.

### 📌 Syntax
```sql
SELECT *
FROM employees
FULL OUTER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### 🧠 SOC Scenario
During an audit, you need to see:
- Employees without machines
- Machines without employees  

In one complete report.

---

## 🧠 Visual Summary (Conceptual)

| Join Type | Rows Returned |
|---------|---------------|
| INNER JOIN | Only matching rows |
| LEFT JOIN | All left + matching right |
| RIGHT JOIN | All right + matching left |
| FULL OUTER JOIN | All rows from both tables |

---

## ✅ Key Takeaways
- Joins allow SQL to combine related data
- `INNER JOIN` returns only matches
- `LEFT JOIN` keeps all records from the first table
- `RIGHT JOIN` keeps all records from the second table
- `FULL OUTER JOIN` keeps everything
- `NULL` indicates missing or unmatched data
- Joins are essential for real SOC investigations

---
*✍️Notes By Abhishek (Ez Abyss)*
