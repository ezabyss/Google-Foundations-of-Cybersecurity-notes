#!/bin/bash

# Go to the projects directory (exit if it fails)
cd /home/researcher2/projects || exit

# Task 1: View permissions (including hidden files)
ls -l
ls -la

# Task 2: Remove write permission for "other" from project_k.txt
chmod o-w project_k.txt

# Restrict project_m.txt so group cannot read or write
chmod g-rw project_m.txt

# Task 3: Remove write permissions from hidden archived file (keep read access)
ls -l .project_x.txt
chmod ug-w .project_x.txt

# Task 4: Restrict drafts directory (remove execute from group)
ls -ld drafts
chmod g-x drafts

# Final verification: show updated permissions
ls -l
ls -la
ls -ld drafts
