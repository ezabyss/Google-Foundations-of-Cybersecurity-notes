# 🔄 The Data Lifecycle & Data Governance  
*Protecting Information from Creation to Destruction*

---

## 🌍 Why the Data Lifecycle Matters
Organizations of all sizes handle **massive amounts of data** every day.  
This data is vulnerable whether it is:
- **At rest**
- **In use**
- **In transit**

Regardless of state, information must be protected by:
- Limiting access
- Controlling authorization
- Applying appropriate security controls

---

## 🔐 Data & the CIA Triad
Protecting data throughout its lifecycle supports:
- **Confidentiality** → Prevents unauthorized access
- **Integrity** → Prevents unauthorized changes
- **Availability** → Ensures data is accessible when needed

---

## 🔄 What Is the Data Lifecycle?
The **data lifecycle** is a security model that maps how data:
- Enters an organization
- Is used and stored
- Eventually becomes obsolete and is removed

Security teams use this model to:
- Design policies
- Choose technologies
- Align security with business goals

---

## 🧩 The Five Stages of the Data Lifecycle

Data flows through **five stages**:

1. **Collect**
2. **Store**
3. **Use**
4. **Archive**
5. **Destroy**

> Protecting data at each stage ensures it remains **secure, accessible, and recoverable**.

---

## 1️⃣ Collect
Data is gathered from:
- Customers
- Employees
- Partners
- External systems

📌 Examples:
- Signup forms
- Payment information
- Medical records

### 🧠 SOC Scenario: Data Collection
**Situation:**  
A web form collects more personal data than required.

**Risk:**  
- Unnecessary exposure
- Privacy violation

**SOC Action:**  
- Flag excessive data collection
- Recommend data minimization

---

## 2️⃣ Store
Collected data is stored on:
- Databases
- Servers
- Cloud storage
- Backup systems

### Security Focus:
- Encryption
- Access controls
- Secure configurations

### 🧠 SOC Scenario: Data Storage
**Situation:**  
SOC detects a publicly accessible cloud storage bucket.

**Risk:**  
- Data leakage

**Action:**  
- Restrict access immediately
- Audit storage permissions

---

## 3️⃣ Use
Data is actively accessed, processed, or modified.

📌 Examples:
- Customer support viewing records
- Systems processing transactions

### 🧠 SOC Scenario: Data in Use
**Situation:**  
Employee accesses sensitive data outside business hours.

**Risk:**  
- Insider threat
- Account compromise

**Action:**  
- Investigate access logs
- Enforce least privilege

---

## 4️⃣ Archive
Data that is no longer actively used but still needed for:
- Legal
- Regulatory
- Business reasons

### Security Focus:
- Long-term protection
- Restricted access
- Integrity preservation

### 🧠 SOC Scenario: Archived Data
**Situation:**  
Archived customer data accessed unexpectedly.

**Risk:**  
- Policy violation

**Action:**  
- Review access controls
- Confirm business justification

---

## 5️⃣ Destroy
Data that is no longer needed must be:
- Securely deleted
- Rendered unrecoverable

📌 Examples:
- Secure wiping
- Cryptographic erasure
- Physical destruction

### 🧠 SOC Scenario: Data Destruction
**Situation:**  
Old drives disposed of without proper wiping.

**Risk:**  
- Data recovery by attackers

**Action:**  
- Enforce secure destruction procedures
- Review disposal policies

---

## 🧭 Data Governance (How Data Is Managed)

### 📌 Definition
**Data governance** is a set of processes that define how data is:
- Managed
- Protected
- Kept accurate
- Made available

Governance applies **across the entire data lifecycle**.

---

## 👥 Key Data Governance Roles

### 👤 Data Owner
- Decides who can access, use, edit, or destroy data
- Responsible for data classification

---

### 🧰 Data Custodian
- Safely handles, stores, and transports data
- Can be a person, system, or service

📌 *As a security professional, this is often your primary role.*

---

### 🧭 Data Steward
- Implements and maintains governance policies
- Ensures rules are followed organization-wide

---

### 🧠 SOC Scenario: Governance Breakdown
**Situation:**  
Unclear ownership leads to delayed breach response.

**Lesson:**  
Clear roles = faster, safer decisions.

---

## 📜 Data Governance Policies
Most organizations define a **data governance policy** that:
- Specifies how data must be handled
- Limits access and usage
- Defines procedures for protection

Security professionals help:
- Enforce policies
- Monitor compliance
- Prevent misuse

---

## ⚖️ Legally Protected Information
Data often represents:
- Personal identity
- Medical decisions
- Financial activity

Because of this, **data owners’ privacy choices must be respected**.

Governments define data types that require protection **by default**.

---

## 🧾 Types of Sensitive Data

### 🪪 PII — Personally Identifiable Information
Information that can identify an individual:
- Name
- Address
- Phone number
- Email

---

### 🏥 PHI — Protected Health Information
Health-related data:
- Medical records
- Diagnoses
- Treatment history

📌 Regulated by:
- HIPAA (U.S.)
- GDPR (EU)

---

### 🔐 SPII — Sensitive Personally Identifiable Information
A stricter subset of PII:
- Bank account numbers
- Login credentials
- Social security numbers

📌 Accessed strictly on a **need-to-know basis**.

---

## 🧠 SOC Scenario: Protected Data Exposure
**Situation:**  
SOC detects leaked credentials in logs.

**Data Type:**  
SPII

**Action:**  
- Immediate containment
- Regulatory notification
- Credential reset

---

## 🎯 Key Takeaways

- Data is vulnerable at every stage of its lifecycle
- The data lifecycle has five stages: collect, store, use, archive, destroy
- Data governance defines how data is managed and protected
- Data owners decide access
- Data custodians protect data
- Data stewards enforce policies
- PII, PHI, and SPII require extra protection
- SOC teams protect data across the entire lifecycle

---

✍️ **Notes By Abhishek (Ez Abyss)**
