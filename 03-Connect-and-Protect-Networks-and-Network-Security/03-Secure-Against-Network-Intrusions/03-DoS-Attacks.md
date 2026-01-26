# 🚨 Denial of Service (DoS) & Distributed DoS (DDoS) Attacks
**Focus:** Network-level DoS attacks, TCP & ICMP abuse  

---

## 1️⃣ What Is a Denial of Service (DoS) Attack?

A **Denial of Service (DoS) attack** targets a **network, server, or device** by flooding it with traffic or requests.

### 🎯 Goal of a DoS Attack
- Overload a system
- Disrupt normal business operations
- Prevent legitimate users from accessing services

If a system **cannot respond**, the attacker has succeeded.

---

## 2️⃣ Why DoS Attacks Are Dangerous

A successful DoS attack can:
- ❌ Take systems offline
- 💸 Cost organizations money and time
- 🔓 Leave systems vulnerable to other attacks
- 📉 Damage reputation and customer trust

> Even temporary outages can have **long-term consequences**.

---

## 3️⃣ Distributed Denial of Service (DDoS)

A **DDoS attack** is an advanced form of DoS that uses:
- Multiple devices
- Multiple locations
- Often botnets (compromised systems)

### Why DDoS Is More Powerful
- Traffic comes from many sources
- Harder to block
- Much higher traffic volume

📌 **Key idea:**  
If **any part** of the network is overwhelmed, the attack is successful.

---

## 4️⃣ Protocol-Level DoS Attacks

Some DoS attacks **don’t rely on huge traffic volume**, but instead exploit how protocols work.

> Even a *small number* of carefully crafted packets can crash a system.

---

## 5️⃣ SYN Flood Attack (TCP-Based)

A **SYN flood** exploits the **TCP three-way handshake**.

### 🔁 Normal TCP Handshake
1. Client → **SYN**
2. Server → **SYN/ACK**
3. Client → **ACK**
➡️ Connection established

---

### 💣 How SYN Flood Works
- Attacker sends SYN packets
- Never sends the final ACK
- Server keeps ports open waiting
- Available ports are exhausted
- Legitimate connections fail

📌 **Result:** Server becomes unavailable.

---

## 6️⃣ ICMP-Based DoS Attacks

### 🔔 What Is ICMP?
**ICMP (Internet Control Message Protocol)** is used for:
- Error reporting
- Status updates
- Network diagnostics (e.g., `ping`)

Think of ICMP as **“Are you okay?”** messages between devices.

---

### 🌊 ICMP Flood Attack
- Attacker sends repeated ICMP requests
- Server is forced to respond to each one
- Bandwidth is consumed
- System eventually crashes

📌 **Problem:** Both incoming *and* outgoing traffic are overwhelmed.

---

## 7️⃣ Ping of Death Attack

The **Ping of Death** is a classic ICMP-based DoS attack.

### How It Works
- Attacker sends an **oversized ICMP packet**
- Packet exceeds **64 KB**, the maximum valid size
- Vulnerable systems fail to handle it
- System crashes

### 🐜 Analogy
- Ants can carry small loads individually
- A giant rock crushes the anthill instantly

📌 **Key point:**  
One malformed packet can be more destructive than many small ones.

---

## 8️⃣ DoS vs DDoS — Quick Comparison

| Feature | DoS | DDoS |
|------|----|----|
| Number of attackers | Single | Multiple |
| Traffic source | One device | Many devices |
| Difficulty to block | Easier | Much harder |
| Common tools | SYN, ICMP | Botnets |

---

## 🛡️ Analyst Perspective 

Security analysts must ask:
- Is traffic volume abnormal?
- Are protocols being abused?
- Are ports stuck in half-open states?
- Is ICMP traffic excessive or malformed?

Early detection = faster mitigation.

---

## 🧠 Key Takeaways

- DoS attacks target **availability**
- DDoS attacks amplify impact using multiple sources
- SYN floods exploit TCP handshake behavior
- ICMP floods and Ping of Death abuse ICMP
- Attacks don’t need massive traffic to succeed

---

## 🎯 Summary

> “A DoS attack disrupts service availability by overwhelming a system with traffic or malformed requests.  
> DDoS attacks increase impact by distributing traffic across multiple sources.  
> Common examples include SYN floods, ICMP floods, and Ping of Death attacks.”

---

## 🧠 Memory Anchors

- **DoS = availability attack**
- **DDoS = many attackers**
- **SYN flood = half-open TCP**
- **ICMP flood = bandwidth exhaustion**
- **Ping of Death = oversized packet**

---

✍️ *Notes By Abhishek (Ez Abyss)*
