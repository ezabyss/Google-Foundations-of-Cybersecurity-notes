# Lab 04: Manage Authorization with Linux Permissions

## Activity Overview
This lab focuses on managing authorization in Linux by examining and modifying file and directory permissions. Authorization determines which users and groups are allowed to access, modify, or execute files and directories.

As a security analyst, configuring proper permissions is critical to protecting sensitive data and preventing unauthorized access to system resources.

---

## Scenario
In this scenario, you are responsible for managing permissions on files and directories located in the `/home/researcher2/projects` directory.

The `researcher2` user belongs to the `research_team` group. You must verify that permissions align with the required access rules and remove any unauthorized access.

You will:
- Examine file and directory permissions
- Identify incorrect permissions
- Modify file permissions using `chmod`
- Manage permissions on hidden files
- Restrict access to a directory

---

## Commands Used
- ls -l – list files with permission details
- ls -la – list all files including hidden files
- chmod – change file and directory permissions
- cd – change directory

---

## Tasks Performed

### Task 1: Check File and Directory Details

Navigate to the projects directory:

    cd /home/researcher2/projects

List permissions of all files and directories:

    ls -l

List permissions including hidden files:

    ls -la

Expected outcome:
- Files are owned by user `researcher2`
- Group owner is `research_team`
- Hidden files are visible when using `ls -la`

---

### Task 2: Change File Permissions

Identify files that allow write permissions for other users.

Remove write permission for others from the affected file:

    chmod o-w project_k.txt

Restrict group permissions on a sensitive file:

    chmod g-rw project_m.txt

Expected outcome:
- Other users cannot write to any files
- Only the owner can read and write `project_m.txt`

---

### Task 3: Change Permissions on a Hidden File

Check permissions of the hidden file:

    ls -l .project_x.txt

Remove write permissions while keeping read access for user and group:

    chmod ug-w .project_x.txt

Expected outcome:
- User and group can read the file
- No user can write to the file

---

### Task 4: Change Directory Permissions

Check permissions of the drafts directory:

    ls -ld drafts

Remove execute permission for the group:

    chmod g-x drafts

Expected outcome:
- Only the `researcher2` user can access the `drafts` directory and its contents

---

## Verification Summary
- Examined file and directory permissions successfully
- Identified and corrected insecure permissions
- Restricted access to sensitive files
- Removed unauthorized access to directories
- Strengthened system authorization controls

---

## Repository Structure

    labs/
    └── lab-04-manage-authorization-linux/
        ├── README.md
        ├── commands.sh
        ├── reflection.md
        └── screenshots/

---

## Notes
- Commands were executed as the `researcher2` user
- Permission changes were applied only where required
