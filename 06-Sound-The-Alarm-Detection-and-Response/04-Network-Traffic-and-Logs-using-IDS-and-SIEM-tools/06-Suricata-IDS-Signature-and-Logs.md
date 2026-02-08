### 📝 Writing, Reading, and Understanding Detection Rules

---

## 🎯 Why This Matters

Signature-based detection is one of the **core skills of a Security Analyst**.  
Tools like **Suricata** rely on signatures (rules) to decide:

- What network traffic is suspicious
- When to generate alerts
- How analysts detect real attacks vs noise

Think of signatures as **custom-built sensors** placed inside your network.

---

## 🌍 Real-World Analogy

Imagine a **metal detector at an airport**:

- It only alerts when **specific conditions** are met
- Sensitivity can be adjusted
- Poor tuning causes too many false alarms

Suricata signatures work the same way.

---

## 🧱 Components of a Suricata Signature

Every Suricata rule has **three core parts**:

1. **Action** – What Suricata should do
2. **Header** – What traffic to inspect
3. **Rule Options** – Why the traffic is suspicious

---

## 🧪 Example Custom Suricata Rule (HTTP)

```
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established; content:"GET"; sid:12345; rev:1;)
```


---

## 🔍 Rule Breakdown (Line by Line)

### 1️⃣ Action

`alert`

➡️ Generate an alert when all rule conditions are met.

Common actions:
- `alert` → Log and alert
- `pass` → Ignore traffic
- `drop` → Block traffic (IPS mode)

---

### 2️⃣ Header

`http $HOME_NET any -> $EXTERNAL_NET any`

| Field | Meaning |
|-----|--------|
| `http` | Inspect HTTP traffic |
| `$HOME_NET` | Internal network |
| `any` | Any source port |
| `->` | Direction of traffic |
| `$EXTERNAL_NET` | Outside network |
| `any` | Any destination port |

📌 This means:  
**HTTP traffic leaving the internal network to the internet**

---

### 3️⃣ Rule Options

Rule options are:
- Inside parentheses `( )`
- Separated by semicolons `;`
- Evaluated in order

| Option | Purpose |
|------|--------|
| `msg` | Alert message shown to analysts |
| `flow` | Matches traffic state |
| `content` | Inspects packet payload |
| `sid` | Unique signature ID |
| `rev` | Rule version |

---

## 🧠 Key Options Explained

### 🔹 `flow:established`

- Matches only **successfully established connections**
- Prevents triggering on half-open or failed connections
- Reduces false positives

---

### 🔹 `content:"GET"`

- Searches packet payload for the string `GET`
- `GET` is an HTTP method used to request data
- Indicates **actual HTTP requests**, not just connections

---

### 🔹 `sid` (Signature ID)

- Must be **unique**
- Used by SIEMs to track alerts
- Required for rule management

Example:
- `sid:12345`

---

### 🔹 `rev` (Revision)

- Tracks rule changes
- Incremented whenever the rule is modified

Example:
- `rev:1` → Initial rule
- `rev:2` → Tuned to reduce noise

---

## 🧠 What This Rule Detects

This signature **alerts when**:

- An HTTP connection is established
- Traffic flows from internal → external network
- The HTTP request contains `GET`

📌 In plain English:  
> “Alert me when a system inside my network makes an HTTP GET request to the internet.”

---

## 📂 Where Suricata Rules Live

Suricata configuration files are typically stored in:

- `/etc/suricata/`
- Custom rules are stored in `rules/custom.rules`

Useful commands:
- Change directory: `cd /etc/suricata`
- List rules: `ls rules`
- View rules: `less rules/custom.rules`

---

## 🪵 Suricata Logs (EVE JSON)

Suricata outputs logs in **EVE JSON format**.

### 🔹 Alert Logs
- Generated when a signature matches
- Include signature details (`sid`, `msg`, IPs)

### 🔹 Network Telemetry Logs
- Record normal network activity
- Example: HTTP requests, DNS queries
- Not always security-related

📌 Both are essential for building an investigation timeline.

---

## 🆚 Log File Comparison

| File | Purpose |
|----|--------|
| `eve.json` | Detailed logs (SIEM-ready) |
| `fast.log` | Minimal alert info (legacy) |

➡️ **Always prefer `eve.json`** for analysis and ingestion.

---

## ⚠️ Common Beginner Mistakes

- Writing rules too broad
- Forgetting to increment `rev`
- Reusing an existing `sid`
- Alerting on normal business traffic

Top analysts **tune**, not just detect.

---

## 🏁 Key Takeaways

- Suricata uses **signature-based detection**
- Rules = Action + Header + Options
- `flow` and `content` reduce false positives
- Custom rules are essential for real environments
- `eve.json` is critical for investigations and SIEMs

---

**✍️ Notes By Abhishek (Ez Abyss)**

