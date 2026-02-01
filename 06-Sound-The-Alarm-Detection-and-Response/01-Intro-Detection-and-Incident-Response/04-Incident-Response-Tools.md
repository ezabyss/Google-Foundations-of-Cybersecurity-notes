# 🧰 Detection Tools, Documentation, & the Analyst’s Toolbox  
**Incident Detection**

---

## 1️⃣ The Security Analyst’s Toolbox Mindset

As a **security analyst**, you are on the **front lines of incident detection**.  
Detection is not done with a single tool—just like a carpenter doesn’t build furniture using only a hammer.

🪚 **Carpenter analogy → Security reality**
- Measuring tape → Asset & log awareness
- Saw → Investigation tools
- Sandpaper → Documentation & refinement
- Full toolbox → Effective detection & response

🎯 An effective analyst combines:
- Security knowledge
- Detection tools
- Investigation tools
- Documentation practices

---

## 2️⃣ Categories of Tools Analysts Use

### 🔍 Detection & Monitoring Tools
Used to:
- Monitor system and network activity
- Detect suspicious or malicious behavior
- Generate alerts for investigation

Examples:
- IDS
- IPS
- EDR
- SIEM (covered later)

---

### 🧪 Investigation Tools
Used to analyze suspicious activity:
- Packet sniffers
- Log analysis tools
- Endpoint inspection tools

---

### 📓 Documentation Tools
Used to:
- Collect evidence
- Track decisions
- Support reporting and compliance

Your **incident handler’s journal** is your **first and most important tool**.

---

## 3️⃣ Documentation: A Core Security Skill

### What Is Documentation?

**Documentation** is any recorded information used to provide:
- Instruction
- Evidence
- Guidance
- Accountability

Forms of documentation include:
- Digital notes
- Handwritten notes
- Audio recordings
- Videos
- Reports

📌 There is **no universal industry standard** for documentation.  
Each organization defines its own practices based on:
- Business needs
- Legal requirements
- Regulatory obligations

---

## 4️⃣ Common Types of Security Documentation

- **Incident handler’s journal**
- **Playbooks**
- **Policies**
- **Plans**
- **Final incident reports**

Organizations may:
- Add new types
- Merge documents
- Remove unnecessary ones

📘 Documentation is tailored—just like security controls.

---

## 5️⃣ Effective vs Ineffective Documentation

### ❌ Ineffective Documentation
- Unclear steps
- Confusing layout
- Poor visuals
- Missing context

Result: Slower response, mistakes, frustration

---

### ✅ Effective Documentation
- Clear
- Consistent
- Accurate
- Easy to follow under pressure

🚨 During an incident, **clarity saves time** and reduces errors.

---

## 6️⃣ Common Documentation Tools

Analysts commonly use:
- Google Docs
- OneNote
- Evernote
- Notepad++
- Ticketing systems like Jira
- Google Sheets
- Audio recorders
- Cameras
- Handwritten notes

📌 Use whatever tools your organization approves—as long as documentation is **clear and reliable**.

---

## 7️⃣ Intrusion Detection Systems (IDS)

### What Is an IDS?

An **Intrusion Detection System (IDS)**:
- Monitors system and network activity
- Detects abnormal or suspicious behavior
- Generates alerts for investigation

📌 IDS **does not stop attacks**—it only detects and alerts.

---

### IDS Example

- Unknown IP attempts login at an unusual time
- IDS detects abnormal behavior
- Alert is sent to analysts
- Analyst investigates and responds

Examples of IDS tools:
- Zeek
- Suricata
- Snort
- Sagan

---

## 8️⃣ Intrusion Prevention Systems (IPS)

### What Is an IPS?

An **Intrusion Prevention System (IPS)**:
- Detects suspicious activity
- Automatically takes action to stop it

Examples of actions:
- Blocking traffic
- Modifying access control lists
- Terminating connections

📌 IPS = IDS + automated prevention

---

### IDS vs IPS (Simple Analogy)

- **IDS** → Alarm system (alerts only)
- **IPS** → Alarm + auto-locking doors

Many tools can function as **both IDS and IPS**:
- Suricata
- Snort
- Sagan

---

## 9️⃣ Endpoint Detection & Response (EDR)

### What Is EDR?

**Endpoint Detection and Response (EDR)**:
- Installed directly on endpoints
- Monitors endpoint behavior
- Uses behavioral analysis and automation

Endpoints include:
- Laptops
- Desktops
- Mobile devices
- Servers

---

### Why EDR Is Powerful

EDR tools:
- Collect detailed endpoint activity
- Use machine learning & AI
- Detect abnormal behavior patterns
- Automatically respond to threats

Example:
- Suspicious process starts on a workstation
- EDR detects unusual behavior
- Process is automatically blocked

Examples of EDR tools:
- Open EDR
- Bitdefender EDR
- FortiEDR

---

## 🔍 Detection Tool Comparison (Quick Reference)

| Capability | IDS | IPS | EDR |
|----------|-----|-----|-----|
| Detects malicious activity | ✓ | ✓ | ✓ |
| Prevents intrusions | ✗ | ✓ | ✓ |
| Logs activity | ✓ | ✓ | ✓ |
| Generates alerts | ✓ | ✓ | ✓ |
| Behavioral analysis | ✗ | ✗ | ✓ |

---

## 10️⃣ Detection Categories (Critical for Analysts)

### ✅ True Positive
- Attack occurs
- Alert correctly triggered

---

### ✅ True Negative
- No attack
- No alert triggered

---

### ❌ False Positive
- Alert triggered
- No real threat exists

⚠️ Wastes analyst time and resources

---

### ❌ False Negative
- Attack occurs
- No alert triggered

🚨 Most dangerous—attack goes unnoticed

---

## 11️⃣ Why Detection Tools Matter

Detection tools:
- Provide visibility into environments
- Alert analysts to suspicious activity
- Support investigation and response
- Reduce dwell time of attackers

📌 Detection is only valuable when paired with:
- Skilled analysts
- Proper documentation
- Effective response processes

---

## 🔑 Key Takeaways

- Analysts rely on **multiple tools**, not just one
- Documentation is a core security skill
- IDS detects, IPS detects + prevents, EDR analyzes behavior
- False positives waste time; false negatives create risk
- Detection tools provide awareness—not decisions
- Analysts turn alerts into action

---

**✍️ Notes By Abhishek (Ez Abyss)**
