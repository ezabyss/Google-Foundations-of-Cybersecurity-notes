# Lab: Join Tables in SQL (INNER, LEFT, RIGHT)

- **SQL Engine:** MariaDB

---

## Activity Overview

This lab focuses on using SQL joins to retrieve information from more than one table. In real security investigations, data is often distributed across multiple related tables. SQL joins help connect these tables using shared columns, allowing analysts to build a complete view of activity.

In this lab, you will use:

- `INNER JOIN` to return only matching records from both tables
- `LEFT JOIN` to return all records from the left table (even without matches)
- `RIGHT JOIN` to return all records from the right table (even without matches)

---

## Scenario

A recent security incident compromised some machines. You need to retrieve investigation data from multiple tables in the `organization` database.

The required information is stored in these tables:

- `machines`
- `employees`
- `log_in_attempts`

You will use joins to connect related records and retrieve the necessary data.

---

## Tasks Performed

### Task 1: Match Employees to Their Machines
- Reviewed machine records from the `machines` table
- Used an `INNER JOIN` to match employees to machines using the shared `device_id` column

### Task 2: Return More Data with LEFT and RIGHT Joins
- Used a `LEFT JOIN` to return all machines and any matching employees (including unassigned machines)
- Used a `RIGHT JOIN` to return all employees and any matching machines (including employees without assigned machines)

### Task 3: Retrieve Login Attempt Data
- Used an `INNER JOIN` to list all login attempts made by employees
- Joined `employees` and `log_in_attempts` using the shared `username` column

---

## SQL Queries

All SQL commands executed during this lab are documented in:

- `queries.sql`

---

## Screenshots

Execution evidence for this lab is stored in:

- `screenshots/`

See `screenshots/README.md` for screenshot filenames and task mapping.

---

## Key Takeaways

- Joins allow combining related data across multiple tables
- `INNER JOIN` returns only matching records from both tables
- `LEFT JOIN` helps identify machines without assigned employees
- `RIGHT JOIN` helps identify employees without assigned machines
- Joining login attempts to employee records supports incident investigations

---
