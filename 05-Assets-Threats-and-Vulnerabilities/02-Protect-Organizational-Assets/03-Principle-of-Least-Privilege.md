# 🔑 Principle of Least Privilege (PoLP)  
*Reducing Risk Through Controlled Access*

---

## 🌍 What Is the Principle of Least Privilege?
The **Principle of Least Privilege (PoLP)**—also called **least privilege**—is a security concept where:

> A user is granted **only the minimum level of access and authorization** required to perform a task or function.

This principle applies to:
- People
- Devices
- Applications
- Services

---

## 🔐 Why Least Privilege Matters (CIA Triad)
Least privilege directly supports the **CIA triad**:

- **Confidentiality** → Limits who can view sensitive data  
- **Integrity** → Reduces accidental or malicious modification  
- **Availability** → Prevents misuse that could disrupt systems  

---

## ⚠️ How Limiting Access Reduces Risk
Implementing least privilege helps organizations by:

- Limiting access to sensitive information  
- Reducing accidental data modification, tampering, or deletion  
- Supporting monitoring, logging, and administration  

> The fewer permissions a user has, the **smaller the attack surface**.

---

## 🧠 SOC Scenario: Excessive Access
**Situation:**  
SOC investigates a breach where a compromised account accessed multiple databases.

**Finding:**  
The user had permissions far beyond their job role.

**Lesson:**  
Privilege creep increases breach impact.

---

## 🧩 Least Privilege & Separation of Duties
Least privilege is closely related to **separation of duties**.

### Separation of Duties:
- Splits critical tasks among multiple users
- Prevents one user from having full control

> This reduces fraud, abuse, and single points of failure.

---

## 🔍 Determining Access & Authorization
To implement least privilege, security teams must answer two questions:

1. **Who is the user?**  
2. **How much access do they need to a specific resource?**

---

## 👤 Who Is a User?
A **user** can be:
- A person (employee, customer, vendor)
- A device
- A software application or service

> Best practice: **Every user gets a unique account**.

Accounts are usually managed in a **directory service**.

---

## 📂 Common Types of User Accounts

| Account Type | Description |
|-------------|------------|
| **Guest accounts** | External users (customers, partners, contractors) |
| **User accounts** | Internal staff, role-based |
| **Service accounts** | Applications or software interactions |
| **Privileged accounts** | Elevated or administrative access |

---

## 🧠 SOC Scenario: Privileged Account Abuse
**Situation:**  
SOC detects unusual activity from an admin account at night.

**Risk:**  
Privileged accounts cause the most damage if compromised.

**Action:**  
- Investigate immediately  
- Enforce stricter access controls  

---

## 🎯 Baseline Access Levels
Each account type should have a **baseline access level**:
- Defined before deployment
- Based on role and necessity

However, access is **not static**.

---

## ⏱️ Time-Based & Situational Access
Access should change depending on context.

### Example:
- A customer support agent can view your data **only while assisting you**
- Access is revoked once the interaction ends

> Least privilege only works if access is **dynamic and monitored**.

---

## 🔐 Passwords & Least Privilege
Even well-designed access controls can fail if:
- Passwords are weak
- Credentials are reused
- MFA is not enforced

> Strong authentication is critical to enforcing least privilege.

---

## 🔄 Why Auditing Is Essential
Setting access correctly is **not enough**.

Accounts must be:
- Reviewed
- Audited
- Updated regularly

This prevents long-term risk.

---

## 🧪 Three Types of Account Audits

---

### 1️⃣ Usage Audits
**Purpose:**  
Review what resources users are accessing and how.

**Benefits:**
- Detects policy violations
- Identifies unused permissions

---

### 🧠 SOC Scenario: Usage Audit
**Situation:**  
SOC finds an employee accessing systems unrelated to their role.

**Action:**  
- Revoke unnecessary permissions  
- Notify management  

---

### 2️⃣ Privilege Audits
**Purpose:**  
Identify **privilege creep**—when users accumulate excess access over time.

**Common Causes:**
- Promotions
- Role changes
- Department transfers

---

### 🧠 SOC Scenario: Privilege Creep
**Situation:**  
An employee still has admin rights from a previous role.

**Risk:**  
Increased attack surface.

**Action:**  
- Adjust permissions  
- Enforce role-based access  

---

### 3️⃣ Account Change Audits
**Purpose:**  
Review logs of account changes in directory services.

**Detects:**
- Unauthorized password changes
- Suspicious permission updates

> Most systems can alert admins automatically.

---

## 🧠 SOC Scenario: Account Change Alert
**Situation:**  
Multiple failed password change attempts detected.

**SOC Action:**
- Lock account  
- Investigate potential compromise  

---

## 🎯 Key Takeaways

- Least privilege grants minimum necessary access
- Reduces data breaches and misuse
- Applies to users, devices, and applications
- Privilege creep is a major security risk
- Auditing is essential for effectiveness
- Strong authentication supports least privilege
- SOC teams monitor, audit, and enforce PoLP daily

---

✍️ **Notes By Abhishek (Ez Abyss)**
