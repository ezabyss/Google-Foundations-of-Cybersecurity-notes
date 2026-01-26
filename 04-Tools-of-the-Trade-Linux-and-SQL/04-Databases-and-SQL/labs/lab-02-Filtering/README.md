# Lab: Apply Filters to SQL Queries

## Activity Overview

This lab focuses on improving SQL queries by applying filters to retrieve specific data more efficiently. As a security analyst, being able to narrow down results is essential when working with large datasets related to employees, machines, and departments.

In this lab, SQL filtering techniques such as the `WHERE` clause and the `LIKE` operator are used to quickly locate relevant information from a relational database.

---

## Scenario

Your team needs specific information about employees, their machines, and department locations to perform tasks such as system updates, posting privacy notices, and sending alerts about machine issues.

The required data is stored in the following tables:

- `machines`
- `employees`

You are responsible for writing filtered SQL queries to retrieve this information efficiently.

---

## Tasks Performed

### Task 1: List All Organization Machines
- Retrieved a list of all machines and their operating systems
- Selected only the `device_id` and `operating_system` columns from the `machines` table

### Task 2: Retrieve Machines with OS 2
- Used the `WHERE` clause to filter machines running **OS 2**
- Identified machines that require operating system updates

### Task 3: List Employees in Specific Departments
- Filtered employee records to show only those in the **Finance** department
- Modified the query to retrieve employees in the **Sales** department
- Reviewed employee identifiers and department counts

### Task 4: Identify Employee Machines
- Identified the employee assigned to a specific office (`South-109`)
- Used the `LIKE` operator to retrieve all employees working in the **South** building
- Reviewed department information for employees in the affected location

---

## SQL Queries

All SQL commands executed during this lab are documented in:

- `queries.sql`

---

## Screenshots

Execution evidence for this lab is stored in:

- `screenshots/`

See `screenshots/README.md` for details on captured outputs.

---

## Key Takeaways

- The `WHERE` clause allows precise filtering of SQL query results
- The `LIKE` operator is useful for matching patterns in text fields
- Filtering reduces noise and improves efficiency when analyzing data
- SQL filtering is essential for real-world security investigations

---
