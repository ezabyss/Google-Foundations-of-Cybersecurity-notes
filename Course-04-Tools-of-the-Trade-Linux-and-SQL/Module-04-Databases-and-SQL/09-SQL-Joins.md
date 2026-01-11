# SQL Joins

Joining tables is useful when information is spread across multiple tables.
For example, one table might describe operating system vulnerabilities, while another lists machines and their operating systems.
By joining these tables, a security analyst can identify vulnerable machines.

---

## Table and Column Qualification

When querying multiple tables, column names can appear in more than one table.
SQL needs to know exactly which column you are referring to.

To avoid ambiguity, SQL uses the following format:

    table_name.column_name

Example:

    employees.employee_id
    machines.employee_id

---

## Keys Used in Joins

Primary key:
- Uniquely identifies each row in a table
- Cannot contain duplicate or NULL values

Foreign key:
- References a primary key in another table
- Can contain duplicate or NULL values

---

## INNER JOIN

An INNER JOIN returns only rows where there is a matching value in both tables.

Syntax:

    SELECT *
    FROM employees
    INNER JOIN machines
    ON employees.device_id = machines.device_id;

---

## LEFT JOIN

Returns all records from the left table and matching records from the right table.

    SELECT *
    FROM employees
    LEFT JOIN machines
    ON employees.device_id = machines.device_id;

---

## RIGHT JOIN

Returns all records from the right table and matching records from the left table.

    SELECT *
    FROM employees
    RIGHT JOIN machines
    ON employees.device_id = machines.device_id;

---

## FULL OUTER JOIN

Returns all records from both tables.
Missing matches are filled with NULL values.

    SELECT *
    FROM employees
    FULL OUTER JOIN machines
    ON employees.device_id = machines.device_id;

---

## Key Takeaways

- INNER JOIN returns only matching rows
- LEFT JOIN returns all rows from the first table
- RIGHT JOIN returns all rows from the second table
- FULL OUTER JOIN returns all rows from both tables
- Column qualification prevents ambiguity
