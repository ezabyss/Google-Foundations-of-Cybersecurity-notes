# 🖥️ Operating System (OS) Hardening

---

## 🎯 Why OS Hardening Is Critical

The **operating system (OS)** is the foundation of every computer system.

> ⚠️ **One insecure OS can compromise the entire network.**

Because the OS controls how hardware, software, and users interact, attackers often target it first.

---

## 🧠 What Is an Operating System?

### 📌 Definition

An **operating system (OS)** is:

* The **interface between computer hardware and the user**
* The **first program loaded** when a computer turns on
* An **intermediary** between applications and hardware

Examples include Windows, Linux, and macOS.

---

## 🔐 What Is OS Hardening?

### 📌 Definition

**OS hardening** is a set of security procedures that:

* Protect the operating system
* Reduce OS-level vulnerabilities
* Improve overall network security

> Securing the OS helps secure *everything built on top of it*.

---

## 🧩 Common OS Hardening Practices

Although operating systems differ, they share **similar hardening practices**.

OS hardening tasks fall into **two categories**:

1. Tasks performed **regularly**
2. Tasks performed **once** during initial setup

---

## 🔄 OS Hardening Tasks (Performed Regularly)

### 1️⃣ Patch Updates

#### 📌 Definition

A **patch update** is a software or OS update that fixes:

* Security vulnerabilities
* Bugs and weaknesses in programs

#### 🔍 Why Patch Updates Matter

* Once a patch is released, attackers know **exactly where the vulnerability exists**
* Systems running outdated OS versions become **easy targets**

> ⏱️ **Best practice:** Apply patches as soon as they are released.

---

### 🧠 Baseline Configuration (Baseline Image)

#### 📌 Definition

A **baseline configuration** is a documented set of:

* Approved system settings
* Security configurations
* Standard rules and permissions

It is used as a **reference point** for future updates and audits.

#### 📋 Example

* Firewall rules listing allowed and blocked network ports

#### 🔎 Why It Matters

* Helps detect unauthorized or suspicious changes
* Makes incident response faster and more accurate

---

### 2️⃣ Hardware & Software Disposal

Proper disposal prevents data leakage.

Best practices:

* Securely wipe old hardware before disposal
* Remove unused software applications

🔐 **Why this matters:**

* Old hardware may still contain sensitive data
* Unused software may contain known vulnerabilities

---

## 🧱 OS Hardening Tasks (Performed Once)

### 🔐 Secure Configuration Settings

Some settings are configured during initial setup:

* Enforcing secure encryption standards
* Disabling unnecessary default services

These steps reduce vulnerabilities **from day one**.

---

## 🔑 Strong Password Policies

### 📌 What Is a Password Policy?

A **password policy** enforces rules that make passwords harder to guess.

Common requirements:

* Minimum length (e.g., 8 characters)
* At least one uppercase letter
* At least one number
* At least one symbol

---

### 🚫 Account Lockout Rules

To prevent brute-force attacks:

* Accounts may be locked after multiple failed login attempts

This discourages malicious actors from guessing passwords.

---

## 🔐 Multi-Factor Authentication (MFA)

### 📌 Definition

**MFA** requires users to verify identity using **two or more factors**.

### 🧠 Authentication Factors

* 🔑 Something you know → Password
* 💳 Something you have → ID card, phone
* 🧬 Something you are → Fingerprint, face scan

> MFA significantly increases security, even if passwords are compromised.

---

## 🧠 Quick Review 

* OS is the foundation of system security
* OS hardening reduces vulnerabilities
* Patch updates must be applied quickly
* Baseline configurations detect changes
* Strong passwords + MFA protect access

---

## 📝 In One Line

> *OS hardening is a set of security procedures that protect operating systems by applying updates, enforcing secure configurations, managing access controls, and reducing vulnerabilities that could compromise the entire network.*

---
✨ Strong OS security = strong network security

---
**Notes by Abhishek (Ez Abyss)**
