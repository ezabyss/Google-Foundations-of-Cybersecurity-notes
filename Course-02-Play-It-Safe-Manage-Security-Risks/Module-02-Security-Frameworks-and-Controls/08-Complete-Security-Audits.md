# 🔍 Internal Security Audits

## Controls Assessment, Compliance, and Communication

**Notes by Abhishek (Ez Abyss)**

---

## 🌐 Where We Are in the Audit Process

An **internal security audit** helps organizations evaluate how well their security controls, policies, and procedures protect assets and data.

### Audit Elements Recap

Internal security audits include **five main elements**:

1. Establishing scope and goals
2. Conducting a risk assessment
3. Completing a controls assessment
4. Assessing compliance
5. Communicating results

📌 *This note focuses on the **last three elements**, which entry-level analysts commonly support.*

---

## 🧠 Questions to Ask Before Continuing

Before moving forward, analysts should review the scope, goals, and risk assessment and ask:

* What is the audit meant to achieve?
* Which assets are most at risk?
* Are current controls sufficient?
* If not, what new controls or regulations are required?

These questions guide the remaining audit steps.

---

## 3️⃣ Controls Assessment

### 🔐 What Is a Controls Assessment?

A **controls assessment** is a detailed review of:

* Existing organizational assets
* Risks to those assets
* Effectiveness of current controls and processes

The goal is to determine whether controls adequately reduce identified risks.

---

### 🗂️ Types of Security Controls

Entry-level analysts may be asked to classify controls into three categories:

#### 🧑‍💼 Administrative Controls

Controls related to **people, policies, and procedures**.

**Examples:**

* Password policies
* Access policies
* Security training procedures

---

#### 💻 Technical Controls

Controls that use **hardware or software** to protect assets.

**Examples:**

* Intrusion Detection Systems (IDS)
* Encryption
* Firewalls

---

#### 🏢 Physical Controls

Controls that prevent **physical access** to protected assets.

**Examples:**

* Surveillance cameras
* Locks
* Secured doors or badge access

📌 *Effective security requires all three control types working together.*

---

## 4️⃣ Compliance Assessment

### 📜 What Is Compliance?

**Compliance regulations** are laws and standards organizations must follow to protect private data.

### Example Compliance Requirements

If an organization:

* Operates in the European Union → **GDPR**
* Accepts credit card payments → **PCI DSS**

The audit evaluates whether current controls meet these regulatory requirements.

📌 *Failure to comply can result in fines, penalties, and reputational damage.*

---

## 5️⃣ Communicating Audit Results

### 📢 Why Communication Matters

Once the audit is complete, findings must be shared with **stakeholders**.

### What Audit Communication Includes

* Summary of audit scope and goals
* Identified risks and their severity
* Timeline for addressing risks
* Required compliance regulations
* Recommendations to improve security posture

📌 *Clear communication turns audit findings into action.*

---

## 🧑‍💼 Real-World Example

An internal password audit revealed:

* Many employee passwords were weak

**Result:**

* The compliance team enforced stricter password policies

📌 *Audits help uncover gaps and drive meaningful security improvements.*

---

## 🎯 Why Internal Audits Are Valuable

Internal security audits:

* Identify gaps in controls and processes
* Improve compliance and security posture
* Reduce organizational risk
* Support continuous improvement

They are also valuable **portfolio-building experiences** for entry-level analysts.

---

## 🧠 Memory Hook

**Controls → Compliance → Communication**

If you remember this order, you remember the final audit steps.

---

## ✅ Key Takeaways

* Controls assessments evaluate effectiveness of safeguards
* Controls fall into administrative, technical, and physical categories
* Compliance assessments ensure legal and regulatory adherence
* Clear communication is essential after audits
* Internal audits are critical learning opportunities for analysts

---

---

## 📘 More About Security Audits

### 🔍 What Is a Security Audit?

A **security audit** is an independent review of an organization’s:

* Security controls
* Policies
* Procedures

These are evaluated against a set of **expectations and criteria**.

#### Types of Criteria

* **Internal criteria:** Organizational policies, procedures, and best practices
* **External criteria:** Laws, regulations, and compliance standards

Audits also assess whether **security controls**—safeguards designed to reduce specific risks—are working as intended.

---

## 🎯 Goals and Objectives of Security Audits

### 🎯 Goal

To ensure an organization’s IT and security practices meet:

* Industry standards
* Organizational standards

### 🧭 Objective

To:

* Identify security gaps and failures
* Define areas needing remediation
* Create a clear plan for improvement

Audits help organizations:

* Safeguard sensitive data
* Avoid penalties and fines
* Maintain compliance with governing agencies

📌 *Audit frequency depends on local laws and federal compliance requirements.*

---

## 🧩 Factors That Affect Security Audits

The type and scope of audits depend on:

