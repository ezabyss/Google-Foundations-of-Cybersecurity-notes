# 🔐 Linux File & Directory Permissions

---

## 🌱 Overview
As a security analyst, understanding **file and directory permissions** is critical. Permissions determine **who can access, modify, or execute** files and directories in Linux.

Permissions are closely tied to **authorization**, which is the process of granting or restricting access to system resources. A core security principle is **need-to-know access**—users should only have the permissions required to perform their job.

---

## 🧠 Why Permissions Matter in Security
Incorrect permissions can lead to:
- Data leaks
- Unauthorized modifications
- Malware execution
- Insider threats

---

### 🧠 SOC Scenario
> During a security audit, an analyst discovers sensitive payroll files readable by all users.  
> This misconfiguration represents a **privacy and compliance violation**.

---

## 🧾 Types of Linux Permissions
Linux has **three permission types**:

### 📖 Read (`r`)
- **File:** Allows contents to be read
- **Directory:** Allows listing files inside the directory

### ✏️ Write (`w`)
- **File:** Allows modification of file contents
- **Directory:** Allows creating or deleting files inside the directory

### ▶️ Execute (`x`)
- **File:** Allows execution if the file is a program
- **Directory:** Allows entering the directory and accessing its contents

---

### 🧠 SOC Scenario
> An attacker uploads a malicious script but cannot run it because **execute permissions are missing**—preventing exploitation.

---

## 👥 Permission Owner Types
Permissions are assigned to **three owner categories**:

- **User (u):** The file owner
- **Group (g):** Users belonging to the same group
- **Other (o):** Everyone else on the system

---

### 🧠 SOC Scenario
> A contractor account appears under “other.”  
> Proper permissions ensure contractors **cannot access internal security files**.

---

## 🔢 Permission String Structure
Permissions are displayed as a **10-character string**, for example:

```text
drwxrwxrwx
```

### Character Breakdown
| Position | Meaning |
|--------|--------|
| 1 | File type (`d` = directory, `-` = file) |
| 2–4 | User permissions (`rwx`) |
| 5–7 | Group permissions (`rwx`) |
| 8–10 | Other permissions (`rwx`) |

Hyphens (`-`) indicate **missing permissions**.

---

### 🧠 SOC Scenario
> A world-writable file (`-rw-rw-rw-`) is flagged during monitoring.  
> Analysts recognize this as a **high-risk configuration**.

---

## 🔍 Checking Permissions with `ls`

### 📌 `ls -l` — View Permissions
```bash
ls -l
```

Displays:
- Permissions
- Owner
- Group
- File size
- Last modification time

---

### 📌 `ls -a` — Show Hidden Files
```bash
ls -a
```

Hidden files begin with a `.`

---

### 📌 `ls -la` — Full Permission View
```bash
ls -la
```

Shows **permissions + hidden files**.

---

### 🧠 SOC Scenario
> An analyst checks hidden configuration files (`.env`, `.hidden`) to verify **no secrets are exposed**.

---

## 🔧 Changing Permissions with `chmod`
The `chmod` command (**change mode**) modifies file and directory permissions.

---

## 🧩 Symbolic Mode Components
`chmod` uses symbols instead of numbers:

### Owner Types
- `u` → user
- `g` → group
- `o` → other

### Operators
- `+` → add permission
- `-` → remove permission
- `=` → assign exact permissions

### Permission Types
- `r` → read
- `w` → write
- `x` → execute

---

## 📌 Example: Modify Group & Other Permissions
```bash
chmod g+w,o-r access.txt
```

Explanation:
- `g+w` → add write permission to group
- `o-r` → remove read permission from other

---

### 🧠 SOC Scenario
> Analysts in the security group need to update logs,  
> but external users must not read them.  
> `chmod` enforces **least privilege**.

---

## 📌 Assign Exact Permissions with `=`
```bash
chmod u=r,g=r,o=r login_sessions.txt
```

📌 This **overwrites existing permissions**.

---

### 🧠 SOC Scenario
> After an incident, logs are locked to **read-only** mode to preserve evidence integrity.

---

## 🛡️ Principle of Least Privilege
**Least privilege** means users should only have the **minimum access required**.

---

### 📌 Real Example
Initial permissions:
```text
-rw-rw----
```

Problem:
- Group has unnecessary access

Fix:
```bash
chmod g-rw bonuses.txt
```

---

### 🧠 SOC Scenario
> A compensation file contains sensitive salary data.  
> Only the HR representative should access it—no group access allowed.

---

## ✅ Key Takeaways
- Permissions control **authorization**
- Linux permissions include `r`, `w`, `x`
- Owners include user, group, and other
- `ls -l` and `ls -la` reveal permissions
- `chmod` modifies access rights
- Least privilege reduces attack surface
- Misconfigured permissions are **common SOC findings**

---

*✍️ Notes By Abhishek (Ez Abyss)*
