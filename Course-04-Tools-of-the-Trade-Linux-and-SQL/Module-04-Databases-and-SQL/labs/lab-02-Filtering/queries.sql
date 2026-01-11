-- SQL Engine: MariaDB

/* =========================
   Task 1: List all organization machines
   ========================= */

-- Retrieve device IDs and operating systems for all machines
SELECT device_id, operating_system
FROM machines;


/* =========================
   Task 2: Retrieve machines with OS 2
   ========================= */

-- Filter machines that use operating system OS 2
SELECT device_id, operating_system
FROM machines
WHERE operating_system = 'OS 2';


/* =========================
   Task 3: List employees in specific departments
   ========================= */

-- Retrieve all employees in the Finance department
SELECT *
FROM employees
WHERE department = 'Finance';

-- Retrieve all employees in the Sales department
SELECT *
FROM employees
WHERE department = 'Sales';


/* =========================
   Task 4: Identify employee machines
   ========================= */

-- Identify the employee assigned to office South-109
SELECT *
FROM employees
WHERE office = 'South-109';

-- Retrieve all employees working in the South building
SELECT *
FROM employees
WHERE office LIKE 'South-%';
