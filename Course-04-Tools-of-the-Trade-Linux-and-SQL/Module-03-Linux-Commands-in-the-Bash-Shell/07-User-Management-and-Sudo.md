# 👤 Linux User Management & Responsible Use of `sudo`
*Authentication, Authorization, and SOC Best Practices*

---

## 🌱 Overview
Managing users is a core responsibility for security analysts. In Linux, **user management is closely tied to authentication and authorization**, ensuring that only approved individuals can access systems and resources.

In this section, you’ll learn how to:
- Add and delete users
- Modify user accounts
- Manage ownership of files
- Use `sudo` responsibly instead of logging in as root

---

## 🔐 Authentication vs Authorization
- **Authentication**: Verifying *who* a user is  
- **Authorization**: Determining *what* a user can access

Both are essential for maintaining a secure multi-user Linux environment.

---

### 🧠 SOC Scenario
> During an access review, an analyst confirms that a user’s login credentials are valid (authentication)  
> but discovers they still have access to sensitive systems they no longer need (authorization issue).

---

## 👑 Root User (Superuser)
The **root user** has unrestricted control over the system.

Root users can:
- Create, modify, or delete any file
- Add or remove users
- Run any command without restriction

---

## ⚠️ Why Logging in as Root Is Dangerous
Running commands as root is **not recommended** because:

- Root accounts are prime targets for attackers
- Mistakes made as root are often **irreversible**
- Actions cannot be attributed to a specific user

---

### 🧠 SOC Scenario
> An administrator accidentally deletes a critical directory while logged in as root.  
> Because there is no user attribution, **incident investigation becomes difficult**.

---

## 🛡️ `sudo` — Super User Do
The `sudo` command allows approved users to run **specific commands with elevated privileges**.

Key characteristics:
- Temporary privilege escalation
- Requires the user’s own password
- Logged for accountability
- Configured through the **sudoers file**

📌 Only trusted users should have sudo access.

---

### 🧠 SOC Scenario
> Audit logs show a configuration change made via `sudo`.  
> Investigators can identify **exactly which user ran the command**.

---

## ➕ Adding Users with `useradd`
The `useradd` command adds a new user to the system.

```bash
sudo useradd salesrep7
```

📌 No output means the command executed successfully.

---

### 🧠 SOC Scenario
> A new employee joins the sales team.  
> The analyst provisions their account using `useradd` to ensure **controlled system access**.

---

### 🔧 Common `useradd` Options
- `-g` → set primary group
- `-G` → add supplemental groups

Example:
```bash
sudo useradd -g security fgarcia
sudo useradd -G finance,admin fgarcia
```

---

## ➖ Deleting Users with `userdel`
The `userdel` command removes a user from the system.

```bash
sudo userdel salesrep7
```

---

### 🧠 SOC Scenario
> An employee leaves the organization.  
> Their account is deleted immediately to prevent **unauthorized access**.

---

### ⚠️ Deleting User Files
```bash
sudo userdel -r fgarcia
```

- Deletes the user
- Removes their home directory and files

📌 Always verify backups before using `-r`.

---

## 🔄 Modifying Users with `usermod`
The `usermod` command modifies existing users.

---

### 📌 Change Primary Group
```bash
sudo usermod -g executive fgarcia
```

---

### 📌 Add Supplemental Group
```bash
sudo usermod -a -G marketing fgarcia
```

⚠️ Always include `-a` with `-G` to avoid removing existing groups.

---

### 📌 Lock an Account
```bash
sudo usermod -L fgarcia
```

Prevents login without deleting the account.

---

### 🧠 SOC Scenario
> A contractor’s project ends.  
> Instead of deleting the account, the analyst **locks it** to preserve file ownership for investigation.

---

## 📁 Changing Ownership with `chown`
The `chown` command changes file or directory ownership.

---

### 📌 Change File Owner
```bash
sudo chown fgarcia access.txt
```

---

### 📌 Change Group Owner
```bash
sudo chown :security access.txt
```

📌 The colon (`:`) specifies a group.

---

### 🧠 SOC Scenario
> Files created by a departed employee are reassigned to a manager  
> to ensure **continued access and accountability**.

---

## 🧠 Principle of Least Privilege
The **principle of least privilege** means granting **only the access required** to perform a task.

Violations increase the risk of:
- Data breaches
- Insider threats
- Accidental system damage

---

### 📌 Least Privilege in Action
Initial permissions:
```text
-rw-rw----
```

Fix:
```bash
chmod g-rw bonuses.txt
```

---

### 🧠 SOC Scenario
> Salary data is restricted so only HR can access it,  
> preventing **unauthorized internal disclosure**.

---

## ⚠️ Responsible Use of `sudo`
- Use `sudo` only when necessary
- Avoid copying commands blindly from the internet
- Never run full workflows as root
- Treat sudo access like a **master key**

---

## ✅ Key Takeaways
- Authentication verifies identity
- Authorization controls access
- Root has unrestricted privileges
- `sudo` provides controlled privilege escalation
- `useradd`, `userdel`, `usermod` manage users
- `chown` manages file ownership
- Least privilege reduces attack surface
- User management is a **daily SOC responsibility**

---

*✍️ Notes By Abhishek (Ez Abyss)*
