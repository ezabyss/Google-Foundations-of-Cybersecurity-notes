# Lab: Perform a SQL Query

## Lab Information

- **Database:** organization
- **SQL Engine:** MariaDB

---

## Activity Overview

This lab builds foundational SQL skills by retrieving and organizing data from a relational database. As a security analyst, querying databases is essential for investigating system activity, identifying outdated assets, and detecting unusual login behavior.

In this activity, SQL queries are executed using the MariaDB shell to extract information from multiple tables and organize results using sorting techniques.

---

## Scenario

You are responsible for identifying employee devices that require updates and investigating login activity for potential anomalies.

The required data is stored in the following database tables:

- `machines`
- `log_in_attempts`

Using SQL, you will retrieve relevant information and organize it to support security analysis.

---

## Tasks Performed

### Task 1: Retrieve Employee Device Data
- Retrieved all device information from the `machines` table
- Selected specific columns such as `device_id`, `email_client`, `operating_system`, and `OS_patch_date`
- Reviewed patch dates to identify devices that may require updates

### Task 2: Investigate Login Activity
- Queried login attempts to review authentication activity
- Retrieved usernames, login dates, login times, and locations
- Examined login attempts for unusual geographic access

### Task 3: Order Login Attempts Data
- Sorted login attempt records by date using `ORDER BY`
- Further refined results by ordering login times within each date
- Improved readability and analysis of authentication patterns

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

- SQL allows efficient retrieval of security-relevant data
- Selecting specific columns improves query focus and performance
- Sorting data helps reveal patterns and anomalies
- Database analysis is a core skill for security investigations

---

