# Lab: Filter SQL Queries with AND, OR, and NOT

---

## Activity Overview

This lab focuses on using logical operators to create more advanced SQL filters. As a security analyst, investigations often require filtering data based on multiple conditions or excluding certain results to narrow down relevant information.

In this lab, SQL queries are enhanced using the `AND`, `OR`, and `NOT` operators to retrieve precise and security-relevant data from a relational database.

---

## Scenario

Your team needs to investigate login activity and employee information to identify potential security issues and perform system updates.

The required data is stored in the following database tables:

- `log_in_attempts`
- `employees`

You are responsible for retrieving targeted information by applying multiple filtering conditions to SQL queries.

---

## Tasks Performed

### Task 1: Retrieve After-Hours Failed Login Attempts
- Filtered login attempts that occurred after business hours
- Retrieved only failed login attempts using the `AND` operator

### Task 2: Retrieve Login Attempts on Specific Dates
- Retrieved login attempts from two specific dates
- Used the `OR` operator to combine multiple date conditions

### Task 3: Retrieve Login Attempts Outside of Mexico
- Filtered out login attempts originating from Mexico
- Used the `NOT` and `LIKE` operators with wildcard matching

### Task 4: Retrieve Employees in Marketing
- Retrieved employees in the **Marketing** department
- Filtered employees located in the **East** building using pattern matching
- Used `AND` and `LIKE` operators together

### Task 5: Retrieve Employees in Finance or Sales
- Retrieved employees belonging to either the **Finance** or **Sales** departments
- Used the `OR` operator to combine department conditions

### Task 6: Retrieve Employees Not in IT
- Identified employees who are not part of the **Information Technology** department
- Used the `NOT` operator to exclude specific records

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

- Logical operators allow precise filtering of SQL query results
- `AND` combines multiple conditions that must all be true
- `OR` retrieves records matching any specified condition
- `NOT` excludes unwanted records from query results
- Advanced filtering is essential for effective security investigations

---
