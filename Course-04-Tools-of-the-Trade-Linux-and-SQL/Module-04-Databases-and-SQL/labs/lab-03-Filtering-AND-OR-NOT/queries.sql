/* =========================
   Task 1: Retrieve after-hours failed login attempts
   ========================= */

-- Retrieve failed login attempts after 18:00
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00'
  AND success = 0;


/* =========================
   Task 2: Retrieve login attempts on specific dates
   ========================= */

-- Retrieve login attempts on 2022-05-08 or 2022-05-09
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-08'
   OR login_date = '2022-05-09';


/* =========================
   Task 3: Retrieve login attempts outside of Mexico
   ========================= */

-- Exclude login attempts originating from Mexico
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';


/* =========================
   Task 4: Retrieve employees in Marketing (East building)
   ========================= */

-- Retrieve employees in the Marketing department located in the East building
SELECT *
FROM employees
WHERE department = 'Marketing'
  AND office LIKE 'East-%';


/* =========================
   Task 5: Retrieve employees in Finance or Sales
   ========================= */

-- Retrieve employees in either the Finance or Sales department
SELECT *
FROM employees
WHERE department = 'Finance'
   OR department = 'Sales';


/* =========================
   Task 6: Retrieve employees not in Information Technology
   ========================= */

-- Retrieve employees who are not in the Information Technology department
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
