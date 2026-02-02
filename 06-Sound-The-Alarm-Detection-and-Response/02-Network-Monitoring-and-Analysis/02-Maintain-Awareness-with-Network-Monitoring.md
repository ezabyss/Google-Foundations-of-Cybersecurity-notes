# 👀 Maintain Awareness with Network Monitoring  
**Network Security**

---

## 1️⃣ Why Network Monitoring Matters

Network communication is **noisy** by nature. Everyday activities like:
- Sending emails
- Streaming videos
- Browsing websites

…all generate **network traffic** and **network data**.

### Key definitions
- **Network traffic**: The *amount* and *type* of data moving across a network (for example, HTTP, HTTPS).
- **Network data**: The *actual data* transmitted between devices.

Because so much data moves constantly, **maintaining situational awareness** is critical. Network monitoring helps organizations **detect suspicious activity early**—before it becomes a serious incident.

---

## 2️⃣ Know Your Network (Foundational Skill)

Networks connect devices, and devices communicate using **network protocols**.

Network communications provide valuable metadata, such as:
- Source IP address
- Destination IP address
- Protocol used
- Amount of data transferred
- Date and time

Security professionals use this information to understand **what “normal” looks like**.

---

## 3️⃣ Establishing a Baseline

A **baseline** is a reference point used for comparison.

### Simple analogy
- A monthly grocery budget is a baseline
- Sudden spikes indicate unusual spending

### In security
A baseline represents **expected network behavior**, including:
- Normal traffic volume
- Typical communication patterns
- Standard business hours activity

📌 **Why baselines matter**  
You can’t detect abnormal behavior unless you first understand normal behavior.

---

## 4️⃣ Monitoring Your Network for Deviations

Once a baseline is established, monitoring focuses on identifying **deviations**.

Examples of suspicious deviations:
- Unusually large data transfers
- Traffic at unexpected times
- Unknown destinations
- Unapproved protocols or ports

---

## 5️⃣ What Network Components Are Monitored?

### 🔁 Flow Analysis

**Network flow** describes how communications move across a network and includes:
- Packets
- Protocols
- Ports

Ports are often associated with protocols:
- Port `443` → HTTPS (encrypted web traffic)

⚠️ **Attackers don’t always follow conventions**

Example:
- HTTPS traffic over port `8088` instead of `443`

This can indicate **command and control (C2)** activity, where attackers maintain communication with compromised systems.

📌 Security teams must:
- Know which ports are approved
- Watch for protocol–port mismatches

---

### 📦 Packet Payload Information

Network packets include:
- Header information (IP addresses, ports)
- **Payload** (actual transmitted data)

Payloads are often encrypted, but when visibility is possible, monitoring can reveal:
- Sensitive data leaving the network
- Unexpected file transfers

🚨 This may indicate **data exfiltration**.

---

### ⏰ Temporal Patterns (Time-Based Analysis)

Network traffic contains timestamps that help identify **time-based anomalies**.

Example baseline:
- Heavy traffic between `9 a.m. – 5 p.m.` (business hours)

Suspicious behavior:
- Large data transfers at `2 a.m.`
- Repeated activity during weekends or holidays

📌 Off-baseline timing is a strong indicator that investigation is needed.

---

## 6️⃣ SOC vs NOC: Protecting the Network

### 🛡️ Security Operations Center (SOC)
- Focuses on **security**
- Detects threats and attacks
- Investigates indicators of compromise (IoCs)
- Responds to incidents

### 🌐 Network Operations Center (NOC)
- Focuses on **performance and availability**
- Handles outages, latency, and uptime issues

📌 SOC = security threats  
📌 NOC = network health  

Both are critical and often work together.

---

## 7️⃣ Network Monitoring Tools

Monitoring can be **automated or manual**.

---

### 🚨 Intrusion Detection Systems (IDS)

IDS tools:
- Monitor network activity
- Detect deviations from baseline
- Alert on possible intrusions

Common focus:
- Packet payload inspection
- Pattern matching for malware or phishing

📌 IDS alerts analysts—it does not stop traffic.

---

### 🔍 Network Protocol Analyzers (Packet Sniffers)

Packet sniffers capture and analyze network traffic in detail.

Common tools:
- `tcpdump`
- `Wireshark`

They allow analysts to:
- Capture packets
- Examine protocols, ports, and payloads
- Investigate suspicious communications manually

📦 Captured traffic is called a **packet capture (PCAP)**.

---

## 8️⃣ Indicators of Compromise (IoCs)

Through monitoring, analysts look for **IoCs**, such as:
- Unexpected outbound traffic
- Connections to suspicious IPs
- Unusual protocol usage
- Activity outside normal time patterns

IoCs help analysts decide **what to investigate next**.

---

## 🔑 Key Takeaways

- Network monitoring maintains situational awareness
- Baselines define what “normal” looks like
- Deviations from baseline indicate potential threats
- Flow analysis, payload inspection, and time patterns are key
- SOCs focus on security; NOCs focus on performance
- IDS and packet sniffers support monitoring efforts
- You can’t protect what you don’t understand

---

**✍️ Notes By Abhishek (Ez Abyss)**
