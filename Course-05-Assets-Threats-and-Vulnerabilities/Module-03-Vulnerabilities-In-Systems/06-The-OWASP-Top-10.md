# 🌐 OWASP Top 10 — Web Application Security

---

## 🌍 Why OWASP Matters

Security is a **global effort**, and staying informed is essential to preparing for future risks.

Previously, the CVE® list helped us understand **known vulnerabilities and exposures** in existing systems. OWASP focuses on a different but equally critical area: **web application security**, especially for **new or custom-built software**.

---

## 🏛️ What Is OWASP?

**OWASP (Open Worldwide Application Security Project®)** is a **nonprofit foundation** dedicated to improving software security.

OWASP provides:

* Open knowledge
* Tools and documentation
* Events and community collaboration

> 🌍 Security professionals around the world rely on OWASP to share best practices for securing web applications.

---

## 🔟 What Is the OWASP Top 10?

The **OWASP Top 10** is a regularly updated list of the **most critical web application security risks**.

Key facts:

* Published since **2003**
* Updated every few years
* Based on frequency and impact of vulnerabilities
* Used by developers, security teams, and auditors

> 🧠 Unlike the CVE list (existing software), OWASP Top 10 helps guide **secure application design**.

---

## 🧑‍💼 Who Uses the OWASP Top 10?

* Developers → build secure applications
* Security teams → prioritize testing
* Auditors → check regulatory compliance
* Organizations → guide secure design decisions

---

## 🚨 Common OWASP Top 10 Vulnerabilities

---

## 1️⃣ Broken Access Control

Access controls restrict what users can do.

**Risk:** Users gain unauthorized access to data or systems.

**Example:**

* A user can delete content they should only view

### 🕵️ SOC Scenario

* Logs show normal user accessing admin endpoint
* SOC identifies access control failure
* Issue escalated for immediate fix

---

## 2️⃣ Cryptographic Failures

Sensitive data must be protected using strong encryption.

**Risk:** Data exposure due to weak or missing encryption

**Example:**

* Using weak hashing algorithms like MD5

### 🕵️ SOC Scenario

* Database breach detected
* Investigation shows plaintext PII stored
* SOC flags compliance violation (e.g., GDPR)

---

## 3️⃣ Injection

Injection occurs when malicious code is sent into an application.

**Risk:** Attackers gain unauthorized control over systems

**Example:**

* SQL injection through login form

### 🕵️ SOC Scenario

* Unusual database queries detected
* SOC traces activity to vulnerable input field
* Application patched

---

## 4️⃣ Insecure Design

Applications lack built-in security controls.

**Risk:** Systems are fragile and easily exploited

### 🕵️ SOC Scenario

* Repeated attacks succeed despite patches
* SOC identifies missing security controls
* Secure redesign recommended

---

## 5️⃣ Security Misconfiguration

Security settings are improperly configured.

**Risk:** Attackers exploit default or weak configurations

**Example:**

* Default credentials left unchanged

### 🕵️ SOC Scenario

* External scan finds open admin panel
* SOC confirms misconfiguration
* Configuration hardened

---

## 6️⃣ Vulnerable and Outdated Components

Applications rely on third-party libraries.

**Risk:** Known vulnerabilities introduced via dependencies

### 🕵️ SOC Scenario

* SCA tool flags outdated library
* SOC blocks deployment
* Dependency updated

---

## 7️⃣ Identification and Authentication Failures

Applications fail to properly verify user identity.

**Risk:** Account takeover

### 🕵️ SOC Scenario

* Multiple logins from different regions
* MFA not enforced
* SOC escalates authentication failure

---

## 8️⃣ Software and Data Integrity Failures

Updates or patches are not validated.

**Risk:** Supply chain attacks

**Example:** SolarWinds attack (2020)

### 🕵️ SOC Scenario

* Malicious update detected
* SOC isolates affected systems
* Incident declared

---

## 9️⃣ Security Logging and Monitoring Failures

Insufficient logging and monitoring.

**Risk:** Attacks go undetected

### 🕵️ SOC Scenario

* Breach discovered weeks later
* Logs missing critical data
* Monitoring strategy updated

---

## 🔟 Server-Side Request Forgery (SSRF)

Attackers manipulate server requests.

**Risk:** Unauthorized access to internal resources

### 🕵️ SOC Scenario

* Server makes unexpected internal requests
* SOC identifies SSRF attack
* Input validation enforced

---

## 🔑 Key Takeaways 

* OWASP Top 10 focuses on web application risks
* Used heavily during application design
* Complements CVE, not replaces it
* Helps prevent common, high-impact attacks
* SOC teams reference OWASP for testing and monitoring

---

✍️ **Notes by Abhishek (Ez Abyss)**
