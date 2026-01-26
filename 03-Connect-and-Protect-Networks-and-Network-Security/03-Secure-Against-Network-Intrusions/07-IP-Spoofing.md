# 🎭 IP Spoofing (Network Impersonation Attack)

## What is IP Spoofing?

**IP spoofing** is a network attack in which an attacker **changes the source IP address of a data packet** to impersonate a trusted or authorized system.

By spoofing an IP address, the attacker:
- pretends to be a legitimate device
- bypasses firewall rules
- gains unauthorized access to a network
- communicates with systems that would normally block them

**Simple idea:**  
The attacker is pretending to be someone they are not.

---

## Why IP Spoofing Is Dangerous

IP spoofing allows attackers to:
- bypass access controls
- trick firewalls into allowing traffic
- launch larger attacks such as DDoS
- impersonate trusted users or systems

Firewalls often trust internal IP addresses.  
IP spoofing abuses that trust.

---

## Common Types of IP Spoofing Attacks

### 1️⃣ On-Path Attack (Man-in-the-Middle)

An **on-path attack** occurs when a malicious actor places themselves **between two communicating devices**, such as:
- a web browser
- a web server

**How it works:**
1. Attacker intercepts network traffic
2. Sniffs packets to learn IP and MAC addresses
3. Pretends to be one or both devices
4. Intercepts or alters data in transit

**Result:**
- stolen data
- modified messages
- loss of confidentiality and integrity

---

### 2️⃣ Replay Attack

A **replay attack** happens when an attacker:
- intercepts a legitimate data packet
- stores it
- resends it later to impersonate an authorized user

**Effects:**
- repeated authentication attempts
- unauthorized actions
- connection disruptions

**Example:**
Replaying a valid login request to gain access later.

---

### 3️⃣ Smurf Attack

A **smurf attack** is a combination of:
- **IP spoofing**
- **Distributed Denial of Service (DDoS)**

**How it works:**
1. Attacker spoofs the victim’s IP address
2. Sends massive traffic toward the victim
3. Target system becomes overwhelmed

**Result:**
- server crash
- network outage
- denial of service

---

## How to Protect Against IP Spoofing

### 🔐 Use Encryption
- Encrypt network traffic using secure protocols
- Prevents attackers from reading intercepted data
- Examples:
  - HTTPS (SSL/TLS)
  - VPN encryption

---

### 🔥 Configure Firewalls Properly

Firewalls can detect IP spoofing by:
- rejecting packets that claim to originate from the internal network but arrive from the internet

**Best firewall rule:**
- Deny incoming packets with source IP addresses matching the local network

**Why this works:**
Devices with internal IPs should already be inside the network.

---

### 🛡️ Network Monitoring
- Monitor unusual traffic patterns
- Detect duplicate packets or replay behavior
- Identify abnormal source IP activity

---

## Key Takeaways

- IP spoofing disguises an attacker as a trusted system
- It is used in on-path, replay, and smurf attacks
- Attackers exploit trust in IP addresses
- Encryption and proper firewall rules are essential defenses
- Blocking spoofed internal IPs at the firewall is critical

---

## Summary

> **IP spoofing is an impersonation attack where attackers fake IP addresses to bypass security controls and gain unauthorized access.**

---

**✍️ Notes By Abhishek (Ez Abyss)**
