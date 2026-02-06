# 🚨 Indicators of Compromise (IoCs) & the Pyramid of Pain  
**Threat Detection**

---

## 1️⃣ What Are Indicators of Compromise (IoCs)?

**Indicators of Compromise (IoCs)** are **observable pieces of evidence** that suggest a potential security incident has occurred.

Think of IoCs as **after-the-fact clues**:
- A malicious file name
- A known bad IP address
- A suspicious domain
- A malware hash

📌 Analogy:  
Finding a broken window and missing valuables in a car → evidence that a theft already happened.

---

## 2️⃣ Indicators of Attack (IoAs) vs IoCs

While IoCs focus on *what already happened*, **Indicators of Attack (IoAs)** focus on **active or ongoing behavior**.

### 🔍 Key Difference

| Concept | Focus | Example |
|------|------|-------|
| **IoC** | Who / What (after the fact) | Malicious file hash, attacker IP |
| **IoA** | Why / How (behavioral, real-time) | Process making suspicious network connections |

### Example
- A process opening a network connection → **IoA**
- The filename of the process and destination IP → **IoCs**

📌 IoAs are behavior-based and harder for attackers to evade.

---

## 3️⃣ Important Note About IoCs

IoCs **do not always confirm** a security incident.

They can result from:
- Human error
- Misconfigurations
- System failures
- Benign testing activity

📌 IoCs must always be **validated through analysis**.

---

## 4️⃣ Why the Pyramid of Pain Exists

Not all IoCs provide the same defensive value.

Security researcher **David J. Bianco** created the **Pyramid of Pain** to show:
- Different types of IoCs
- How difficult it is for attackers to change them
- How much “pain” attackers feel when defenders block them

---

## 5️⃣ Understanding the Pyramid of Pain

<img width="1600" height="845" alt="image" src="https://github.com/user-attachments/assets/a5481f2e-cd46-4cb5-a5d6-8370ebb90783" />


The Pyramid of Pain ranks IoCs from **easiest to hardest** for attackers to change.

📌 The higher up the pyramid you detect and block, the more disruption you cause to attackers.

---

## 6️⃣ Pyramid of Pain Levels (Bottom → Top)

### 🔹 1. Hash Values (Lowest Pain)
- Hashes of known malicious files
- Used to uniquely identify malware samples

Example:
- SHA-256 hash of a ransomware binary

🧠 Attacker pain: **Very low**  
Attackers can easily recompile or modify malware.

---

### 🔹 2. IP Addresses
- IPv4 or IPv6 addresses used by attackers

Example:
- `192.168.1.1`

🧠 Attacker pain: **Low**  
Attackers can switch IPs quickly using VPNs or cloud infrastructure.

---

### 🔹 3. Domain Names
- Domains used for phishing or command-and-control (C2)

Example:
- `malicious-site.example`

🧠 Attacker pain: **Moderate**  
Registering new domains takes more effort than changing IPs.

---

### 🔹 4. Network Artifacts
- Observable network-level evidence

Examples:
- Unusual User-Agent strings
- Specific protocol usage patterns
- C2 communication behaviors

🧠 Attacker pain: **High**  
Changing network behaviors risks breaking their tools.

---

### 🔹 5. Host Artifacts
- Evidence left on a compromised host

Examples:
- Malicious file names
- Registry keys
- Persistence mechanisms

🧠 Attacker pain: **High**  
Requires rewriting malware and changing deployment methods.

---

### 🔹 6. Tactics, Techniques, and Procedures (TTPs) — Highest Pain
- **How attackers operate**
- Their behavior patterns

Definitions:
- **Tactics** → High-level goals (e.g., lateral movement)
- **Techniques** → How tactics are executed (e.g., Pass-the-Hash)
- **Procedures** → Exact implementation details

🧠 Attacker pain: **Extreme**  
Changing TTPs requires retraining, new tools, and new workflows.

📌 TTPs are the **hardest to detect** but **most valuable to defenders**.

---

## 7️⃣ Why the Pyramid of Pain Matters to Analysts

- Low-level IoCs are easy to detect but easy to evade
- High-level IoCs disrupt attacker operations
- Mature detection focuses on **behavior**, not just indicators

📌 The goal is not just detection — it’s **attacker disruption**.

---

## 🔑 Key Takeaways

- IoCs are evidence of potential security incidents
- IoAs focus on real-time attacker behavior
- IoCs alone do not confirm incidents
- The Pyramid of Pain ranks IoCs by attacker disruption
- Hashes and IPs are easy for attackers to change
- TTP-based detection causes maximum attacker pain
- Strong security programs focus higher in the pyramid

---

**✍️ Notes By Abhishek (Ez Abyss)**
