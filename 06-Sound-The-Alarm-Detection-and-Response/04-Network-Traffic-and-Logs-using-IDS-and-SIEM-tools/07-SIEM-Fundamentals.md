# 📊 SIEM Fundamentals: Log Ingestion & Data Access
*Thinking Like a Security Analyst*

---

## 🧠 Why SIEM Matters
As a security analyst, **speed, scale, and visibility** are everything.

You’ll constantly need to:
- Triage alerts
- Monitor systems
- Investigate incidents
- Correlate events across many systems

A **SIEM (Security Information and Event Management)** platform exists to make this possible.

> A SIEM is the **central nervous system** of a SOC.

---

## 🔍 What Is a SIEM?
A SIEM is a security platform that:
- Collects log data from many sources
- Normalizes data into a common structure
- Indexes events for fast search
- Correlates activity to detect threats

---

## 🔄 SIEM Process Overview

Every SIEM follows the same **three core stages**:

| Stage | Purpose |
|-----|--------|
| Collect & Aggregate | Gather logs from systems and devices |
| Normalize | Convert logs into a consistent format |
| Analyze & Index | Enable search, correlation, and detection |

This transforms **raw noise → actionable intelligence**.

---

## 📥 Log Ingestion (The Foundation)
A SIEM is only as strong as the **data it ingests**.

### Log ingestion
Log ingestion is the process of **collecting and importing log data** from log sources into a SIEM platform.

📌 Important:
- The SIEM stores a **copy** of logs
- Original logs remain unchanged
- Analysis occurs on ingested data

---

## 🧾 Common Log Sources

| Source | Example Events |
|-----|---------------|
| Endpoints | Process execution |
| Servers | Authentication attempts |
| Firewalls | Allowed / blocked traffic |
| IDS / IPS | Alerts & signatures |
| Applications | Errors, access logs |
| Cloud platforms | API calls, identity activity |

---

## 🧠 Why Normalization Is Critical
Logs come in **many formats**.

Example:
- Windows logs ≠ Firewall logs ≠ Application logs

### Normalization:
- Converts logs into a **standard schema**
- Extracts relevant security fields
- Makes correlation possible

Without normalization:
> Analysts spend time decoding logs instead of stopping attacks.

---

## 📌 Indexing: Analyst Speed
After normalization, SIEMs **index the data**.

Indexing allows:
- Fast searching across millions of events
- Pivoting between related logs
- Timeline reconstruction during incidents

📎 Think of indexing like a **search engine for security data**.

---

## 🚚 Log Forwarders (How Data Reaches SIEM)

Manually uploading logs doesn’t scale.

### Log forwarders
Log forwarders are agents or services that:
- Collect logs automatically
- Forward them to a SIEM
- Run continuously

---

## 🔧 Types of Log Forwarders

| Type | Description |
|----|------------|
| Native | Built into OS or services |
| Third-party | Installed separately |
| Vendor-specific | Designed for a SIEM platform |

📌 Examples:
- Splunk Universal Forwarder
- Google SecOps ingestion pipelines

---

## 🧠 Why Log Forwarders Matter
They:
- Automate data collection
- Reduce analyst overhead
- Enable near real-time detection
- Support large environments

Without them:
> Visibility gaps appear, and incidents go undetected.

---

## 🛠️ Modern SIEM Platforms

### 🔹 Splunk Enterprise Security
- Data analytics and SIEM platform
- Uses indexes for searching
- Powerful query language
- Flexible dashboards and alerts

---

### 🔹 Google Security Operations (formerly Chronicle)
**Chronicle has been rebranded as Google Security Operations (Google SecOps).**

Key characteristics:
- Cloud-native SIEM by Google
- Massive scale and long-term retention
- Automatic normalization
- Optimized for threat hunting and correlation
- Deep integration with Google Cloud

📌 Data flow:
Logs → ingestion pipelines → normalization → indexed search

---

## 🧠 SOC Analyst Mental Model

| Without SIEM | With SIEM |
|------------|----------|
| Disconnected logs | Centralized visibility |
| Manual review | Automated correlation |
| Slow investigations | Rapid response |
| Missed patterns | Clear attack narratives |

---

## ✅ Key Takeaways
- SIEMs centralize and correlate security data
- Log ingestion is the foundation
- Normalization enables efficient analysis
- Log forwarders scale data collection
- **Google Security Operations is the current name for Chronicle**
- SIEM proficiency is a **core SOC skill**

---

**✍️ Notes By Abhishek (Ez Abyss)**
