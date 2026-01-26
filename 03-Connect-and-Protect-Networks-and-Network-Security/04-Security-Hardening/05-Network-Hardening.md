# 🌐 Network Hardening

---

## 🎯 How Network Hardening Fits In

Earlier, you learned about **OS hardening**, which focuses on **individual devices**.

> **Network hardening** focuses on securing the **connections, traffic, and communication** between those devices.

Both are essential — but network hardening protects the **entire infrastructure**.

---

## 🔐 What Is Network Hardening?

### 📌 Definition

**Network hardening** is the process of strengthening network security by:

* Controlling network traffic
* Limiting access
* Securing communication channels
* Reducing network-level attack surfaces

---

## 🧩 Areas of Focus in Network Hardening

Network hardening focuses on:

* Port filtering
* Network access privileges
* Network encryption
* Monitoring and logging

---

## 🔄 Network Hardening Tasks (Performed Regularly)

### 1️⃣ Firewall Rules Maintenance

* Review and update firewall rules regularly
* Remove outdated or unnecessary rules

> Only required traffic should be allowed through the firewall.

---

### 2️⃣ Network Log Analysis

#### 📌 What Is a Log?

A **log** is a record of events occurring within a system or network.

#### 📌 Network Log Analysis

The process of examining network logs to:

* Identify suspicious activity
* Detect intrusions
* Investigate incidents

---

### 🧠 SIEM (Security Information and Event Management)

#### 📌 Definition

A **SIEM** is a tool that:

* Collects log data from across the network
* Analyzes security events
* Displays data on a **single dashboard** ("single pane of glass")

#### 🔍 Why SIEM Matters

* Centralized monitoring
* Faster detection and response
* Prioritization of threats

SIEM reports:

* Identify vulnerabilities
* Rank them from **high to low priority**
* Set shorter deadlines for high-risk issues

---

### 3️⃣ Patch Updates

* Apply network device and server patches
* Fix known vulnerabilities in network software

> Unpatched network components are common attack targets.

---

### 4️⃣ Server Backups

* Protect critical network data
* Enable fast recovery after incidents

---

## 🧱 Network Hardening Tasks (Performed Once, Updated as Needed)

### 1️⃣ Port Filtering

#### 📌 Definition

**Port filtering** is a firewall function that:

* Allows or blocks specific port numbers
* Limits unwanted network communication

#### 🔑 Core Principle

> Only ports required for normal operations should be allowed.

All unused ports should be blocked to prevent exploitation.

---

### 2️⃣ Network Access Privileges

* Users should only access network resources required for their role
* Prevents unauthorized movement across the network

🧠 This follows the **principle of least privilege**.

---

### 3️⃣ Secure Wireless Protocols

* Use the most up-to-date wireless security protocols
* Disable outdated or insecure protocols

> Older wireless protocols are easier to exploit.

---

### 4️⃣ Network Segmentation

#### 📌 Definition

**Network segmentation** divides a network into smaller, isolated subnets.

#### 📋 Example

* Marketing subnet
* Finance subnet

#### 🔐 Benefits

* Prevents issues from spreading across the entire network
* Limits access based on job roles
* Improves monitoring and control

---

### 🏢 Security Zones

* Highly sensitive or classified data is placed in **restricted zones**
* Restricted zones are isolated from the rest of the network

> Breaches in one zone do not automatically affect others.

---

### 5️⃣ Network Encryption

#### 📌 Definition

**Encryption standards** are rules used to:

* Encrypt outgoing data
* Decrypt incoming data

#### 🔐 Best Practices

* Encrypt all network communications
* Apply **stronger encryption** to restricted zones

> Encryption protects data even if traffic is intercepted.

---

## 🧠 Summary

* Network hardening protects network traffic and communication
* Firewalls, logs, SIEM, and patching are ongoing tasks
* Port filtering reduces exposed entry points
* Segmentation limits damage spread
* Encryption protects data in transit

---

## 📝 Key Line

> *Network hardening strengthens network security by controlling traffic, limiting access, monitoring activity, segmenting networks, and encrypting communications to reduce attack surfaces and prevent the spread of security incidents.*

---

**✍️ Notes By Abhishek (Ez Abyss)**
