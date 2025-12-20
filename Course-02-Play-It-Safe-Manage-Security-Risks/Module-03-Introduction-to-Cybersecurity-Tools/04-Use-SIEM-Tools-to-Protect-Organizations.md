# 🛡️ Using SIEM Tools to Protect Organizations

**Notes By Abhishek (Ez Abyss)**

> Understand how security analysts use SIEM dashboards—specifically **Splunk** and **Chronicle**—to identify threats, risks, and vulnerabilities and protect organizational assets.

---

## 🌐 Overview

SIEM tools are not just for collecting logs.  
They provide **dashboards** that help cybersecurity professionals:
- Monitor security events
- Detect suspicious activity
- Prioritize risks
- Respond to incidents efficiently

Dashboards organize complex log data into **visual, actionable insights**.

---

## 🔎 SIEM Tools in Focus

Here, we explore how two common SIEM tools are used in real security operations:
Both tools allow analysts to monitor organizational activity through dashboards.

---

## 🧰 Splunk SIEM Dashboards

Splunk provides **Splunk Enterprise** and **Splunk Cloud**, both of which use dashboards to:
- Collect and analyze logs from multiple sources
- Provide full visibility into daily operations
- Support threat detection and incident response

---

### 🛡️ Security Posture Dashboard

**Purpose:**
- Designed for Security Operations Centers (SOCs)
- Displays the last **24 hours of notable security events**

**How analysts use it:**
- Monitor real-time threats
- Detect suspicious network activity
- Verify whether security controls and policies are working as designed

---

### 📊 Executive Summary Dashboard

**Purpose:**
- Monitors overall organizational security health over time

**How analysts use it:**
- Generate high-level summaries for stakeholders
- Identify long-term trends in incidents and risk
- Support strategic security decisions

---

### 🚨 Incident Review Dashboard

**Purpose:**
- Helps identify suspicious patterns during incidents

**How analysts use it:**
- Review a visual timeline of events leading up to an incident
- Highlight high-risk items needing immediate investigation
- Understand attacker behavior and incident progression

---

### ⚠️ Risk Analysis Dashboard

**Purpose:**
- Identifies risk levels for specific **risk objects**:
  - Users
  - Computers
  - IP addresses

**How analysts use it:**
- Detect unusual behavior (e.g., logins outside working hours)
- Monitor spikes in network traffic
- Prioritize mitigation efforts for critical assets

---

## ☁️ Chronicle SIEM Dashboards
**cloud-native SIEM tool** from Google that:
- Retains large volumes of log data
- Analyzes threats at scale
- Supports fast and flexible investigations

Chronicle allows log analysis by:
- Asset
- Domain name
- User
- IP address

---

### 🔍 Enterprise Insights Dashboard

**Purpose:**
- Highlights recent alerts
- Identifies Indicators of Compromise (IOCs)

**How analysts use it:**
- Review suspicious domain names
- Evaluate alerts using confidence scores and severity levels
- Monitor access attempts to critical assets from unusual locations or devices

---

### 📥 Data Ingestion & Health Dashboard

**Purpose:**
- Displays log ingestion status and system health

**How analysts use it:**
- Verify log sources are correctly configured
- Ensure logs are processed successfully
- Detect ingestion failures that could cause blind spots

---

### 🧬 IOC Matches Dashboard

**Purpose:**
- Identifies top threats, risks, and vulnerabilities

**How analysts use it:**
- Track IOCs (domains, IPs, devices) over time
- Identify threat trends
- Focus on the highest-priority risks

---

### 🧾 Main Dashboard

**Purpose:**
- Provides a high-level summary of:
  - Alerts
  - Events
  - Data ingestion

**How analysts use it:**
- Review timelines of security activity
- Detect spikes in failed logins or abnormal behavior
- Identify trends across locations, devices, and users

---

### 👤 User Sign-In Overview Dashboard

**Purpose:**
- Displays user authentication behavior across the organization

**How analysts use it:**
- Detect unusual login behavior
- Identify impossible travel scenarios
- Protect user accounts and applications

---

### 📏 Rule Detections Dashboard

**Purpose:**
- Shows statistics on incidents by:
  - Frequency
  - Severity
  - Detection rules

**How analysts use it:**
- Review alerts triggered by specific rules
- Manage recurring incidents
- Improve mitigation strategies to reduce risk

---

## 🧠 Key Takeaways

- SIEM dashboards help analysts focus on what matters most
- Splunk dashboards support SOC operations and risk management
- Chronicle dashboards enable large-scale, cloud-based threat analysis
- Dashboards visualize trends, timelines, and severity
- SIEM tools reduce risk by enabling faster detection and response
- Prioritization is essential for effective security operations

---
Mastering SIEM dashboards is a **core skill for entry-level security analysts**.
---
