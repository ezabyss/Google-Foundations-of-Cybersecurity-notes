# 🌿 Managing Directories & Files in Linux  

---

## 🌱 Overview
The Linux file system can be visualized as a **tree**.

- The **root directory** is the base
- **Subdirectories** are the branches
- Files live along these branches

In this section, you’ll learn how to **create, remove, move, copy, and edit** directories and files—skills that are essential for **Security Operations Center (SOC)** work.

---

## 🎯 Why File Organization Matters in Security
Security analysts deal with:
- Logs
- Reports
- Evidence files
- Configuration data

📌 If data is well-organized, analysts can:
- Detect threats faster
- Reduce investigation time
- Prevent accidental data exposure

---

### 🧠 SOC Scenario
> During an incident response, logs are scattered across directories.  
> An analyst who knows **where files belong** can immediately isolate suspicious activity instead of wasting time searching.

---

## 📁 Directories in Linux
Linux uses **directories** (similar to folders) to organize files.

Example:
```text
reports/
├── drafts/
└── final/
```

This separation prevents unfinished work from being mistaken as final evidence.

---

### 🧠 SOC Scenario
> A junior analyst accidentally sends a **draft report** to management.  
> Proper directory separation (`drafts/` vs `final/`) prevents this mistake.

---

## 🧭 Creating & Removing Directories

### 📌 `mkdir` — Create a Directory
```bash
mkdir drafts
```

Creates a new directory named `drafts`.

---

### 📌 `rmdir` — Remove an Empty Directory
```bash
rmdir oldreports
```

📌 `rmdir` only works if the directory is **empty**, protecting you from accidental data loss.

---

### 🧠 SOC Scenario
> An analyst attempts to delete a directory containing evidence.  
> `rmdir` fails because files still exist—**preventing accidental destruction of forensic data**.

---

## 📄 Creating & Removing Files

### 📌 `touch` — Create a File
```bash
touch OS_patches.txt
```

Creates an empty file.

---

### 📌 `rm` — Remove a File
```bash
rm email_patches.txt
```

Deletes the specified file.

⚠️ Deleted files are difficult to recover.

---

### 🧠 SOC Scenario
> After confirming a report is no longer needed, an analyst removes outdated files to prevent confusion during audits.

---

## 🚚 Moving & Copying Files

### 📌 `mv` — Move or Rename Files
```bash
mv email_policy.txt drafts/
```

Moves `email_policy.txt` into the `drafts` directory.

📌 `mv` can also rename files:
```bash
mv permissions.txt perm.txt
```

---

### 📌 `cp` — Copy Files
```bash
cp vulnerabilities.txt /home/analyst/projects
```

Copies the file while keeping the original.

---

### 🧠 SOC Scenario
> A vulnerabilities report is needed for both:
> - The **current incident**
> - An **upcoming security project**
>
> The analyst uses `cp` to avoid modifying the original evidence.

---

## ✏️ Editing Files with `nano`
Security analysts frequently edit:
- Reports
- Access lists
- Configuration notes

---

### 📌 `nano` — Beginner-Friendly Editor
```bash
nano OS_patches.txt
```

Opens the file for editing.

---

### 💾 Save & Exit Nano
Inside nano:
- Save → `Ctrl + O` → Enter
- Exit → `Ctrl + X`

---

### 🧠 SOC Scenario
> An analyst updates a report title during a live incident briefing.  
> `nano` allows **quick edits without leaving the terminal**.

---

## 📝 Writing to Files with Output Redirection

### 📌 Overwrite File (`>`)
```bash
echo "time" > permissions.txt
```

⚠️ Overwrites the entire file.

---

### 📌 Append to File (`>>`)
```bash
echo "last updated date" >> permissions.txt
```

Adds content without removing existing data.

---

### 🧠 SOC Scenario
> An analyst appends timestamps to a permissions log during an investigation.  
> Using `>>` ensures **previous audit data is preserved**.

---

## 🔐 Security Perspective
These commands allow analysts to:
- Maintain evidence integrity
- Separate drafts from final reports
- Preserve logs for audits
- Avoid accidental data loss

📌 File management is a **daily SOC responsibility**, not just a technical skill.

---

## ✅ Key Takeaways
- Linux directories form a tree-like structure
- `mkdir` and `rmdir` manage directories safely
- `touch` and `rm` manage files
- `mv` moves or renames files
- `cp` copies files without deleting originals
- `nano` is ideal for quick edits
- `>` overwrites files, `>>` appends content
- Proper organization improves **security and response time**

---

*✍️ Notes By Abhishek (Ez Abyss)*
