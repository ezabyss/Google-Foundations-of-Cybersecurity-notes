# 🚨 Incident Lifecycle Frameworks & Incident Fundamentals  

---

## 1️⃣ Why Incident Lifecycle Frameworks Matter

**Incident lifecycle frameworks** provide a structured way to handle security incidents so that responses are:

- Consistent  
- Effective  
- Repeatable  
- Well-documented  

Without a framework, incident response becomes **reactive, chaotic, and error-prone**.

Frameworks help organizations:
- Standardize incident response operations
- Clearly define roles and responsibilities
- Reduce response time
- Improve recovery and learning after incidents

Organizations can **adopt and adapt** frameworks based on their size, risk profile, and industry.

---

## 2️⃣ The NIST Cybersecurity Framework (CSF)

In this course, the primary framework is the **NIST Cybersecurity Framework (CSF)**.

The **Six core functions** of the NIST CSF are:

1. **Govern**
2. **Identify**
3. **Protect**
4. **Detect**
5. **Respond**
6. **Recover**

📌 This course focuses on the **last three functions**, which are most relevant to SOC analysts:
- Detect
- Respond
- Recover

These stages represent **active incident response work**.

---

## 3️⃣ From CSF to the NIST Incident Response Lifecycle

While the CSF provides a **high-level security strategy**, the **NIST Incident Response Lifecycle** goes deeper into **operational incident handling**.

### NIST Incident Response Lifecycle Phases

1. **Preparation**
2. **Detection and Analysis**
3. **Containment, Eradication, and Recovery**
4. **Post-Incident Activity**

⚠️ Important note:  
This lifecycle is **not linear**. It is a **cycle**, meaning:
- Steps may overlap
- Analysts may return to earlier stages as new information emerges

This mirrors real-world incident response, where investigations evolve continuously.

---

## 4️⃣ What Is a Security Incident?

According to NIST, an incident is:

> *“An occurrence that actually or imminently jeopardizes, without lawful authority, the confidentiality, integrity, or availability of information or an information system; or constitutes a violation or imminent threat of violation of law, security policies, security procedures, or acceptable use policies.”*

Let’s simplify this.

---

## 5️⃣ Events vs. Security Incidents (Critical Distinction)

### 🔹 What is an Event?
An **event** is any **observable occurrence** on a:
- Network
- System
- Application
- Device

📌 Events are logged and monitored.

#### Example (Normal Event)
- A user forgets their email password
- Requests a password reset
- Successfully resets it

✅ This is an event  
❌ This is **not** a security incident  
Why? No policy violation occurred.

---

### 🔹 What is a Security Incident?
A **security incident** is an event that:
- Violates security policy  
- Threatens confidentiality, integrity, or availability  
- Involves malicious or unauthorized activity  

#### Example (Security Incident)
- A malicious actor initiates a password reset
- Gains access to someone else’s account
- Changes the password without authorization

✅ This is an event  
✅ This **is** a security incident  

📌 **Key rule to remember:**  
> All security incidents are events, but not all events are security incidents.

---

## 6️⃣ The Analyst’s Role During an Incident

Security analysts act like **digital detectives**.

Their job is to:
- Investigate carefully
- Preserve evidence
- Document every finding

An incident investigation focuses on the **Five W’s**:

- **Who** triggered the incident?
- **What** happened?
- **When** did it occur?
- **Where** did it take place?
- **Why** did it happen?

These questions guide:
- Incident response actions
- Reporting
- Lessons learned

---

## 7️⃣ Importance of Documentation

Accurate documentation is essential for:
- Incident tracking
- Legal and compliance needs
- Final incident reports
- Improving future response efforts

### 📓 Incident Handler’s Journal

An **incident handler’s journal** is a personal documentation method used by analysts to record:

- Observations
- Timeline details
- Indicators of compromise (IOCs)
- Decisions made
- Questions and hypotheses

Throughout this course, you are expected to **maintain your own incident handler’s journal**.

📌 This habit builds:
- Strong investigative skills
- Clear thinking under pressure
- Professional incident reporting ability

---

## 🔑 Key Takeaways

- Incident frameworks standardize response operations
- NIST CSF provides strategic guidance
- The NIST Incident Response Lifecycle supports operational response
- Incident response is cyclical, not linear
- Events are not always incidents
- Analysts investigate incidents using the Five W’s
- Documentation is critical for response and recovery

---

**✍️ Notes By Abhishek (Ez Abyss)**
