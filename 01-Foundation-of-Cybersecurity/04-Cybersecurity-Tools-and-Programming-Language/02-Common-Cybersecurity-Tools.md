# Common Cybersecurity Tools  
_Notes by Abhishek (EzAbyss)_

---

## 🌩️ 1. Introduction: Security Is Like Preparing for a Storm

Cybersecurity can be compared to **preparing for a storm**.

If water starts leaking into your house:
- The **color or shape of the bucket doesn’t matter**
- What matters is **stopping the damage**

In the same way, in cybersecurity:
- The specific tool is less important than
- **How effectively it helps reduce risk and stop threats**

As an entry-level security analyst, you’ll have many tools in your toolkit.  
Your goal is to use them to **identify, assess, and mitigate risks**.

---

## 📄 2. What Are Logs?

Before understanding tools, we must understand **logs**.

### 🔹 Log (Definition)
A **log** is a record of events that occur within an organization’s systems.

### 🔹 Examples of security logs:
- Employee login records  
- Access to web-based services  
- System activity records  
- Network connections  

### 🔹 Why logs matter:
Logs help security professionals:
- Detect suspicious behavior  
- Identify vulnerabilities  
- Investigate security incidents  
- Confirm or rule out breaches  

Logs are the **raw data** that security tools organize and analyze.

---

# 📊 3. SIEM Tools (Security Information and Event Management)

### 🔹 What is a SIEM?
A **SIEM tool** collects and analyzes log data from multiple sources to monitor security-critical activity.



---

## 🔹 What SIEM Tools Do

- Collect logs from many systems  
- Analyze events in **real time**  
- Detect suspicious patterns  
- Generate alerts for potential threats  
- Reduce the amount of data analysts must manually review  

Without SIEM:
- Analysts may need hours or days to read logs  

With SIEM:
- Alerts highlight **only what matters**

---

## 🔹 Common SIEM Tools

### 🟦 Splunk
- Data analysis platform  
- **Splunk Enterprise** provides SIEM capabilities  
- Self-hosted  
- Used to store, search, and analyze log data  

### 🟩 Google Chronicle
- Cloud-native SIEM tool  
- Stores and analyzes security data in the cloud  
- Fast feature updates  
- Scales easily for large environments  

### 🔹 Why SIEMs Are Important
All SIEM tools:
- Collect data from many sources  
- Filter and analyze events  
- Help teams **detect and respond quickly**  

---

## 🧠 How Analysts Use SIEM Tools

As a security analyst, you may use SIEM tools to:
- Analyze alerts  
- Identify attack patterns  
- Investigate incidents  
- Proactively search for threats  

Each organization may configure SIEM tools differently, but the **purpose remains the same**:  
➡️ **Reduce risk and prevent damage**

---

# 📘 4. Playbooks

### 🔹 What Is a Playbook?
A **playbook** is a documented guide that explains **how to respond** to a specific situation.

Think of it as a **step-by-step manual**.

---

## 🔹 Why Playbooks Matter

Playbooks help analysts:
- Respond consistently  
- Reduce mistakes  
- Act quickly under pressure  
- Know what to do **before, during, and after** an incident  

---

## 🔹 Examples of Playbook Use
- Security incident response  
- Compliance reviews  
- Access management  
- Account compromise handling  

Playbooks vary by organization, but they always provide **clear guidance**.

---

# 🌐 5. Network Protocol Analyzers (Packet Sniffers)

### 🔹 What Is a Network Protocol Analyzer?
Also called a **packet sniffer**, this tool captures and analyzes **network traffic**.

---

## 🔹 What Packet Sniffers Do
- Inspect data moving across the network  
- Detect unauthorized data transfers  
- Identify malicious traffic  
- Help troubleshoot network issues  

---

## 🔹 Common Network Protocol Analyzers
- **tcpdump**  
- **Wireshark**

These tools allow analysts to see **what is actually happening** on the network.

---
## 🔍 Cybersecurity Tool Comparison Table

| Tool Type | Tool Name | Primary Purpose | Key Features | Best Used For | Beginner Tip |
|----------|----------|----------------|--------------|---------------|--------------|
| **SIEM** | **Splunk Enterprise** | Collect, search, and analyze log data | Self-hosted, powerful search, dashboards, alerts | Log analysis, incident investigation | Focus on learning searches and alerts first |
| **SIEM** | **Google Chronicle** | Cloud-native log storage and analysis | Scalable, fast search, cloud-based | Large-scale security monitoring | Understand how cloud SIEM differs from on-prem |
| **Playbook** | **Incident Response Playbooks** | Guide security response actions | Step-by-step procedures | Handling incidents consistently | Follow the steps—don’t improvise |
| **Network Analyzer** | **Wireshark** | Capture and inspect network packets | GUI-based, detailed packet view | Traffic analysis, troubleshooting | Learn basic filters first |
| **Network Analyzer** | **tcpdump** | Capture network traffic via command line | Lightweight, fast, CLI-based | Quick packet capture | Practice simple capture commands |
| **Log Source** | **System & App Logs** | Record system events | Login logs, access logs | Detect suspicious activity | Logs are the foundation of all tools |
| **Automation** | **SQL** | Query and analyze security data | Structured queries, fast filtering | Trend analysis, investigations | Start with SELECT statements |
| **Automation** | **Python** | Automate security tasks | Scripting, APIs, data processing | Automation, analysis | Learn basic scripts, not advanced code |



