# Lab 03: Manage Files with Linux Commands

## Activity Overview
This lab focuses on managing directories and files in a Linux environment using core Bash commands. Tasks include creating and removing directories, moving and deleting files, and editing files using the nano text editor.

As a security analyst, maintaining an organized file structure and accurately documenting changes is essential for managing data securely and efficiently.

---

## Scenario
In this scenario, you are required to organize the `/home/analyst` directory by modifying its structure and updating the files it contains.

You will:
- Create a new directory
- Remove an unused directory
- Move and delete files
- Create a new file
- Edit a file to document completed tasks

These tasks reflect common file management responsibilities in security and system administration roles.

---


## Commands Used
- mkdir – create directories
- rmdir / rm – remove directories and files
- mv – move files
- touch – create empty files
- nano – edit text files
- ls – list directory contents
- clear – clean up the shell display

---

## Tasks Performed

### Task 1: Create a New Directory

    mkdir /home/analyst/logs
    ls /home/analyst

Expected outcome:
- A new directory named `logs` is created

---

### Task 2: Remove an Unused Directory

    rmdir /home/analyst/temp
    ls /home/analyst

Expected outcome:
- The `temp` directory is removed

---

### Task 3: Move a File

    cd /home/analyst/notes
    mv Q3patches.txt /home/analyst/reports
    ls /home/analyst/reports

Expected outcome:
- `Q3patches.txt` is moved to the reports directory

---

### Task 4: Remove a File

    rm /home/analyst/notes/tempnotes.txt
    ls /home/analyst/notes

Expected outcome:
- `tempnotes.txt` is removed

---

### Task 5: Create a New File

    touch /home/analyst/notes/tasks.txt
    ls /home/analyst/notes

Expected outcome:
- A new file named `tasks.txt` is created

---

### Task 6: Edit a File Using nano

    nano /home/analyst/notes/tasks.txt

Text added to the file:

    Completed tasks
    1. Managed file structure in /home/analyst

Exit and save the file, then clean the shell:

    clear

Verify file contents:

    cat /home/analyst/notes/tasks.txt

Expected outcome:
- The file contains the documented task information

---

## Summary
- Created and removed directories successfully
- Moved and deleted files correctly
- Created and edited files using nano
- Verified file contents after editing
- Maintained an organized directory structure

---

## Repository Structure

    labs/
    └── lab-03-manage-files-linux/
        ├── README.md
        ├── commands.sh
        ├── reflection.md
        └── screenshots/

---
