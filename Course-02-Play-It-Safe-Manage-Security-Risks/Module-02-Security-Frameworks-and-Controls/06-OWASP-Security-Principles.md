# 🔐 OWASP Security Principles
**Notes by Abhishek (Ez Abyss)**

---

## 🌐 Overview

As a **security analyst**, protecting an organization’s **data and assets** is a core responsibility. Along with **NIST frameworks** and the **CIA triad**, security principles help teams minimize **threats, risks, and vulnerabilities**.

The **Open Worldwide Application Security Project® (OWASP)** provides widely used security principles that guide secure system and application design. These principles are especially important for **entry-level analysts**, as they appear frequently in daily security work.

---

## 🧠 Why OWASP Security Principles Matter

In real-world environments, security principles are embedded in everyday tasks such as:

* Analyzing logs
* Monitoring SIEM dashboards
* Using vulnerability scanners
* Reviewing access controls

These principles help ensure security is **practical, consistent, and effective**.

---

## 🔑 Core OWASP Security Principles

### 1️⃣ Minimize Attack Surface Area

**Definition:**
The attack surface includes all possible vulnerabilities or **attack vectors** a threat actor could exploit.

**Common Attack Vectors:**

* Phishing emails
* Weak passwords
* Unnecessary software features

**How Organizations Reduce Attack Surface:**

* Disable unused features
* Restrict access to sensitive assets
* Enforce strong password policies

📌 *Fewer entry points mean fewer opportunities for attackers.*

---

### 2️⃣ Principle of Least Privilege

**Definition:**
Users should have **only the minimum access** required to perform their job tasks.

**Why It Matters:**

* Limits damage if credentials are compromised
* Reduces insider threat risk

**Example:**

* An entry-level analyst may view logs but cannot change user permissions

📌 *Limited access limits impact.*

---

### 3️⃣ Defense in Depth

**Definition:**
Use **multiple layers of security controls** to protect systems and data.

**Examples of Controls:**

* Multi-factor authentication (MFA)
* Firewalls
* Intrusion detection systems (IDS)
* Permission and access controls

📌 *If one control fails, others still protect the system.*

---

### 4️⃣ Separation of Duties

**Definition:**
No single individual should have enough privileges to misuse a system.

**Why It Matters:**

* Prevents fraud and abuse
* Reduces risk of insider threats

**Example:**

* The person who prepares paychecks should not be the one who approves them

📌 *Critical actions should require multiple roles.*

---

### 5️⃣ Keep Security Simple

**Definition:**
Avoid overly complex security solutions.

**Why It Matters:**

* Complex systems are harder to manage
* Complexity increases misconfiguration risk

📌 *Simple security is easier to maintain and more reliable.*

---

### 6️⃣ Fix Security Issues Correctly

**Definition:**
When an incident occurs, identify the **root cause** and fix it properly.

**Best Practices:**

* Contain the issue
* Identify vulnerabilities
* Apply correct fixes
* Test remediation

**Example:**

* Replacing weak Wi-Fi passwords with stronger password policies

📌 *Fixing symptoms without addressing root causes leads to repeat incidents.*

---

## ➕ Additional OWASP Security Principles

### 7️⃣ Establish Secure Defaults

**Definition:**
Systems should be **secure by default**.

**Key Idea:**

* It should take extra effort to make a system insecure

📌 *Default settings should prioritize security.*

---

### 8️⃣ Fail Securely

**Definition:**
When a system or control fails, it should default to its **most secure state**.

**Example:**

* A firewall failure should block all traffic, not allow everything

📌 *Failure should not create new vulnerabilities.*

---

### 9️⃣ Don’t Trust Services

**Definition:**
Do not assume third-party systems are secure.

**Why It Matters:**

* Third-party vendors may follow different security standards

**Example:**

* Verifying airline reward balances before displaying them to customers

📌 *Trust must be verified, not assumed.*

---

### 🔟 Avoid Security by Obscurity

**Definition:**
Security should not rely on keeping system details secret.

**Key Idea:**

* Strong security depends on controls, not secrecy

**OWASP Example:**

* Application security should rely on password policies, defense in depth, network design, and auditing—not hidden source code

📌 *Hidden systems are not secure systems.*

---

## ✅ Key Takeaways

* OWASP security principles guide secure system design
* These principles are used daily by cybersecurity professionals
* They work alongside **NIST frameworks** and the **CIA triad**
* Applying these principles reduces risk and protects people
* Strong understanding helps entry-level analysts stand out

---
