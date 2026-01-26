# Lab 01: Navigate the Linux File System and Read Files


## Activity Overview
This lab focuses on navigating the Linux file system and reading file contents using the Bash shell. These skills are essential for working in Linux environments where a graphical user interface (GUI) is not available.

As a security analyst, the ability to locate files, navigate directories, and inspect logs is critical when investigating incidents, auditing systems, or analyzing reports remotely.

---

## Scenario
In this scenario, you are required to locate and analyze files stored within the /home/analyst directory using the Linux command line.

You will:
- Identify your current working directory
- List directory contents
- Navigate through subdirectories
- Read text files
- Inspect log files for relevant information

---

## Commands Used
- pwd  – display current working directory
- ls   – list files and directories
- cd   – change directory
- cat  – display full file contents
- head – display the first lines of a file

---

## Tasks Performed

### Task 1: Get Current Directory Information

    pwd

    ls

Expected outcome:
- The current directory is /home/analyst
- Files and directories in the working directory are displayed

---

### Task 2: Navigate to the Reports Directory

    cd /home/analyst/reports

    ls

Expected outcome:
- The users subdirectory is listed

---

### Task 3: Locate and Read a User Report File

    cd /home/analyst/reports/users

    ls

    cat Q1_added_users.txt

Expected outcome:
- User information such as usernames, departments, and employee IDs is displayed

---

### Task 4: Navigate to the Logs Directory and Inspect Log Data

    cd /home/analyst/logs

    ls

    head server_logs.txt

Expected outcome:
- The first 10 lines of the log file are displayed
- Warning messages can be identified from the output

---

## Notes
- Commands were executed as the analyst user
- Files were accessed within the /home/analyst directory
- Screenshots provide execution evidence for each task
