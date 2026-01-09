# Lab 05: Add and Manage Users with Linux Commands

## Activity Overview

This lab focuses on authentication and user management in Linux. Authentication is the process of verifying a user’s identity, while proper user and group management ensures that only authorized individuals can access system resources.

As a security analyst, managing users is a critical responsibility. This includes adding new users, assigning appropriate group memberships, managing file ownership, and removing users who no longer require access.

---

## Scenario

A new employee with the username **researcher9** joins the organization. You are responsible for managing this user’s access throughout their lifecycle in the system.

During this lab, you will:

- Add a new user to the system
- Assign the user to a primary group
- Change ownership of a project file
- Add the user to a secondary group
- Remove the user and clean up unused groups

All tasks require superuser privileges, so `sudo` is used for every command.

---

## Tasks Performed

### Task 1: Add a New User
- Created a new user named `researcher9`
- Assigned `research_team` as the user’s primary group

### Task 2: Assign File Ownership
- Changed ownership of `/home/researcher2/projects/project_r.txt` to `researcher9`

### Task 3: Add the User to a Secondary Group
- Added `researcher9` to the `sales_team` group
- Retained `research_team` as the primary group

### Task 4: Delete the User
- Removed `researcher9` from the system
- Deleted the unused group created for the user

---

## Commands Used

All commands executed during this lab are documented in:

- `commands.sh`

---

## Screenshots

Execution screenshots are stored in:

- `screenshots/`

See `screenshots/README.md` for details.

---

## Key Takeaways

- User and group management is essential for enforcing authentication in Linux
- Commands such as `useradd`, `usermod`, `userdel`, and `chown` control user access
- Cleaning up unused users and groups reduces security risks
- Using `sudo` ensures privileged operations are performed securely

---

