# Lab 02: Filter Information with grep
---

## Activity Overview
This lab focuses on filtering and searching information in Linux using the grep command and piping. The ability to efficiently search files and file contents is an essential skill for security analysts when reviewing logs, analyzing user data, and locating relevant system information.

---

## Scenario
In this scenario, you are working as a security analyst and need to locate specific information contained in server logs and user report files. You are also required to find files based on name patterns.

We will:
- Search log files for error messages
- Locate files containing specific strings in their names
- Search file contents for specific users and departments

These tasks simulate real-world workflows used in security monitoring and investigations.

---

## Commands Used
- grep  – search for specific text patterns
- ls    – list files in a directory
- cd    – change directory
- pipe (|) – pass output from one command to another

---

## Tasks Performed

### Task 1: Search for Error Messages in a Log File

Navigate to the logs directory:

    cd /home/analyst/logs

Search the server log file for error messages:

    grep error server_logs.txt

Expected outcome:
- Only lines containing the word "error" are displayed
- Error messages are isolated from the log file

---

### Task 2: Find Files Containing Specific Strings

Navigate to the users reports directory:

    cd /home/analyst/reports/users

List files that contain "Q1" in their names:

    ls | grep Q1

Expected outcome:
- Only files containing "Q1" in their filenames are displayed

List files that contain "access" in their names:

    ls | grep access

Expected outcome:
- Only files containing the word "access" are displayed

---

### Task 3: Search File Contents

List files in the users directory:

    ls

Search for a specific username in the deleted users file:

    grep jhill Q2_deleted_users.txt

Expected outcome:
- Confirms whether the username "jhill" exists in the file

Search for users added to the Human Resources department:

    grep "Human Resources" Q4_added_users.txt

Expected outcome:
- Displays users added to the Human Resources department in quarter 4

---

## Summary
- Successfully filtered log data using grep
- Used piping to search filenames efficiently
- Located specific user information within files

---

## Repository Structure

    labs/
    └── lab-02-filter-with-grep/
        ├── README.md
        ├── commands.sh
        ├── reflection.md
        └── screenshots/

---

## Notes
- Commands were executed as the analyst user
- All searches were performed using the Linux Bash shell
- Screenshots provide evidence of successful execution
