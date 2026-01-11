/* =========================
   Task 1: Match employees to their machines
   ========================= */

-- Review all machines (baseline)
SELECT *
FROM machines;

-- INNER JOIN to match employees to machines using device_id
SELECT *
FROM machines
INNER JOIN employees
ON machines.device_id = employees.device_id;


/* =========================
   Task 2: Return more data with LEFT and RIGHT joins
   ========================= */

-- LEFT JOIN: return all machines and any matching employees
-- Includes machines that are not assigned to any employee
SELECT *
FROM machines
LEFT JOIN employees
ON machines.device_id = employees.device_id;

-- RIGHT JOIN: return all employees and any matching machines
-- Includes employees that do not have a machine assigned
SELECT *
FROM machines
RIGHT JOIN employees
ON machines.device_id = employees.device_id;


/* =========================
   Task 3: Retrieve login attempt data
   ========================= */

-- INNER JOIN to retrieve login attempts made by employees
-- Join employees and log_in_attempts using the username column
SELECT *
FROM employees
INNER JOIN log_in_attempts
ON employees.username = log_in_attempts.username;
