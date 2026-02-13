# 📄 Import and Parse a Text File (Security Logs) — Python Lab

## 📌 Overview

Security logs are commonly stored in text files. To analyze them, security analysts must be able to:

- Import log files safely
- Read file content into Python
- Parse/transform data for analysis
- Update logs when entries are missing
- Generate communication artifacts (like allow lists)

This lab demonstrates those skills using Python file handling and string parsing.

---

## 🎯 Skills Demonstrated

- File handling with the `with` statement
- `open()` modes: `"r"`, `"a"`, `"w"`
- Reading file content using `.read()`
- Splitting text into lists using `.split()`
- Appending missing entries using `.write()`
- Creating and reading an allow-list text file

---

## 📁 Repo Structure

```
parse-textfile/
├── README.md
├── import-and-parse.py
└── data/
    ├── login.txt
    └── allow_list.txt
```

## ▶️ How to Run
`python3 lab_import_parse.py`

## 🔄 Reset the Login File (Optional)
If you want to reset data/login.txt back to original contents:
`python3 lab_import_parse.py --reset`

## 🧩 What the Lab Does

### Task 1 & 2 — Import and Read a Log File
- Uses with open(import_file, "r") as file:
- Reads the full log using file.read()
- Stores output as a string

### Task 3 — Split the Log into a List
- Uses text.split() to break the log into list items
- Task 4 — Append a Missing Log Entry
- Uses open(import_file, "a") + .write() to append missing entry
- Re-reads the file to confirm updates

### Task 5–7 — Create an Allow List File
- Writes allowed IP addresses to data/allow_list.txt
- Reads it back and prints it

## 🛡 Real-World Security Relevance

This workflow supports:
- Preparing logs for SIEM ingestion
- Quickly validating whether a log file is complete
- Communicating approved access lists to teams
- Building automation pipelines for security operations

## 🧠 Key Takeaways
- with automatically closes files safely
- "r" = read, "a" = append, "w" = write (overwrite/create)
- .read() loads entire file into a string
- .split() converts string data into list format for analysis
- .write() can update or generate new security artifacts

---
✍️ Notes By Abhishek (Ez Abyss)
