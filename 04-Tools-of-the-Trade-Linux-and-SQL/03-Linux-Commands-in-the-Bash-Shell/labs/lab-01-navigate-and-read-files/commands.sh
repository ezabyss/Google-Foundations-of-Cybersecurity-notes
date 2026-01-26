#!/bin/bash

# Task 1: Display current directory and list contents
pwd
ls

# Task 2: Navigate to reports directory and list contents
cd /home/analyst/reports || exit
ls

# Task 3: Navigate to users directory and read user report
cd /home/analyst/reports/users || exit
ls
cat Q1_added_users.txt

# Task 4: Navigate to logs directory and inspect log file
cd /home/analyst/logs || exit
ls
head server_logs.txt

# || exit ensures the script stops immediately if a critical command fails, preventing incorrect or misleading execution.
