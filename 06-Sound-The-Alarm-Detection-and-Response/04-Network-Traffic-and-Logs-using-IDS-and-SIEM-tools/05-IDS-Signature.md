# 🛡️ IDS Signatures Explained  
### Reading, Writing, and Understanding Detection Rules

---

## 🎯 Why IDS Signatures Matter

As a **Security Analyst**, you don’t just respond to alerts —  
you help **define what gets detected**.

An **IDS signature** is a **detection rule** that tells an Intrusion Detection System:
- What traffic to inspect
- What patterns are suspicious
- What action to take when a match occurs

👉 Think of signatures as **security tripwires** placed across the network.

---

## 🌍 Real-World Analogy

Imagine airport security:

- **Action** → What happens when something suspicious is found  
- **Header** → Who is traveling, from where, to where  
- **Options** → Why it’s suspicious (message, ID, revision)

IDS signatures work the same way.

---

## 🧱 Core Components of an IDS Signature

Most Network Intrusion Detection Systems (NIDS) signatures contain **three parts**:

1. **Action**
2. **Header**
3. **Rule Options**

---

## 1️⃣ Action — What Should the IDS Do?

The **action** is the first part of the signature.

Common actions:
- `alert` → Generate an alert
- `pass` → Ignore the traffic
- `reject` → Block and log the traffic

📌 Example:
- If suspicious traffic hits a sensitive port → `alert`

---

## 2️⃣ Header — What Traffic Are We Inspecting?

The **header defines network traffic characteristics**:

- Protocol (TCP, UDP, ICMP)
- Source IP and port
- Destination IP and port
- Traffic direction

### Example Header Breakdown

<img width="1504" height="715" alt="image" src="https://github.com/user-attachments/assets/648b82b6-3a12-4713-98a6-1c4bd89a0c01" />

- Protocol: TCP
- Source IP: `10.120.170.17`
- Source Port: `any`
- Direction: `->`
- Destination IP: `133.113.202.181`
- Destination Port: `80`

📌 This means:
Traffic coming **from 10.120.170.17 on any port going to 133.113.202.181 on port 80**

---

## 3️⃣ Rule Options — Why Is This Traffic Suspicious?

Rule options:
- Are enclosed in parentheses `( )`
- Are separated by semicolons `;`
- Provide **context and control**

---

## 🧪 Example IDS Signature (Explained)
```
tcp 10.120.170.17 any -> 133.113.202.181 80
(msg:"This is a message"; sid:12345; rev:1;)
```
<img width="1392" height="572" alt="image" src="https://github.com/user-attachments/assets/9f1fb112-4648-4a8e-ac2d-297f4976190c" />


---

## 🔍 Rule Options Explained

| Option | Meaning | Why It Matters |
|------|--------|----------------|
| `msg` | Alert message | What the analyst sees in the alert |
| `sid` | Signature ID | Unique identifier for the rule |
| `rev` | Revision number | Tracks rule updates over time |

---

## 🔄 Why `sid` and `rev` Are Critical

### `sid` (Signature ID)
- Must be **unique**
- Used by SIEMs and SOAR tools
- Helps correlate alerts across systems

### `rev` (Revision)
- Increases every time the rule is modified
- Helps analysts understand **rule evolution**
- Critical for change tracking and audits

📌 Example:
- `rev:1` → Initial rule
- `rev:2` → Updated for false positives
- `rev:3` → Tuned for new attacker behavior

---

## 🧠 How Analysts Use Signatures in Practice

Security analysts:
- Write custom signatures for new threats
- Tune rules to reduce false positives
- Test signatures in staging environments
- Track rule changes using `sid` and `rev`

📌 Example use case:
Detecting unusual outbound HTTP traffic from internal hosts.

---

## ⚠️ Common Beginner Mistakes

- Forgetting to increment `rev`
- Reusing an existing `sid`
- Writing overly broad rules
- Alerting on normal business traffic

Top analysts **tune**, not just detect.

---

## 🏁 Key Takeaways

- IDS signatures define **what gets detected**
- Every rule has **Action + Header + Options**
- `msg`, `sid`, and `rev` are essential for SOC workflows
- Well-written signatures reduce alert fatigue
- Mastering signatures = thinking like a defender **and** attacker

---

**✍️ Notes By Abhishek (Ez Abyss)**
