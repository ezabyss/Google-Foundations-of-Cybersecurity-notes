## Reflection

This lab helped me understand how SQL joins are used to connect related data across multiple tables. In a security investigation, information is often distributed between different tables, and joins make it possible to analyze that data as a complete dataset.

Using an `INNER JOIN` to match employees with their assigned machines showed how shared identifiers such as `device_id` connect records across tables. This type of join is especially useful when analyzing assets tied directly to specific users.

The `LEFT JOIN` and `RIGHT JOIN` queries highlighted how joins can be used to identify gaps in data, such as machines without assigned employees or employees without assigned machines. This is valuable for detecting misconfigurations or incomplete asset assignments.

Finally, joining employee data with login attempt records demonstrated how authentication activity can be linked to user identities during incident investigations. Overall, this lab strengthened my ability to use SQL joins to retrieve meaningful, security-relevant insights from relational databases.
