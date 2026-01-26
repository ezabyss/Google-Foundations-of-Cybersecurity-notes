# CIA Triad & NIST Cybersecurity Framework  
_Notes by Abhishek (EzAbyss)_

---

## 🔐 1. Introduction

this lesson focuses on **specific, widely used security principles**:

- The **CIA Triad**
- The **NIST Cybersecurity Framework (NIST CSF)**
- How these help organizations reduce risks and protect assets

These concepts form the foundation of nearly every security policy, interview question, and analyst workflow.

---

# 🧩 2. The CIA Triad

The **CIA Triad** is a foundational model used to guide security decision-making.

It stands for:

## **C – Confidentiality**  
Only **authorized people** can access data.

### How to ensure confidentiality:
- Access controls (RBAC / least privilege)
- MFA & authentication
- Encryption (protecting data at rest/in transit)
- Secure permissions

Example:  
Only HR employees should access payroll data — everyone else is denied.

---

## **I – Integrity**  
Data must remain **accurate, authentic, and unmodified** unless changed by authorized users.

### How to ensure integrity:
- Encryption  
- Hashing  
- Version control  
- Audit logs  
- Checksums  

Example:  
If malware modifies bank transaction logs, integrity is lost.

---

## **A – Availability**  
Authorized users must have **reliable access** to data and systems when needed.

### How to ensure availability:
- Backups  
- Redundancy  
- Load balancing  
- DDoS protection  
- System maintenance  

Example:  
If customers can’t access your banking app, availability is broken.

---

# 💡 3. What Is an Asset?

An **asset** = anything with value to an organization.

Value is determined by:

- Sensitivity of the data  
- Cost to replace  
- Impact if compromised  

### Examples:
- High-value asset → Database storing SSNs or bank accounts  
- Low-value asset → Public news blog  

Higher value = stricter security controls.

---

# 🏛️ 4. NIST Cybersecurity Framework (NIST CSF)

The **NIST CSF** is a *voluntary*, widely used framework from the  
**National Institute of Standards and Technology (U.S.)**.

It provides:

- Standards  
- Guidelines  
- Best practices  

Purpose:  
**To help organizations manage and reduce cybersecurity risk.**

### Why NIST CSF matters:
- Used by government, enterprises, and security teams worldwide  
- Helps analysts manage **short-term and long-term risk**  
- Aligns security with business goals  
- Reduces chances of data breaches  
- Ensures consistent, repeatable processes  

---

# 👥 5. Threat Actors & Frameworks Working Together

Understanding a threat actor’s **motivation** + understanding your **most valuable assets** helps analysts make effective security decisions.

Example of dangerous insider threat:

### ⚠️ Disgruntled Employees  
They:
- Already have access  
- Know where sensitive data is stored  
- Understand internal systems  

To reduce this risk:

- Apply **availability + least privilege**
- Ensure employees access **only what they need**
- Use guidelines defined through frameworks like NIST CSF

---

# 🌍 6. Importance of Diversity in Security Teams

Attacks originate from around the world → diverse teams help:

- Identify attacker behavior  
- Understand cultural context  
- Spot global threat patterns  
- Improve defensive
