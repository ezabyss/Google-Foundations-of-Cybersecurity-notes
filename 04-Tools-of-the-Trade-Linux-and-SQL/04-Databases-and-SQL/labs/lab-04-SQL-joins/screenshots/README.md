# Screenshots – Join Tables in SQL (INNER, LEFT, RIGHT)

This directory contains screenshots captured during the execution of the SQL lab **“Join Tables in SQL (INNER, LEFT, RIGHT)”**, completed using the MariaDB shell.

These screenshots provide **visual evidence** of successfully joining multiple tables to retrieve security-relevant information from the `organization` database.

---

## Screenshot Checklist and Filenames

### Task 1: Match Employees to Their Machines
- **task-01-inner-join-employees-machines.png**  
  Shows an `INNER JOIN` between the `machines` and `employees` tables using the `device_id` column

---

### Task 2: Return More Data with LEFT and RIGHT Joins
- **task-02-left-join-machines-employees.png**  
  Shows a `LEFT JOIN` returning all machines, including those without assigned employees

- **task-02-right-join-machines-employees.png**  
  Shows a `RIGHT JOIN` returning all employees, including those without assigned machines

---

### Task 3: Retrieve Login Attempt Data
- **task-03-inner-join-employees-login-attempts.png**  
  Shows an `INNER JOIN` between the `employees` and `log_in_attempts` tables using the `username` column

---

## Notes

- All screenshots were taken from the **MariaDB SQL shell**
- Each screenshot includes both the SQL query and its output
- Filenames follow a consistent, task-based naming convention
- Screenshots are intended for **documentation and portfolio use**

---
