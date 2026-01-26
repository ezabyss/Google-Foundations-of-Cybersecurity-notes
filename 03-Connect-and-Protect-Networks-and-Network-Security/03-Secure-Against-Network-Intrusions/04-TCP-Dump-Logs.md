# 📡 Reading tcpdump Logs
**Focus:** Network protocol analyzers & packet inspection  

---

## 1️⃣ What Is a Network Protocol Analyzer?

A **network protocol analyzer** (also called a **packet sniffer** or **packet analyzer**) is a tool used to:

- Capture network traffic
- Analyze data packets in transit
- Investigate suspicious or malicious activity

Security analysts use these tools to **monitor networks**, **detect attacks**, and **troubleshoot performance issues**.

---

## 2️⃣ Common Network Protocol Analyzers

Some widely used network protocol analyzers include:

- **SolarWinds NetFlow Traffic Analyzer**
- **ManageEngine OpManager**
- **Azure Network Watcher**
- **Wireshark**
- **tcpdump**

📌 This section focuses specifically on **tcpdump**, but the concepts apply to other analyzers as well.

---

## 3️⃣ What Is tcpdump?

**tcpdump** is a **command-line network protocol analyzer** that captures and displays network packets.

### Key Characteristics
- Lightweight (low CPU & memory usage)
- Text-based (runs entirely in the terminal)
- Uses the open-source **libpcap** library
- Preinstalled on many Linux distributions
- Available on Unix-based systems, including macOS

---

## 4️⃣ What tcpdump Does

tcpdump:
- Captures live network traffic
- Displays packet details in real time
- Converts packet data into human-readable output

### Information tcpdump Displays
- Source IP address
- Destination IP address
- Source port
- Destination port
- Timestamp of each packet

---

## 5️⃣ Interpreting tcpdump Output

When tcpdump runs, it prints packet information directly to the terminal (and optionally to a log file).

### Key Fields in tcpdump Output

| Field | Description |
|-----|------------|
| Timestamp | Time the packet was captured (HH:MM:SS.microseconds) |
| Source IP | IP address where the packet originated |
| Source Port | Port number used by the sender |
| Destination IP | IP address receiving the packet |
| Destination Port | Port number receiving the packet |

📌 **Note:**  
By default, tcpdump:
- Resolves IP addresses to hostnames
- Replaces port numbers with common service names (e.g., `http`, `https`)

---

## 6️⃣ Common Uses of tcpdump

Security analysts use tcpdump to:

- Monitor network communications
- Troubleshoot network performance issues
- Establish a **baseline** for normal network traffic
- Detect and identify malicious traffic
- Investigate suspected DoS or intrusion attempts
- Locate unauthorized applications or access points
- Create data for alerts and incident response

---

## 7️⃣ tcpdump as an Investigative Tool

tcpdump is especially useful during:
- **Incident response**
- **Intrusion detection**
- **Network forensics**
- **DoS/DDoS analysis**

In later exercises, tcpdump logs can help identify:
- Abnormal traffic volumes
- Repeated packet patterns
- Suspicious source IP addresses

---

## 8️⃣ Security Risks of Packet Analyzers

⚠️ While tcpdump is a powerful defensive tool, attackers can misuse packet analyzers.

Attackers may use packet sniffers to:
- Capture usernames and passwords
- Steal sensitive data
- Learn network structure and services

📌 **Security analysts must understand both defensive and offensive uses** of these tools.

---

## 🧠 Key Takeaways

- Network protocol analyzers capture and analyze network traffic
- tcpdump is a lightweight, command-line packet analyzer
- tcpdump outputs timestamps, IPs, and port information
- Analysts use tcpdump for monitoring, troubleshooting, and security investigations
- Attackers can misuse packet sniffers, making awareness critical

---

## 🎯 Analyst Mindset

> “If you understand how packets move through a network,  
> you can identify when something doesn’t belong.”

---

✍️ *Notes By Abhishek (Ez Abyss)*
