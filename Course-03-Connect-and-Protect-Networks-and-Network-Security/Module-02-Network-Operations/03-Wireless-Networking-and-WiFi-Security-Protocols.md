# 📡 Wireless Networking & Wi-Fi Security Protocols (IEEE 802.11)
**Focus:** Wireless Communication, Wi-Fi Standards, WEP → WPA → WPA2 → WPA3  

---

## 1️⃣ What Is IEEE 802.11 (Wi-Fi)?

**IEEE 802.11** is a family of standards that define **wireless LAN (WLAN)** communication.

- **IEEE** = Institute of Electrical and Electronics Engineers  
- **802.11** = Wireless networking standards
- Commonly marketed as **Wi-Fi**

> **Key idea:**  
> Wi-Fi is not a single protocol — it’s a **suite of standards**.

---

## 2️⃣ Why Wireless Security Matters

Wireless networks transmit data using **radio waves**, which:
- Can be intercepted
- Don’t require physical access
- Are more exposed than wired networks

As a **security analyst**, you are responsible for:
- Ensuring encryption is strong
- Preventing unauthorized access
- Detecting insecure legacy protocols

---

## 3️⃣ Evolution of Wireless Networking

| Era | Key Development |
|---|---|
| Pre-1980s | Wired communication only |
| Mid-1980s | License-free radio spectrum |
| Late 1990s | First Wi-Fi protocols |
| Today | Secure, encrypted wireless networks |

Wireless devices now include:
- Laptops
- Smartphones
- Tablets
- IoT devices (thermostats, cameras, locks)

---

## 4️⃣ Wireless Security Protocols — Overview

Wi-Fi security protocols evolved to fix vulnerabilities in earlier versions.

| Protocol | Year | Status |
|---|---|---|
| WEP | 1999 | ❌ Insecure / deprecated |
| WPA | 2003 | ⚠ Transitional |
| WPA2 | 2004 | ✅ Standard (but aging) |
| WPA3 | 2018 | 🔒 Most secure |

---

## 5️⃣ Wired Equivalent Privacy (WEP)

### 🔹 What is WEP?
- First Wi-Fi security protocol
- Designed to match wired privacy

### ❌ Why WEP Failed
- Weak encryption
- Short keys
- Easily cracked

### 🚨 Security Risk
- Can be broken in minutes
- Considered **high-risk**

> **Analyst note:**  
> If you see WEP → **treat as critical vulnerability**

---

## 6️⃣ Wi-Fi Protected Access (WPA)

### 🔹 Why WPA Was Created
- Replace WEP
- Improve encryption
- Maintain backward compatibility

### 🔐 Key Improvements
- Uses **TKIP (Temporal Key Integrity Protocol)**
- Larger keys than WEP
- Adds **message integrity checks**

### ⚠ Major Vulnerability: KRACK
- Attackers manipulate the authentication handshake
- Can force encryption keys to all zeros
- Makes traffic readable

> **Result:** WPA was replaced by WPA2

---

## 7️⃣ WPA2 — The Wi-Fi Security Standard

### 🔹 Why WPA2 Is Better
- Uses **AES (Advanced Encryption Standard)**
- Replaces TKIP with **CCMP**
- Strong encryption + integrity + authentication

### 🔐 Encryption Stack
- AES → Encryption
- CCMP → Message authentication + integrity

> **Industry standard** for Wi-Fi security (for many years)

---

## 8️⃣ WPA2 Modes: Personal vs Enterprise

### 🏠 WPA2 Personal
| Feature | Description |
|---|---|
| Authentication | Shared passphrase |
| Best for | Home networks |
| Setup | Simple |
| Risk | Password sharing |

---

### 🏢 WPA2 Enterprise
| Feature | Description |
|---|---|
| Authentication | Individual user credentials |
| Best for | Organizations |
| Access control | Centralized |
| Key exposure | Users never see keys |

> **Security insight:**  
> Enterprise mode prevents key theft from endpoints

---

## 9️⃣ WPA3 — Modern Wi-Fi Security

### 🔹 Why WPA3 Exists
- Fix KRACK vulnerability
- Strengthen authentication
- Improve encryption

### 🔐 Key Security Improvements

| Feature | WPA2 | WPA3 |
|---|---|---|
| Handshake | Vulnerable | Secure |
| Auth method | PSK | SAE |
| Encryption | 128-bit | 128-bit / 192-bit |
| Offline attacks | Possible | Prevented |

---

### 🔹 Simultaneous Authentication of Equals (SAE)
- Password-authenticated key exchange
- Prevents offline brute-force attacks
- No data capture for cracking

> **Mental model:**  
> WPA3 locks the door *before* data moves

---

## 🔐 Security Analyst Takeaways

- **Never use WEP**
- **Avoid WPA**
- **WPA2 Enterprise > WPA2 Personal**
- **WPA3 is the future**
- Legacy devices = security risk

---

## 🎯 Summary

> “IEEE 802.11 defines wireless LAN communication.  
> Wireless security evolved from WEP to WPA, WPA2, and WPA3 to address encryption and authentication weaknesses.  
> Modern secure networks should use WPA2-Enterprise or WPA3 to prevent key reuse, handshake attacks, and unauthorized access.”

---

## 🧠 Memory Anchors

- **Wi-Fi = IEEE 802.11**
- **WEP = broken**
- **WPA = temporary**
- **WPA2 = AES + CCMP**
- **WPA3 = SAE + stronger encryption**
- **Enterprise > Personal**

---

**✍️ Notes by Abhishek (Ez Abyss)**  
