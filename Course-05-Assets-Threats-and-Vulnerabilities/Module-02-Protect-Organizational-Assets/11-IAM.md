# 🔐 Identity & Access Management (IAM)  
*Controlling Who Gets Access, To What, When, and Why*

---

## 🌍 Why Identity & Access Matter
Security is not just about tools—it’s about **creating a controlled environment** that supports a defense strategy.

At the core of access control are two fundamental security principles:
- **Least Privilege**
- **Separation of Duties**

IAM and AAA frameworks exist to enforce these principles consistently.

---

## 🔑 Core Security Principles

### Principle of Least Privilege
A user is granted **only the minimum access** required to perform their task.

Example:
- An IT employee can approve purchases **only for IT**, not all departments.

---

### Separation of Duties (SoD)
Responsibilities are **divided among multiple users** so no single person has excessive control.

Example:
- One person enters purchase requests
- A different person approves them

> Least privilege limits access.  
> Separation of duties divides responsibility.

---

## 🧩 AAA vs IAM

### AAA Framework
AAA focuses on **how access happens**:
1. **Authentication** – Who are you?
2. **Authorization** – What can you do?
3. **Accounting** – What did you do?

---

### Identity & Access Management (IAM)
**IAM** is a broader collection of **processes and technologies** used to:
- Manage digital identities
- Grant and revoke access
- Track user activity
- Enforce compliance

Both AAA and IAM aim to ensure:
> The right user gets the right access, at the right time, for the right reason.

---

## 👤 What Is a User?
In IAM, a **user** can be:
- A person
- A device
- A software application

All must be authenticated, authorized, and monitored.

---

## 🔐 Authenticating Users
Authentication proves identity using one or more factors:

- **Something you know** → password, PIN
- **Something you have** → OTP, security token
- **Something you are** → biometrics

Common authentication tools:
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)

---

## 🛠️ User Provisioning & Deprovisioning

### User Provisioning
The process of **creating and maintaining** a digital identity.

Example:
- New instructor receives access to teaching systems.

---

### User Deprovisioning
The process of **removing access** when it is no longer needed.

Example:
- Employee leaves → account disabled immediately.

> Improper deprovisioning is a major cause of breaches.

---

## 🔓 Granting Authorization
Once a user is authenticated, the system must decide:
> **What resources can this user access?**

This is handled using **access control models**.

---

## 🏛️ Mandatory Access Control (MAC)
**MAC** is the **strictest** access control model.

### Characteristics:
- Access based on **need-to-know**
- Controlled by a **central authority**
- Users **cannot** change permissions

### Common Use:
- Military
- Government
- Law enforcement

📌 Also called **non-discretionary access control**.

---

## 👤 Discretionary Access Control (DAC)
**DAC** allows the **data owner** to decide who gets access.

### Characteristics:
- Flexible
- Owner-controlled
- Common in personal and business environments

### Example:
- Sharing a Google Drive folder with editor/viewer access

📌 Easier to manage, but higher risk if misused.

---

## 🧩 Role-Based Access Control (RBAC)
**RBAC** assigns permissions based on **job roles**.

### Characteristics:
- Scalable
- Easy to manage
- Common in enterprises

### Example:
- Marketing role → analytics access
- IT role → server administration

📌 Users inherit permissions through roles, not individually.

---

## 📊 MAC vs DAC vs RBAC

| Model | Who Controls Access | Flexibility | Security Level |
|----|------------------|------------|---------------|
| MAC | Central authority | Low | Very High |
| DAC | Data owner | High | Moderate |
| RBAC | System / admin | Medium | High |

---

## 🧠 SOC Perspective
SOC teams care about:
- Over-privileged users
- Role misconfiguration
- Failure to deprovision accounts
- Unauthorized access patterns

IAM logs are critical for:
- Incident response
- Insider threat detection
- Compliance audits

---

## 🛠️ Access Control Technologies
IAM systems typically include:
- User directory
- Identity management tools
- Authorization engines
- Auditing & logging systems

Organizations may:
- Build custom IAM solutions (costly)
- License third-party IAM platforms (common)

⚠️ Tools alone are not enough—**configuration matters**.

---

## 🎯 Key Takeaways

- IAM and AAA enforce least privilege and separation of duties
- Authentication verifies identity
- Authorization controls access to resources
- Accounting tracks user actions
- MAC is strict and centrally controlled
- DAC is owner-controlled and flexible
- RBAC is scalable and role-driven
- Proper provisioning and deprovisioning are critical
- IAM misconfigurations are a common breach vector

---

✍️ **Notes By Abhishek (Ez Abyss)**
