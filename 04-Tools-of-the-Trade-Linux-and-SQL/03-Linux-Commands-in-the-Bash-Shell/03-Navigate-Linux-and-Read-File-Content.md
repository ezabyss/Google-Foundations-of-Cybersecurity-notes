# 🌳 Navigating the Linux File System & Reading File Content

---

## 🌱 Overview
Learning how to communicate with the Linux operating system is a key milestone for every security analyst. As we continue using the Linux command line, this section focuses on **navigating the Linux file system** and **reading file content**.

Security analysts often work without a graphical user interface (GUI). Instead, they rely on the shell to locate, inspect, and analyze files such as **logs**, **configuration files**, and **access reports**.

---

## 🌳 Understanding the Linux File System (Tree Analogy)
Imagine a **tree**.

- You might notice the **trunk**
- Or the **branches**
- But everything begins with the **roots**

Linux organizes files in a similar way.

---

## 🧠 Filesystem Hierarchy Standard (FHS)
The **Filesystem Hierarchy Standard (FHS)** is the Linux component responsible for organizing data.

Key ideas:
- Everything in Linux is considered a **file**
- Files are organized in a **hierarchical structure**
- All directories branch out from a single starting point

📌 The FHS ensures Linux systems are **consistent and predictable**.

---

## 🌱 Root Directory (`/`)
The **root directory** is the **highest-level directory** in Linux.

- Represented by a single forward slash: `/`
- All other directories branch from it
- Similar to the **roots of a tree**

---

## 📁 File Paths
A **file path** describes the location of a file or directory.

- Levels in the hierarchy are separated by `/`
- Paths trace back to the root

### Example:
```text
/home/analyst/logs
```

Explanation:
- `/` → root directory
- `home` → subdirectory
- `analyst` → user directory
- `logs` → subdirectory inside analyst

---

## 📂 Standard FHS Directories
Below are common directories found directly under the root (`/`):

- `/home` → Home directories for users
- `/bin` → Binary files and executables
- `/etc` → System configuration files
- `/tmp` → Temporary files (commonly targeted by attackers)
- `/mnt` → Mounted storage devices (USBs, drives)

📌 **Security Tip:** `/tmp` is writable by all users and is often abused by attackers.

---

## 👤 User-Specific Directories
Each user has a directory under `/home`.

Example:
```text
/home/analyst
```

Inside a user’s home directory, you may find:
- `logs`
- `projects`
- `reports`

---

## 🔁 Tilde Shortcut (`~`)
The tilde (`~`) represents the **current user’s home directory**.

Example:
```text
/home/analyst/logs
```
Can also be written as:
```text
~/logs
```

---

## 📍 Absolute vs Relative File Paths
### Absolute Path
- Starts from the root (`/`)
- Example:
```text
/home/analyst/projects
```

### Relative Path
- Starts from the current directory
- Uses:
  - `.` → current directory
  - `..` → parent directory

Example:
```text
../projects
```

---

## 🧭 Key Commands for Navigating the File System

---

### 📌 `pwd` — Print Working Directory
Displays your current location.

```bash
pwd
```

Example output:
```text
/home/analyst
```

📌 Returns the **absolute path** of the current directory.

---

### 📌 `whoami` — Identify Current User
```bash
whoami
```

Example output:
```text
analyst
```

---

### 📌 `ls` — List Files and Directories
Displays contents of the current directory.

```bash
ls
```

Example output:
```text
logs  oldreports  projects  reports  updates.txt
```

You can also list another directory:
```bash
ls projects
```

Or using an absolute path:
```bash
ls /home/analyst/projects
```

---

### 📌 `cd` — Change Directory
Used to move between directories.

Navigate to a subdirectory:
```bash
cd logs
```

Navigate using absolute path:
```bash
cd /home/analyst/logs
```

Go up one level:
```bash
cd ..
```

📌 `cd` does not display output when successful.

---

## 📄 Reading File Content in Linux
Security analysts frequently read files to:
- Analyze logs
- Review configuration settings
- Investigate unauthorized access

---

### 📌 `cat` — Display Entire File
```bash
cat updates.txt
```

📌 Displays **all contents** of a file at once.

---

### 📌 `head` — View Beginning of a File
```bash
head updates.txt
```
Displays the **first 10 lines** by default.

Specify number of lines:
```bash
head -n 5 updates.txt
```

---

### 📌 `tail` — View End of a File
```bash
tail updates.txt
```

📌 Useful for reading **recent log entries**.

---

### 📌 `less` — Paginated File Viewing
```bash
less updates.txt
```

Navigation controls inside `less`:
- Space → next page
- `b` → previous page
- ↓ → next line
- ↑ → previous line
- `q` → quit

📌 Ideal for **large files**.

---

## ✅ Key Takeaways
- Linux uses the **Filesystem Hierarchy Standard (FHS)**
- The root directory (`/`) is the starting point
- File paths describe file locations
- `pwd`, `ls`, and `cd` are core navigation commands
- `cat`, `head`, `tail`, and `less` are essential for reading files
- These skills are **critical for security analysts**

---
## Lab Documentation

**📄 Lab README**  
- [Lab 01 – Navigate and Read Files](labs/lab-01-navigate-and-read-files/README.md)

**📸 Execution Screenshots**  
- [Screenshots Folder](labs/lab-01-navigate-and-read-files/screenshots)

**Description**  
This lab demonstrates navigating the Linux file system, locating files, and reading file contents using core Bash commands such as `pwd`, `ls`, `cd`, `cat`, and `head`.

---

*✍️ Notes By Abhishek (Ez Abyss)*
