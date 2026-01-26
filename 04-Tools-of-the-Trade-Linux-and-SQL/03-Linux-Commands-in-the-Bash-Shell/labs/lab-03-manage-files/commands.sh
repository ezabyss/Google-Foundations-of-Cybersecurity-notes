#!/bin/bash

# Task 1: Create logs directory and verify
mkdir /home/analyst/logs
ls /home/analyst

# Task 2: Remove temp directory and verify
rmdir /home/analyst/temp
ls /home/analyst

# Task 3: Move Q3patches.txt from notes to reports
cd /home/analyst/notes || exit
mv Q3patches.txt /home/analyst/reports
ls /home/analyst/reports

# Task 4: Remove unused file from notes
rm tempnotes.txt
ls /home/analyst/notes

# Task 5: Create tasks.txt file
touch /home/analyst/notes/tasks.txt
ls /home/analyst/notes

# Task 6: Edit file using nano (manual step)
nano /home/analyst/notes/tasks.txt

# Clear shell after exiting nano
clear

# Verify file contents
cat /home/analyst/notes/tasks.txt
