# 🕵️ Overview of Interception Tactics

Interception attacks are network attacks that **capture, monitor, or alter data packets while they are traveling across a network**.  
Two of the most common techniques used in interception attacks are **packet sniffing** and **IP spoofing**.

Understanding how these attacks work—and how to defend against them—is essential for security analysts.

---

## What Are Interception Attacks?

**Interception attacks** occur when malicious actors:
- intercept data packets in transit
- inspect or collect sensitive information
- modify packets before they reach their destination

Because these attacks target **data in motion**, they can compromise:
- confidentiality
- integrity
- availability

---

## Packet Sniffing (Detailed Review)

### What Is Packet Sniffing?

**Packet sniffing** is the practice of capturing and inspecting data packets as they travel across a network.

- Security analysts use packet sniffing for:
  - incident investigation
  - troubleshooting network issues
- Malicious actors use packet sniffing to:
  - steal sensitive data
  - gather information for further attacks

---

### Role of the Network Interface Card (NIC)

A **Network Interface Card (NIC)**:
- connects a device to a network
- reads incoming packets
- accepts packets addressed to its MAC address

#### Promiscuous Mode
A NIC can be placed into **promiscuous mode**, which allows it to:
- accept **all packets on the network**
- even those not addressed to its device

**Security risk:**  
Malicious actors can use tools like **Wireshark** to capture traffic on private networks, collect personal information, and extract IP and MAC addresses.

---

## IP Spoofing (Detailed Review)

After sniffing packets, attackers can perform **IP spoofing**.

**IP spoofing** occurs when a malicious actor:
- impersonates the IP (and sometimes MAC) address of an authorized device
- sends packets that appear legitimate
- bypasses firewall rules and access controls

Properly configured firewalls can:
- refuse unauthorized packets
- block suspicious or spoofed IP traffic

---

## Common Interception Attacks

### 1️⃣ On-Path Attack (Man-in-the-Middle)

An **on-path attack** occurs when an attacker:
- secretly intercepts communication between two trusted devices
- captures or alters data in transit

**What attackers gain:**
- usernames
- passwords
- session data

#### DNS Manipulation
If DNS lookups are intercepted:
- attackers can spoof DNS responses
- redirect users to malicious websites

**Primary defense:**
- encrypt data in transit using **TLS (SSL/TLS)**

---

### 2️⃣ Smurf Attack

A **smurf attack** combines:
- **IP spoofing**
- **Denial of Service (DoS)**

**How it works:**
1. Attacker spoofs a victim’s IP address
2. Sends packets to a broadcast address
3. All devices respond to the victim
4. Network becomes overwhelmed

Often uses **ICMP ping requests** to flood the network.

**Impact:**
- network slowdown
- server crashes
- complete service outage

**Primary defense:**
- Next Generation Firewalls (NGFW)
- anomaly and traffic monitoring

---

### 3️⃣ Denial of Service (DoS) Attack

A **Denial of Service (DoS) attack** prevents a system from:
- responding to legitimate users
- performing normal operations

**Key difference from IP spoofing:**
- packets may appear fully legitimate
- IP addresses may not be spoofed

Attackers flood systems with traffic until:
- resources are exhausted
- services become unavailable

---

## Defense-in-Depth Strategy (Pro Tip)

There is **no single defense** that stops all interception attacks.

**Best practice: defense-in-depth**
- encrypt data in transit
- deploy advanced firewalls
- monitor traffic anomalies
- apply layered security controls

Using multiple defenses increases resilience against:
- packet sniffing
- IP spoofing
- DoS and DDoS attacks

---

## Key Takeaways

- Interception attacks target **data in transit**
- Packet sniffing gathers information for further attacks
- IP spoofing impersonates trusted devices
- On-path, smurf, and DoS attacks disrupt operations
- Encryption and layered defenses are critical
- Security analysts must proactively mitigate these threats

---

## One-Line Summary

> **Interception attacks exploit data in motion using packet sniffing and IP spoofing, making encryption and layered security essential for network defense.**

---
**✍️ Notes By Abhishek (Ez Abyss)**