* Industry type
* Organization size
* Applicable government regulations
* Geographic location
* Business decisions to follow specific compliance standards

---

## 🏗️ Role of Frameworks and Controls in Audits

Security frameworks and controls play a critical role in audits.

### 📐 Frameworks

Examples include:

* **NIST Cybersecurity Framework (CSF)**
* **ISO/IEC 27000 series**

Frameworks help organizations:

* Prepare for audits
* Align with regulatory requirements
* Reduce time spent during internal and external audits

### 🔐 Controls

Controls are used alongside frameworks to enforce security.

Three main control categories reviewed during audits:

* **Administrative / Managerial controls**
* **Technical controls**
* **Physical controls**

---

## 📋 Audit Checklist (High-Level)

Creating an audit checklist is essential before conducting an audit.

### 1️⃣ Identify the Scope of the Audit

The audit should:

* List assets that will be assessed (e.g., firewalls, PII, physical assets)
* Explain how the audit supports organizational goals
* Define how often audits should be performed
* Evaluate policies, protocols, and procedures for effectiveness

---

### 2️⃣ Complete a Risk Assessment

A risk assessment evaluates organizational risks related to:

* Budget
* Existing controls
* Internal processes
* External standards and regulations

---

### 3️⃣ Conduct the Audit

* Assess the security of assets defined in the scope
* Verify whether controls are implemented correctly

---

### 4️⃣ Create a Mitigation Plan

A mitigation plan is a strategy to:

* Reduce risk levels
* Minimize potential costs, penalties, or operational impact
* Improve overall security posture

---

### 5️⃣ Communicate Results to Stakeholders

The final audit report includes:

* Detailed findings
* Recommended improvements
* Identified risks and urgency levels
* Required compliance regulations and standards

---

## 🧩 Control Categories (Detailed Reference)

Security controls are grouped into **three main categories**. During audits, analysts review all three to ensure *defense in depth*.

### 🧑‍💼 Administrative / Managerial Controls

Controls focused on **people, policies, and procedures**.

| Control Name                | Control Type | Purpose                                                      |
| --------------------------- | ------------ | ------------------------------------------------------------ |
| Least Privilege             | Preventative | Reduces impact of malicious insiders or compromised accounts |
| Disaster Recovery Plans     | Corrective   | Provide business continuity                                  |
| Password Policies           | Preventative | Reduce brute-force and dictionary attacks                    |
| Access Control Policies     | Preventative | Define who can access or modify data                         |
| Account Management Policies | Preventative | Manage account lifecycle and reduce attack surface           |
| Separation of Duties        | Preventative | Prevent abuse by limiting excessive privileges               |

---

### 💻 Technical Controls

Controls implemented using **hardware and software solutions**.

| Control Name                    | Control Type | Purpose                                   |
| ------------------------------- | ------------ | ----------------------------------------- |
| Firewall                        | Preventative | Filter malicious or unwanted traffic      |
| IDS / IPS                       | Detective    | Detect and prevent anomalous traffic      |
| Encryption                      | Deterrent    | Protect confidentiality of sensitive data |
| Backups                         | Corrective   | Restore systems after incidents           |
| Password Management Tools       | Preventative | Reduce password fatigue and reuse         |
| Antivirus (AV) Software         | Corrective   | Detect and quarantine known threats       |
| Manual Monitoring & Maintenance | Preventative | Manage risks from outdated systems        |

---

### 🏢 Physical Controls

Controls that restrict **physical access** to assets.

| Control Name                | Control Type             | Purpose                              |
| --------------------------- | ------------------------ | ------------------------------------ |
| Time-Controlled Safe        | Deterrent                | Reduce physical attack opportunities |
| Adequate Lighting           | Deterrent                | Discourage unauthorized activity     |
| CCTV                        | Preventative / Detective | Deter and investigate incidents      |
| Locking Cabinets            | Preventative             | Protect network infrastructure       |
| Alarm Signage               | Deterrent                | Increase perceived risk to attackers |
| Locks                       | Preventative / Deterrent | Prevent unauthorized access          |
| Fire Detection & Prevention | Detective / Preventative | Protect physical infrastructure      |

---

## 🧠 Control Types (Quick Memory Table)

| Control Type | Purpose                                       |
| ------------ | --------------------------------------------- |
| Preventative | Stop incidents before they occur              |
| Detective    | Identify incidents during or after occurrence |
| Corrective   | Restore assets after incidents                |
| Deterrent    | Discourage attacks                            |

---

## 🧠 Memory Hook

**Audit Flow:**
Scope → Risk → Controls → Compliance → Mitigation → Communication

---

## ✅ Final Key Takeaways

* Security audits validate controls, policies, and compliance
* Audits help maintain and improve security posture
* Frameworks and controls simplify audit preparation
* Checklists ensure audits are structured and repeatable
* Audit experience is valuable for professional portfolios

---
