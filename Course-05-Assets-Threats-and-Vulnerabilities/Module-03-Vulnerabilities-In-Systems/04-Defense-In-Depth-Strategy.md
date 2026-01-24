# 🏰 Defense in Depth Security Model

---

## 🌍 Core Concept: Layered Defense

A **layered defense** is difficult to penetrate.

If one security barrier fails, **another layer takes its place** to stop or slow the attack. This approach reduces overall risk and limits damage.

This concept is known as **Defense in Depth** — a security model based on using **multiple, overlapping security controls**.

---

## 🏰 The Castle Analogy

Defense in depth is often called the **castle approach** because it mirrors how castles were protected in the Middle Ages.

Castles were difficult to attack because they used **multiple defensive layers**, each designed to counter different attack methods.

---

## 🧱 Castle Layers and Vulnerabilities

### 1️⃣ The Moat

* Water-filled barrier surrounding the castle
* Prevented large groups of attackers from reaching the walls

**Vulnerability:** Some attackers could still cross it

---

### 2️⃣ Stone Walls

* Tall, thick walls protected the castle

**Vulnerability:** Walls could be climbed

---

### 3️⃣ Watch Towers

* Towers staffed with defenders
* Archers stopped attackers trying to climb the walls

---

> 🧠 Each layer assumed another might fail, so additional defenses were always in place.

---

## 🔐 Defense in Depth in Cybersecurity

Defense in depth applies to **any asset**, but it is most commonly used in cybersecurity to protect **information**.

It uses a **five-layer design**, where data passes through multiple security layers as it moves across a network.

---

## 🛡️ The Five Layers of Defense in Depth

---

## 1️⃣ Perimeter Layer (Authentication)

**Purpose:** Filter external access

This layer focuses on **who is allowed in**.

### Common Controls

* Usernames and passwords
* Authentication systems

Only trusted users are allowed to move to the next layer.

### 🕵️ SOC Scenario

* Multiple failed login attempts detected
* SOC flags possible brute-force attempt
* Account temporarily locked

➡️ **SOC Role:** Stop unauthorized access at the perimeter

---

## 2️⃣ Network Layer (Authorization)

**Purpose:** Control what users are allowed to access

This layer manages traffic within the network.

### Common Controls

* Network firewalls
* Network segmentation

### 🕵️ SOC Scenario

* Firewall logs show blocked malicious IPs
* SOC confirms firewall rules working as intended

➡️ **SOC Role:** Monitor and enforce network-level controls

---

## 3️⃣ Endpoint Layer

**Purpose:** Protect devices connected to the network

Endpoints include:

* Laptops
* Desktops
* Servers

### Common Controls

* Antivirus software
* Endpoint detection and response (EDR)

### 🕵️ SOC Scenario

* Malware detected on employee laptop
* SOC isolates device from network
* Threat removed

➡️ **SOC Role:** Prevent spread from compromised endpoints

---

## 4️⃣ Application Layer

**Purpose:** Secure how users interact with applications

Security is built **into the application itself**.

### Common Controls

* Multi-Factor Authentication (MFA)
* Input validation

### 🕵️ SOC Scenario

* Attacker obtains password
* MFA prevents account takeover
* SOC reviews authentication logs

➡️ **SOC Role:** Detect and block application-level attacks

---

## 5️⃣ Data Layer

**Purpose:** Protect the most critical asset — data

This layer focuses on information such as:

* Personally Identifiable Information (PII)
* Sensitive business data

### Key Control: Asset Classification

* Data is labeled based on sensitivity
* Stronger protections applied to more sensitive data

### 🕵️ SOC Scenario

* Attempted access to restricted data detected
* Access denied based on classification
* SOC investigates user activity

➡️ **SOC Role:** Protect critical data from unauthorized access

---

## 🔄 How the Layers Work Together

* Data moves through **all five layers** during normal use
* Each layer reduces risk if another fails
* Multiple controls ensure no single point of failure

> 🔁 Defense in depth assumes **breach is possible**, so damage must be limited.

---

## 🧠 Why Organizations Use Defense in Depth

* Reduces overall security risk
* Limits attack impact
* Improves detection and response
* Strengthens asset protection

---

## ✅ Key Takeaways

* Defense in depth uses **multiple security layers**
* Inspired by medieval castle defenses
* No single control is enough
* Five cybersecurity layers protect information
* SOC teams monitor and respond at every layer

---

✍️ **Notes by Abhishek (Ez Abyss)**
