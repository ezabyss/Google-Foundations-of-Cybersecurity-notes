# 🌐 Vulnerabilities, Exposures & the CVE Ecosystem

---

## 🤝 Security Is a Global Team Effort

Protecting information is not limited to a single security team or organization.

* Researchers
* Vendors
* Ethical hackers
* Governments
* Security analysts worldwide

All contribute to identifying and sharing security risks.

> 🌍 Cybersecurity improves when knowledge is shared globally.

---

## ⚠️ Vulnerability vs Exposure (Key Difference)

### 🔓 Vulnerability

* A **weakness in a system**
* Exists even if no mistake is made

**Example:** Software with a coding flaw

---

### 🚪 Exposure

* A **mistake or misconfiguration** that can be exploited

**Example Analogy:**

* A document can be misplaced (vulnerability)
* Leaving it near an open window is an **exposure**

> 🧠 Exposures are often caused by human error.

---

## 📚 What Is the CVE List?

The **Common Vulnerabilities and Exposures (CVE) list** is a public dictionary of known:

* Vulnerabilities
* Exposures

It provides a **standard naming system** so security teams can communicate clearly.

---

## 🏛️ Origin of the CVE List

* Created in **1999**
* Developed by **MITRE Corporation**
* MITRE operates nonprofit research centers
* Sponsored by the **U.S. government**

**Goal:** Improve global security technologies through shared knowledge.

---

## 🆔 How a CVE Is Created

Anyone can report a vulnerability, but not all reports become CVEs.

A reported issue must be reviewed by a **CVE Numbering Authority (CNA)**.

### 🧪 CVE Qualification Criteria

A vulnerability must meet **all four** conditions:

1️⃣ **Independent** – Can be fixed on its own
2️⃣ **Recognized as a security risk**
3️⃣ **Supported by evidence**
4️⃣ **Affects only one codebase**

If approved, it receives a **CVE ID** (e.g., CVE-2024-XXXX).

---

## 🕵️ SOC Scenario: CVE Identification

* SOC analyst reviews vulnerability report
* Confirms issue affects a single application
* Evidence submitted to CNA
* CVE ID assigned

➡️ **SOC Role:** Track and document known vulnerabilities

---

## 📊 Beyond CVE: Severity Analysis

Once listed, vulnerabilities are often reviewed by other databases to determine **severity and impact**.

One of the most widely used is the **NIST National Vulnerability Database (NVD)**.

---

## 📏 CVSS: Common Vulnerability Scoring System

**CVSS** is a scoring system used to measure the **severity** of vulnerabilities.

* Scale: **0.0 – 10.0**
* Provided by NIST NVD
* Base score does **not change over time**

### 🧮 CVSS Score Interpretation

* **0.0 – 3.9:** Low risk
* **4.0 – 6.9:** Medium risk
* **7.0 – 8.9:** High risk
* **9.0 – 10.0:** Critical risk

---

## 🕵️ SOC Scenario: CVSS-Based Prioritization

* New CVE published with CVSS score of **9.8**
* SOC flags it as critical
* Patch scheduled immediately
* Monitoring increased until fix is applied

➡️ **SOC Role:** Prioritize remediation based on severity

---

## 🛠️ How Security Teams Use CVE & CVSS

Security teams rely on CVE and CVSS to answer:

* Is this vulnerability dangerous?
* How severe is the risk?
* How quickly should it be fixed?

These tools support:

* Vulnerability management
* Patch prioritization
* Risk-based decision making

---

## 🌍 Value of Public Vulnerability Libraries

* Bring together diverse global expertise
* Improve transparency
* Strengthen defenses across organizations

> 🤝 Sharing vulnerabilities helps protect everyone.

---

## ✅ Key Takeaways

* Vulnerabilities are system weaknesses
* Exposures are mistakes that increase risk
* CVE provides standard identification
* CNA reviews vulnerabilities before listing
* CVSS scores help prioritize fixes
* SOC teams use CVE and CVSS daily

---

✍️ **Notes by Abhishek (Ez Abyss)**
