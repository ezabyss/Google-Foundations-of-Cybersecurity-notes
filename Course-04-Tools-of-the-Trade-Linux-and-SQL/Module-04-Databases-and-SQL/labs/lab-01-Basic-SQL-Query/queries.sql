/* =========================
   Task 1: Retrieve employee device data
   ========================= */

-- 1) Return all device information from the machines table
SELECT *
FROM machines;

-- 2) Return only device_id and email_client from the machines table
SELECT device_id, email_client
FROM machines;

-- 3) Return device_id, operating_system, and OS_patch_date from the machines table
SELECT device_id, operating_system, OS_patch_date
FROM machines;


/* =========================
   Task 2: Investigate login activity
   ========================= */

-- 1) Return event_id and country for login attempts
SELECT event_id, country
FROM log_in_attempts;

-- 2) Return username, login_date, and login_time for login attempts
SELECT username, login_date, login_time
FROM log_in_attempts;

-- 3) Return all login attempt data
SELECT *
FROM log_in_attempts;


/* =========================
   Task 3: Order login attempts data
   ========================= */

-- 1) Order login attempts by login_date
SELECT *
FROM log_in_attempts
ORDER BY login_date;

-- 2) Order login attempts by login_date and then login_time
SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
