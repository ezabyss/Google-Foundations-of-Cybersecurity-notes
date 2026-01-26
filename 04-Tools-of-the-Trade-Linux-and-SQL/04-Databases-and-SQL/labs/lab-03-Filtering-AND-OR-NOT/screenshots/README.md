# Screenshots – Filter SQL Queries with AND, OR, and NOT

This directory contains screenshots captured during the execution of the SQL lab **“Filter SQL Queries with AND, OR, and NOT”**, completed using the MariaDB shell.

These screenshots provide **visual evidence** of applying logical operators to retrieve targeted, security-relevant data from the `organization` database.

---

## Screenshot Checklist and Filenames

### Task 1: Retrieve After-Hours Failed Login Attempts
- **task-01-after-hours-failed-logins.png**  
  Shows filtering failed login attempts after 18:00 using the `AND` operator

---

### Task 2: Retrieve Login Attempts on Specific Dates
- **task-02-logins-specific-dates.png**  
  Shows use of the `OR` operator to retrieve login attempts from two dates

---

### Task 3: Retrieve Login Attempts Outside of Mexico
- **task-03-logins-not-mexico.png**  
  Shows use of `NOT` and `LIKE 'MEX%'` to exclude login attempts from Mexico

---

### Task 4: Retrieve Employees in Marketing (East Building)
- **task-04-marketing-east-building.png**  
  Shows filtering employees in the Marketing department located in the East building using `AND` and `LIKE`

---

### Task 5: Retrieve Employees in Finance or Sales
- **task-05-finance-or-sales.png**  
  Shows use of the `OR` operator to retrieve employees from Finance or Sales departments

---

### Task 6: Retrieve Employees Not in IT
- **task-06-not-it-department.png**  
  Shows use of the `NOT` operator to exclude employees in the Information Technology department

---

## Notes

- All screenshots were taken from the **MariaDB SQL shell**
- Each screenshot includes both the SQL query and its output
- Filenames follow a consistent, task-based naming convention
- Screenshots are intended for **documentation and portfolio use**

---

## Purpose

These screenshots demonstrate the ability to:

- Apply logical operators (`AND`, `OR`, `NOT`) in SQL queries
- Combine multiple conditions for precise filtering
- Use pattern matching with `LIKE` and wildcards
- Perform advanced data filtering relevant to security investigations
