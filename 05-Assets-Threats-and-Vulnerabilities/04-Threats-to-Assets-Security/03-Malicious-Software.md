# 🦠 Malware: Understanding Digital Infections 

## 1. What is Malware?
**Malware (malicious software)** is software designed to harm devices, networks, or data.  
Just like humans can get sick from viruses, computers can get “infected” by malware.

### Key Characteristics
- Designed to **disrupt normal operations**
- Often works **without user knowledge or consent**
- Can spread:
  - Through infected USB drives
  - Over networks and the internet
  - Via phishing emails and malicious downloads

📌 **SOC relevance:**  
Malware infections are a **top incident category** handled by SOC analysts due to their speed, scale, and impact.

---

## 2. Core Malware Types (High-Yield)

### 🧬 Virus
**Definition:**  
Malicious code that hides inside trusted programs and spreads when the user runs the infected file.

**Key Traits**
- Requires **user action** to activate
- Clones itself into other files
- Often spread via phishing attachments

🧠 **SOC Scenario**  
An employee opens a “Payroll_Update.exe” attachment.  
Endpoint detection alerts show abnormal file replication activity.  
➡️ Analyst isolates the device and scans for file-based infections.

---

### 🐛 Worm
**Definition:**  
Malware that **self-replicates** and spreads across networks **without user action**.

**Key Traits**
- Scans networks automatically
- Exploits shared access or vulnerabilities
- Can spread extremely fast

**Real Example:**  
Blaster (MSBlast) Worm  
- Affected Windows XP / 2000
- Caused endless reboot loops
- Spread globally

🧠 **SOC Scenario**  
Network traffic spikes abnormally between internal hosts.  
Multiple systems crash simultaneously.  
➡️ Analyst identifies lateral movement → blocks network segment.

---

### 🐴 Trojan (Trojan Horse)
**Definition:**  
Malware disguised as a **legitimate application or file**.

**Key Traits**
- Relies on **deception**
- Often installs additional malware
- Common delivery method for ransomware

🧠 **SOC Scenario**  
User downloads “Free_PDF_Converter.exe”.  
Shortly after, outbound C2 traffic appears.  
➡️ Analyst discovers trojan installing a secondary payload.

---

### 💰 Ransomware
**Definition:**  
Malware that **encrypts data** and demands payment for decryption.

**Key Traits**
- Makes itself known to the victim
- Uses encryption to lock files
- No guarantee attackers will restore access

**Famous Example:**  
WannaCry (2017)

🧠 **SOC Scenario**  
File server becomes inaccessible.  
Ransom note detected across endpoints.  
➡️ Analyst initiates incident response, isolates systems, checks backups.

---

### 🕵️ Spyware
**Definition:**  
Malware that secretly collects and sells information **without consent**.

**Common Targets**
- Login credentials
- PINs
- Browsing behavior

📌 Difference from legitimate tracking:
- Legitimate software allows **opt-out**
- Spyware does not

🧠 **SOC Scenario**  
User reports account takeover.  
Logs show credential reuse after freeware installation.  
➡️ Analyst traces spyware bundled in third-party software.

---

## 3. Potentially Unwanted Applications (PUAs)

### 📢 Adware
- Displays advertisements
- Can slow systems
- Malicious adware benefits attackers, not developers

### 😱 Scareware
- Fake warnings (“Your system is infected!”)
- Tricks users into installing malware

🧠 **SOC Scenario**  
User installs “Antivirus Alert Tool” from pop-up.  
System performance degrades.  
➡️ Analyst removes scareware and educates user.

---

## 4. Advanced Malware Types

### 🧠 Fileless Malware
**Definition:**  
Malware that operates **only in memory**, never touching disk.

**Why it’s dangerous**
- Evades traditional antivirus
- Uses legitimate system tools

📌 **Detection method:**  
Memory analysis

🧠 **SOC Scenario**  
No malicious files found, but PowerShell behavior is abnormal.  
➡️ Analyst performs memory inspection → detects fileless payload.

---

### 🔑 Rootkits
**Definition:**  
Malware that provides **remote administrative access**.

**Key Purpose**
- Backdoor access
- Install additional malware

**Delivery Mechanisms**
- Dropper: delivers hidden malware
- Loader: downloads additional payloads later

🧠 **SOC Scenario**  
System shows persistent admin access even after reboots.  
➡️ Analyst suspects rootkit → rebuilds system.

---

### 🤖 Botnets
**Definition:**  
A network of infected computers controlled by a **bot-herder**.

**Uses**
- DDoS attacks
- Spam campaigns
- Credential harvesting

🧠 **SOC Scenario**  
Endpoint communicates periodically with unknown external IP.  
Multiple hosts show same behavior.  
➡️ Analyst identifies botnet command-and-control pattern.

---

## 5. How Malware Spreads 
- Phishing emails
- Malicious attachments
- USB devices
- Insecure freeware
- Network vulnerabilities

📌 **User awareness + layered defenses** are critical.

---

## 6. Key Takeaways 
- Malware is **diverse and evolving**
- Many infections rely on **human error**
- Detection may require:
  - Endpoint monitoring
  - Network analysis
  - Memory inspection
- SOC analysts must **identify, isolate, eradicate, and educate**

---

### 📝 Notes by Abhishek (Ez Abyss)
