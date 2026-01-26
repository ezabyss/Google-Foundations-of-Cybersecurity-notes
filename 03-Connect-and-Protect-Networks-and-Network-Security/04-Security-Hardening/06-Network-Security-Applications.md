# 🛡️ Network Security Applications

---

## 🎯 Big Picture: Network Hardening & Monitoring

Network hardening and monitoring involve **adding security layers** until the organization reaches an acceptable level of risk.

> This layered approach is called **defense in depth**.

Each device, tool, or strategy adds **another protective layer** to the network.

---

![684781d4-cc92-428e-8c72-a0eb76f23366-md](https://github.com/user-attachments/assets/aa069da2-6d37-49fa-8bd7-5671d1b437cd)
*Figure: Defense in Depth using Firewall, IDS, and IPS*


## 🧠 Defense in Depth (Core Concept)

### 📌 Definition

**Defense in depth** is a security strategy that uses **multiple layers of security controls** to protect a network.

🔐 If one layer fails, the next layer still protects the system.

---

## 🧩 Network Security Devices Covered

This section focuses on **four key network security tools**:

1. Firewalls
2. Intrusion Detection Systems (IDS)
3. Intrusion Prevention Systems (IPS)
4. Security Information and Event Management (SIEM)

Security teams may use **any or all** of these depending on:

* Cost
* Risk tolerance
* Security requirements

---

## 🔥 Firewall

### 📌 Purpose

A **firewall** allows or blocks network traffic based on predefined rules.

### 🔍 How It Works

* Inspects packet **headers**
* Filters traffic based on:

  * Port numbers
  * IP addresses
  * Protocols

🔐 **Next‑generation firewalls (NGFWs)** can also inspect **packet payloads**.

---

### 📍 Placement

* At the network perimeter
* Each system should also have its **own local firewall**

---

### ✅ Advantages

* Basic but essential protection
* Blocks unauthorized traffic

### ❌ Limitations

* Traditional firewalls only inspect packet headers
* Limited visibility into advanced attacks

---

## 🚨 Intrusion Detection System (IDS)

### 📌 Definition

An **IDS** monitors network or system activity and **alerts administrators** about possible intrusions.

---

### 🔍 How IDS Works

* Analyzes network traffic
* Detects:

  * Known attack signatures
  * Unusual or abnormal behavior

When suspicious activity is detected, the IDS:
➡️ Sends an **alert** to the administrator

---

### 📍 Placement

* **Behind the firewall**
* Before traffic enters the internal network (LAN)

🔎 This placement reduces **false positives** by filtering noisy traffic first.

---

### ✅ Advantages

* Detects malicious activity
* Provides visibility into attacks

### ❌ Limitations

* Cannot stop traffic
* Only detects known attacks or obvious anomalies

---

## 🛑 Intrusion Prevention System (IPS)

### 📌 Definition

An **IPS** monitors network activity and **actively blocks** suspicious traffic.

> IPS = IDS + automatic response

---

### 🔍 How IPS Works

* Detects attack signatures and anomalies
* Takes action by:

  * Dropping packets
  * Blocking senders
  * Stopping malicious connections

---

### 📍 Placement

* Inline, **behind the firewall** and before the internal network

---

### ✅ Advantages

* Actively stops attacks
* Provides stronger protection than IDS

### ❌ Limitations

* Inline failure can disrupt network connectivity
* False positives may block legitimate traffic

---

## 📦 Full Packet Capture Devices

### 📌 Purpose

* Record and analyze **all network traffic**
* Support investigation of IDS/IPS alerts

These tools help security professionals:

* Reconstruct attacks
* Perform deep forensic analysis

---

## 📊 Security Information and Event Management (SIEM)

### 📌 Definition

A **SIEM** collects, aggregates, and analyzes log data from across the organization.

---

### 🔍 What SIEM Collects Logs From

* Firewalls
* IDS / IPS
* VPNs
* Proxies
* DNS servers

---

### 🧠 Key Features

* Centralized dashboard
* Real‑time monitoring
* Threat prioritization

This centralized view is called a **single pane of glass**.

---

### 🏢 SOC & SIEM

Security analysts often work in a **Security Operations Center (SOC)** where they:

* Monitor SIEM dashboards
* Investigate alerts
* Decide when incidents require escalation

---

### ❗ Important Note

A SIEM:

* ❌ Does not stop attacks
* ✅ Supports analysts with visibility and analysis

Human expertise is still essential.

---

## 🧠 Tool Comparison (High‑Yield)

| Tool     | What It Does               | Key Limitation                       |
| -------- | -------------------------- | ------------------------------------ |
| Firewall | Allows or blocks traffic   | Limited inspection (headers only)    |
| IDS      | Detects and alerts         | Cannot stop attacks                  |
| IPS      | Detects and blocks         | Inline failure risk, false positives |
| SIEM     | Aggregates & analyzes logs | Does not take direct action          |

---

## 💰 Cost & Risk Considerations

* Each tool costs money to:

  * Purchase
  * Deploy
  * Maintain
* Some tools require **additional staff** (e.g., SIEM monitoring)

Decision‑makers must balance:

> **Security level vs Cost vs Risk**

---

## 📝 Key Line

> *Network security applications support defense in depth by layering firewalls, IDS, IPS, and SIEM tools to monitor, detect, analyze, and respond to security threats while balancing cost and organizational risk.*

---

**✍️ Notes By Abhishek (Ez Abyss)**
