#!/bin/bash

# Task 1: Add a new user named researcher9
sudo useradd researcher9

# Assign researcher9 to the research_team group as the primary group
sudo usermod -g research_team researcher9

# Task 2: Change ownership of the project file to researcher9
sudo chown researcher9 /home/researcher2/projects/project_r.txt

# Task 3: Add researcher9 to the sales_team as a secondary group
# -a appends the group without removing existing group memberships
# -G specifies the supplementary group
sudo usermod -aG sales_team researcher9

# Verify user details before deletion
# This checks the user ID, primary group, and supplementary groups
id researcher9

# Task 4: Delete the user researcher9 from the system
sudo userdel researcher9

# Remove the unused group created for researcher9
sudo groupdel researcher9
