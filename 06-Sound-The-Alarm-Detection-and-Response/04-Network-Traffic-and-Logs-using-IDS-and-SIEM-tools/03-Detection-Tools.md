# 🚨 Detection, Telemetry, and Intrusion Detection Systems (IDS)

> **Detection requires data.**  
> In cybersecurity, this data comes from **logs** and **telemetry**, which together provide the evidence needed to detect, investigate, and respond to threats.

---

## 📊 Logs vs Telemetry (Core Concept)

| Concept | Description |
|------|------------|
| Logs | Records of events that occurred on systems or networks |
| Telemetry | The **data itself** collected and transmitted for analysis |

📌 Example:
- Logs → “A connection was allowed at 10:32 AM”
- Telemetry → Packet captures, network flows, endpoint metrics

📌 **Packet captures** are a classic example of **network telemetry**.

---

## 🔍 Why Logs & Telemetry Matter
For security professionals, logs and telemetry:
- Act as **evidence** during investigations
- Help answer **who, what, when, where, and how**
- Enable detection, alerting, and response

---

## 🛑 What Is an Intrusion Detection System (IDS)?
An **Intrusion Detection System (IDS)** is an application that:
- Monitors system or network activity
- Detects suspicious or malicious behavior
- Logs the activity
- Generates alerts

📌 IDS tools **detect and alert** — they do not block traffic.

---

## 💻 Endpoints and Hosts
An **endpoint** (also called a **host**) is any device connected to a network, such as:
- Laptops
- Desktops
- Servers
- Tablets
- Smartphones

📌 Endpoints are common attack targets because they are **entry points into networks**.

---

## 🧠 Types of IDS Technologies

### 1️⃣ Host-Based Intrusion Detection System (HIDS)

A **HIDS**:
- Is installed as an **agent** on a single host
- Monitors activity on that host only

#### What HIDS Can Monitor
- File system changes
- User activity
- System resource usage
- Inbound and outbound traffic
- Application installations

📌 Example:
If an unauthorized application is installed, the HIDS:
- Logs the activity
- Generates an alert

---

### 2️⃣ Network-Based Intrusion Detection System (NIDS)

A **NIDS**:
- Monitors **network traffic**
- Is installed at key points in the network
- Inspects traffic flowing between devices

📌 NIDS tools function similarly to **packet sniffers**.

#### Deployment Strategy
- Multiple NIDS sensors are placed across the network
- This provides **better visibility**

📌 When suspicious traffic is detected:
- The activity is logged
- An alert is generated

---

## 🧩 HIDS vs NIDS (Quick Comparison)

| Feature | HIDS | NIDS |
|------|------|------|
| Scope | Single host | Entire network |
| Visibility | Internal host activity | Network traffic |
| Installation | Agent on endpoint | Sensor on network |
| Best For | Endpoint attacks | Network-based attacks |

📌 Using **both together** provides a layered defense.

---

## 🧪 Detection Techniques Used by IDS

IDS tools rely on **detection techniques** to identify threats.

### 1️⃣ Signature-Based Analysis

#### How It Works
- Uses predefined **signatures**
- Signatures represent known malicious patterns
- Activity is compared against these signatures

📌 If activity matches a signature:
- The event is logged
- An alert is generated

#### Real-World Example
- Alert triggered after **three failed login attempts**
- Indicates a possible **brute-force attack**

---

### ✅ Advantages of Signature-Based Analysis
- Low false positives
- Highly effective for known threats

### ❌ Disadvantages of Signature-Based Analysis
- Cannot detect unknown threats
- Requires frequent signature updates
- Attackers can slightly modify attacks to evade detection

---

## 2️⃣ Anomaly-Based Analysis

#### How It Works
Anomaly-based detection has two phases:

1. **Training Phase**
   - Establishes a baseline of normal behavior

2. **Detection Phase**
   - Compares current activity to the baseline
   - Deviations are logged and alerted

---

### ✅ Advantages of Anomaly-Based Analysis
- Can detect **unknown or zero-day attacks**
- Effective against new and evolving threats

### ❌ Disadvantages of Anomaly-Based Analysis
- High false positive rate
- Normal changes can trigger alerts
- If compromised during training, malicious behavior becomes “normal”

---

## 🧠 Signature vs Anomaly

| Feature | Signature-Based | Anomaly-Based |
|------|----------------|--------------|
| Detects known threats | Yes | Yes |
| Detects unknown threats | No | Yes |
| False positives | Low | High |
| Requires baseline | No | Yes |
| Maintenance | Signature updates | Baseline tuning |

---

## 📦 IDS Logs and SIEM Integration
IDS tools generate **IDS logs**, which include:
- Device details
- Network activity
- Detection results

These logs are often sent to:
- Centralized log servers
- SIEM platforms

📌 SIEM tools allow:
- Correlation across systems
- Faster investigations
- Centralized alerting

---

## 🧠 Key Takeaways
- Detection depends on logs and telemetry
- HIDS monitors individual hosts
- NIDS monitors network traffic
- Signature-based detection finds known threats
- Anomaly-based detection finds unknown threats
- IDS logs feed into SIEMs for analysis

---

## ✅ One-Line Summary

> Intrusion detection systems use logs and telemetry to monitor hosts and networks, applying signature-based and anomaly-based techniques to detect and alert on malicious activity.

---

**✍️ Notes By Abhishek (Ez Abyss)**
