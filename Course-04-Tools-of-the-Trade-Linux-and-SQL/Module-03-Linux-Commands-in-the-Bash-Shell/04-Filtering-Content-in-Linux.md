# 🔍 Filtering Content in Linux (grep, pipe, find)

---

## 🌱 Overview

Filtering is a critical skill for security analysts. It allows you to search for specific information that can help solve complex security problems, such as identifying malware, investigating unauthorized access, or analyzing logs.

---

## 🎯 Why Filtering Matters in Cybersecurity
Security analysts often need to:
- Search for suspicious strings in files
- Identify affected files quickly
- Narrow down large datasets into meaningful results

📌 Filtering allows analysts to **customize data** based on specific conditions instead of manually reviewing files.

---

## 🧠 What Is Filtering?
**Filtering** means selecting data that matches a certain condition.

Examples:
- Finding all `.txt` files affected by malware
- Searching for error messages in log files
- Identifying files modified recently
- Locating files that contain suspicious keywords

Linux provides powerful tools to perform this filtering efficiently.

---

## 🔎 `grep` — Search for Text Inside Files
The `grep` command searches a specified file and returns **all lines that contain a given string**.

### 🔹 Basic Syntax
```bash
grep STRING FILE
```

---

### 📌 Example: Searching for a Keyword
```bash
grep OS updates.txt
```

Explanation:
- `OS` → string being searched
- `updates.txt` → file being searched

📌 Output includes **only lines that contain the word `OS`**.

---

### 📌 Another Example
```bash
grep error time_logs.txt
```

This command:
- Searches for the word `error`
- Returns only lines from `time_logs.txt` that contain it

📌 This is extremely useful for **log analysis**.

---

## 🔗 Piping (`|`) — Connect Commands Together
Piping allows the **output of one command** to become the **input of another command**.

### 🧠 How Piping Works
Think of a physical pipe:
- Data enters from one side
- Travels through the pipe
- Comes out on the other side

Linux piping works the same way.

---

### 🔹 Pipe Character
The pipe is represented by:
```text
|
```

📌 Often located on the same key as `\` on keyboards.

---

## 🔎 Using `grep` with Piping
When `grep` is used **after a pipe**, it searches the output of the previous command instead of a file.

---

### 📌 Example: Filtering Directory Contents
```bash
ls /home/analyst/reports | grep users
```

Explanation:
- `ls /home/analyst/reports` lists all files and directories
- `|` sends that output to `grep`
- `grep users` returns only names containing `users`

📌 Files that do not contain the word `users` are filtered out.

---

## 🧠 Why Piping Is Powerful
- Eliminates unnecessary output
- Reduces manual searching
- Enables advanced filtering workflows

📌 Piping is a **general redirection tool**, not limited to filtering.

---

## 📁 `find` — Search for Files and Directories
The `find` command searches for files and directories that meet **specific criteria**.

### 🔹 Basic Syntax
```bash
find START_LOCATION CRITERIA
```

---

### 📌 Example: Basic Search
```bash
find /home/analyst/projects
```

📌 This returns **everything** under the projects directory.

---

## ⚙️ Using Options with `find`
Options modify the behavior of the `find` command and usually begin with a hyphen (`-`).

---

### 🔎 `-name` and `-iname`
Used to search by file or directory name.

- `-name` → case-sensitive
- `-iname` → case-insensitive

---

### 📌 Example: Search by Name
```bash
find /home/analyst/projects -name "*log*"
```

This returns files that:
- Contain `log`
- Are case-sensitive

---

### 📌 Case-Insensitive Search
```bash
find /home/analyst/projects -iname "*log*"
```

📌 This will also match `Log`, `LOG`, etc.

---

### ⭐ Wildcard (`*`)
The asterisk (`*`) represents:
- Zero or more unknown characters

Example:
```text
*log*
```

Matches:
- access_log.txt
- systemlog
- error_logs

---

## ⏱️ `-mtime` — Search by Modification Time
Security analysts often need to identify **recently modified files**.

---

### 📌 Example: Modified Within Last 3 Days
```bash
find /home/analyst/projects -mtime -3
```

Returns files modified:
- Less than 3 days ago

---

### 📌 Other Time Examples
- More than 1 day ago:
```bash
find /home/analyst/projects -mtime +1
```

- Less than 1 day ago:
```bash
find /home/analyst/projects -mtime -1
```

---

### 🧠 Minutes Instead of Days
Use `-mmin` to search based on minutes.

---

## 🔐 Security Perspective
Filtering tools help security analysts:
- Detect malware patterns
- Investigate unauthorized access
- Analyze logs efficiently
- Reduce response time during incidents

📌 These commands are used **daily** in real-world security roles.

---

## ✅ Key Takeaways
- Filtering is essential for security analysis
- `grep` searches for text inside files
- Piping (`|`) sends output from one command to another
- `find` searches files and directories using criteria
- Options like `-name`, `-iname`, and `-mtime` refine searches
- These tools help analysts work faster and smarter

---
## Lab Documentation

**📄 Lab README**  
- [Lab 02 – Filter with grep](labs/lab-02-Filter-With-Grep/README.md)

**📸 Execution Screenshots**  
- [Screenshots Folder](labs/lab-02-Filter-With-Grep/screenshots)

**Description**  
This lab demonstrates practical usage of `grep` and piping to search log files, filter file names, and extract specific user and system information efficiently.

---
*✍️ Notes By Abhishek (Ez Abyss)*
