# 📊 SIEM & SOAR: Alert Management and Incident Visibility  
**Incident Detection & Response | SOC Analyst Core Tools**

---

## 1️⃣ Where Do Alerts Go?

Detection tools like IDS, IPS, and EDR generate alerts—but **where do those alerts actually go?**

👉 This is where **SIEM (Security Information and Event Management)** tools come in.

A **SIEM** is a centralized platform that:
- Collects log data
- Analyzes events
- Provides visibility into security activity
- Generates alerts for analysts to investigate

Think of SIEM as the **central nervous system** of security operations.

---

## 2️⃣ SIEM Explained with a Simple Analogy

### 🚗 The Car Dashboard Analogy

A car has many components:
- Engine
- Tires
- Battery
- Fuel system

You don’t inspect each part manually.  
Instead, you rely on the **dashboard** to alert you when something is wrong.

🖥️ **SIEM works the same way**:
- Networks have thousands of systems and devices
- SIEM aggregates their activity
- Presents a centralized, high-level view
- Alerts analysts when something needs attention

---

## 3️⃣ What Is SIEM?

A **Security Information and Event Management (SIEM)** tool:
- Collects log data from multiple sources
- Analyzes activity in real time
- Detects suspicious or malicious behavior
- Sends alerts to security teams

SIEM enables **log analysis**, which is the process of examining logs to identify events of interest.

---

## 4️⃣ Why SIEM Tools Are Critical

### 🔍 Key Advantages of SIEM

#### ✅ Access to Event Data
- Ingests data from hundreds of systems
- Provides visibility into real-time and historical activity

#### ✅ Monitoring, Detection, and Alerting
- Continuously monitors environments
- Applies detection rules
- Generates alerts when rules are matched

#### ✅ Log Storage & Retention
- Stores historical data for investigations
- Supports compliance and audits
- Retention policies are customizable

📌 SIEM replaces manual log review with **centralized intelligence**.

---

## 5️⃣ The SIEM Process (3 Core Steps)

The SIEM workflow consists of **three critical stages**:

1. Collect and aggregate data  
2. Normalize data  
3. Analyze data  

---

## 6️⃣ Step 1: Collect & Aggregate Data

### 📥 Log Collection
SIEM tools ingest logs from sources such as:
- Firewalls
- IDS / IPS
- Servers
- Routers
- Databases
- Applications

Logs contain details like:
- Timestamps
- IP addresses
- Usernames
- Actions taken

### 🧩 Aggregation
Aggregation means:
- Centralizing logs from all sources into one location

📌 This eliminates the need to check systems individually.

---

### 🔎 Parsing (Part of Step 1)

Raw logs can be hard to read.

Example raw log:
April 3 11:01:21 server sshd[1088]: Failed password for user nuhara from 218.124.14.105 port 5023

Parsed log:
- host = server  
- process = sshd  
- source_user = nuhara  
- source_ip = 218.124.14.105  
- source_port = 5023  

Parsing maps **fields to values**, making logs easier to analyze.

---

## 7️⃣ Step 2: Normalize Data

Different systems generate logs in **different formats**.

Normalization:
- Converts raw data into a **standard, structured format**
- Ensures consistency across logs
- Makes searching and correlation easier

📌 Normalized data allows analysts to query logs efficiently during investigations.

---

## 8️⃣ Step 3: Analyze Data

Once data is collected, aggregated, and normalized, the SIEM performs **analysis**.

### 🔍 How Analysis Works
- SIEM applies detection rules and conditions
- If log activity matches a rule → alert is generated

### 🔗 Correlation
Correlation compares multiple log events to:
- Identify patterns
- Detect multi-stage attacks
- Reveal activity that looks benign in isolation

📌 Correlation is what turns **data into insight**.

---

## 9️⃣ Common SIEM Tools in the Industry

Popular SIEM platforms include:
- AlienVault OSSIM
- Chronicle
- Elastic
- Exabeam
- IBM QRadar
- LogRhythm
- Splunk

Each tool differs in scale, cost, and features, but the **core process remains the same**.

---

## 🔁 SOAR: Automating the Response

While SIEM focuses on **visibility and alerting**, **SOAR** focuses on **action**.

### What Is SOAR?

**Security Orchestration, Automation, and Response (SOAR)**:
- Automates analysis and response
- Executes workflows
- Manages cases and incidents

### SIEM vs SOAR

- **SIEM** → Collects, analyzes, alerts  
- **SOAR** → Automates response and case management  

📌 Multiple incidents can be grouped into a **case** within SOAR for centralized handling.

---

## 10️⃣ How SIEM & SOAR Work Together

1. Detection tools generate logs
2. SIEM collects and analyzes logs
3. Alerts are generated
4. SOAR automates response actions
5. Analysts review, refine, and escalate as needed

This integration improves:
- Response speed
- Consistency
- Analyst efficiency

---

## 🔑 Key Takeaways

- SIEM centralizes security visibility
- It collects, aggregates, normalizes, and analyzes log data
- SIEM enables real-time and historical investigations
- Correlation turns isolated events into meaningful alerts
- SOAR automates response and case management
- Together, SIEM and SOAR improve detection and response efficiency

---

**✍️ Notes By Abhishek (Ez Abyss)**
