# 🚨 Detection & Analysis Phase  
**Incident Response Lifecycle**

---

## 1️⃣ Where Detection & Analysis Fit in Incident Response

Incidents are **inevitable**. As a security analyst, one of your most important responsibilities is working in the **Detection and Analysis** phase of the incident response lifecycle.

This phase answers two critical questions:
- **Did something suspicious happen?** (Detection)
- **Is it truly a security incident?** (Analysis)

📌 Remember:
- **All incidents are events**
- **Not all events are incidents**

---

## 2️⃣ Events vs Incidents (Clear Distinction)

### 🔹 Events
Normal, expected activities such as:
- Website visits
- Password reset requests
- User logins

These occur constantly and are logged by systems.

### 🔥 Incidents
Events that:
- Violate security policies
- Threaten confidentiality, integrity, or availability
- Involve unauthorized or malicious activity

Example:
- A malicious actor gains unauthorized access to an account

---

## 3️⃣ Detection: Discovering Security Events

**Detection** is the prompt discovery of potential security events.

Detection is commonly performed using:
- Intrusion Detection Systems (IDS)
- Security Information and Event Management (SIEM) tools

These tools:
- Collect event data from multiple sources
- Analyze activity
- Generate alerts when unusual behavior is detected

📌 Detection does not confirm an incident — it signals the **need for investigation**.

---

## 4️⃣ Analysis: Validating Alerts

Once an alert is triggered, analysts move into **analysis**.

Analysis involves:
- Investigating alerts
- Validating whether an incident actually occurred
- Reviewing indicators of compromise (IoCs)
- Applying critical thinking and context

This step separates:
- **True positives** (real incidents)
- **False positives** (benign activity)

---

## 5️⃣ Challenges in Detection & Analysis

### ⚠️ Detection Is Never Perfect
- It’s impossible to detect everything
- Tools only detect what they are configured to monitor
- Limited resources may prevent full coverage

Some incidents are **unavoidable**, which is why response planning is critical.

---

### 🔔 Alert Fatigue Is Real
Analysts may receive:
- Hundreds or thousands of alerts per shift

Common causes:
- Misconfigured detection rules
- Overly broad alert logic
- Poorly tuned environments

📌 Not all high alert volumes are noise — some indicate **active exploitation** of new vulnerabilities.

---

## 6️⃣ Why Analysts Must Be Skilled at Alert Analysis

A skilled analyst can:
- Quickly triage alerts
- Identify false positives
- Spot real threats hiding in noise
- Prioritize response actions

This skill directly impacts:
- Response time
- Damage containment
- Organizational risk

---

## 7️⃣ Beyond Tools: Additional Detection Methods

Detection tools are powerful, but **not sufficient alone**. Organizations use additional methods to improve coverage and accuracy.

---

## 8️⃣ Threat Hunting (Human-Driven Detection)

**Threat hunting** is the proactive search for threats that:
- Were not detected by automated tools
- Are actively evading detection

Key characteristics:
- Human-driven
- Hypothesis-based
- Uses technology + analyst intuition

### Why threat hunting matters
Some threats, like **fileless malware**, are difficult to detect because they:
- Live in memory
- Avoid files and signatures
- Bypass traditional detection methods

Threat hunting helps identify these stealthy threats **before damage occurs**.

---

### 👤 Threat Hunters
Threat hunters:
- Research emerging threats
- Study attacker tactics, techniques, and procedures (TTPs)
- Assess organizational exposure
- Use IoCs, IoAs, threat intelligence, and machine learning

---

## 9️⃣ Threat Intelligence (Adding Context)

**Threat intelligence** is evidence-based information about:
- Existing threats
- Emerging attacker behavior
- Known malicious infrastructure

### Common sources
- Industry reports (attacker TTPs)
- Government advisories
- Threat data feeds (IPs, domains, hashes)

---

### 🧠 Threat Intelligence Platforms (TIPs)

Managing large volumes of intelligence is difficult.

A **TIP**:
- Collects intelligence from multiple sources
- Centralizes and correlates data
- Helps prioritize relevant threats

📌 Threat intelligence should **add context**, not blindly drive detections.

---

## 🔮 Cyber Deception

**Cyber deception** uses deliberate decoys to:
- Trick attackers
- Increase detection
- Reveal attacker behavior

### Honeypots
Honeypots are intentionally vulnerable systems or resources designed to attract attackers.

Example:
- A fake file named *Client Credit Card Information - 2022*

When accessed:
- Security teams are alerted
- Attacker behavior is observed safely

---

## 🔑 Key Takeaways

- Detection identifies potential security events
- Analysis confirms whether an incident occurred
- Not all events are incidents
- Detection tools have limitations
- Alert fatigue is common but manageable
- Threat hunting uncovers hidden threats
- Threat intelligence provides critical context
- Cyber deception increases visibility into attacker behavior
- Strong detection uses **multiple complementary methods**

---

**✍️ Notes By Abhishek (Ez Abyss)**
