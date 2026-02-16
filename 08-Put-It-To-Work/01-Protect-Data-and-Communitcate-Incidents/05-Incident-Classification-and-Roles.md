# 🚨 Incident Classification & Escalation Roles  

---

# 🎯 Why Incident Classification Matters

Not all security incidents are the same.

Proper classification helps you:

✔ Determine severity  
✔ Decide urgency  
✔ Escalate correctly  
✔ Protect critical assets  

Misclassification = Delayed response = Bigger damage

---

# 🦠 1️⃣ Malware Infection

## Definition

A malware infection occurs when malicious software infiltrates an organization’s systems or network.

Malware is designed to:

- Disrupt operations
- Steal data
- Encrypt files
- Create backdoors
- Slow down systems

---

## Examples

- Phishing malware
- Trojan infections
- Spyware
- Worms
- Ransomware

---

## 🔥 High-Impact Example: Ransomware

Effects:

- Files encrypted
- Systems locked
- Business halted
- Ransom demanded

Impact:

- Financial loss
- Reputational damage
- Operational downtime

---

## 🚦 Escalation Rule

ALWAYS escalate malware infections.

Even minor infections can spread laterally.

---

# 🔐 2️⃣ Unauthorized Access

## Definition

Occurs when someone gains digital or physical access to a system without permission.

---

## Examples

- Brute force attack
- Compromised credentials
- Insider accessing restricted systems
- Stolen access card

---

## 🧠 Key Concept

Not all unauthorized access has equal urgency.

Escalation urgency depends on:

- Sensitivity of the system
- Type of data involved
- Business impact

Example:

Access to guest WiFi → Lower severity  
Access to payroll database → Critical severity  

---

## 🚦 Escalation Rule

All unauthorized access must be escalated.

Severity determines response speed.

---

# ⚠️ 3️⃣ Improper Usage

## Definition

Occurs when an employee violates acceptable use policies.

---

## Examples

- Installing unapproved software
- Accessing coworker’s files
- Using company software for personal business
- Sharing credentials

---

## ⚖️ Intent Matters — But Don’t Assume

Improper usage can be:

✔ Accidental  
✔ Due to unclear policy  
✔ Intentional misuse  

As an entry-level analyst:

You do NOT determine intent.

You escalate.

---

## 🚦 Escalation Rule

Always escalate improper usage to supervisor.

---

# 🧭 Escalation Decision Framework

Ask:

1. Is this malware?
2. Is this unauthorized access?
3. Is this policy violation?
4. What asset is affected?
5. What is the business impact?

Then escalate according to policy.

---

# 👥 Roles During Incident Escalation

Security escalation is collaborative.

Understanding roles helps you escalate correctly.

---

# 🏷 Data Owner

## Definition

The person who decides:

- Who can access data
- Who can modify data
- How data is classified
- When data can be destroyed

## Example

If someone accesses restricted software → escalate to software’s data owner.

---

# 🗂 Data Controller

## Definition

Determines:

- Why data is collected
- How it is processed
- How it is used
- Compliance with privacy laws

## Focus Area

Customer personal data.

If customer PII is at risk → escalate to data controller.

---

# 🏢 Data Processor

## Definition

Processes data on behalf of the controller.

Often a third-party vendor.

Responsible for:

- Implementing security controls
- Processing data securely

Escalation typically goes through vendor management oversight.

---

# 🔐 Data Custodian

## Definition

Implements and manages security controls.

Responsibilities:

- Grant/revoke access
- Monitor systems
- Strengthen controls
- Maintain storage policies

Custodians are notified when controls fail.

---

# 🛡 Data Protection Officer (DPO)

## Definition

Ensures organization complies with:

- Data protection laws
- Privacy regulations
- Internal policies

DPOs are notified when:

- PII exposure occurs
- Policy violations happen
- Compliance standards are breached

---

# 🧠 Escalation Flow (Simplified)

Entry-Level Analyst  
        ↓  
Supervisor / SOC Lead  
        ↓  
Relevant Data Role (Owner / Controller / Custodian / DPO)  
        ↓  
Engineering / Legal / Executive Team (if required)

---

# 📊 Real-World Scenario

Scenario:

Employee installs unauthorized software.

Potential Outcomes:

- Harmless
- Malware infection
- Data exfiltration risk

Escalation Path:

Analyst → Supervisor → Data Custodian → IT Security

---

# 🔥 Critical Reminder

You are not expected to:

- Decide punishment
- Investigate alone
- Determine legal impact

You ARE expected to:

✔ Recognize incident type  
✔ Follow escalation policy  
✔ Document clearly  
✔ Escalate promptly  

---

# 🎯 Key Takeaways

✔ Malware infections require immediate escalation  
✔ Unauthorized access severity depends on asset criticality  
✔ Improper usage must always be escalated  
✔ Understand organizational roles  
✔ Escalation is structured, not emotional  
✔ Entry-level analysts are the first defense layer  

---

# 💬 Insight

“Proper incident classification ensures the right stakeholders are engaged at the right time, minimizing risk and preserving organizational integrity.”

---

# 🏆 Final Principle

Correct classification  
+  
Timely escalation  
=  
Reduced organizational damage  

Security is teamwork.

---

**✍️ Notes By Abhishek (Ez Abyss)**
