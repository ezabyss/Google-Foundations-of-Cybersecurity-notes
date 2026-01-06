#!/bin/bash

# Task 1: Navigate to logs directory and search for error messages
cd /home/analyst/logs || exit
grep error server_logs.txt

# Task 2: Navigate to users reports directory and filter filenames
cd /home/analyst/reports/users || exit

# List files containing "Q1" in their names
ls | grep Q1

# List files containing "access" in their names
ls | grep access

# Task 3: Search file contents for specific information

# Search for username jhill in deleted users file
grep jhill Q2_deleted_users.txt

# Search for users added to the Human Resources department
grep "Human Resources" Q4_added_users.txt
