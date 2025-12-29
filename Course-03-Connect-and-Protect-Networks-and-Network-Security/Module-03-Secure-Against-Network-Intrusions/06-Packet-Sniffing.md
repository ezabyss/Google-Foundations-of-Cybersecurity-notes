# 📡 Packet Sniffing (Network Interception Attack)

## What is Packet Sniffing?

**Packet sniffing** is the practice of using software or hardware tools to **observe data packets as they travel across a network**.

Each data packet contains:
- **Header** → sender IP address and receiver IP address
- **Body (payload)** → actual data such as:
  - names
  - date of birth
  - personal messages
  - financial information
  - credit card numbers

---

## Legitimate vs Malicious Packet Sniffing

### Legitimate Use (Security Analysts)
Security analysts may use packet sniffing to:
- investigate ongoing security incidents
- debug network issues
- analyze suspicious traffic
- establish baseline network behavior

Tools such as **tcpdump** and **Wireshark** are commonly used for these purposes.

---

### Malicious Use (Threat Actors)
Malicious actors use packet sniffing to:
- spy on data not intended for them
- steal sensitive information
- modify data in transit
- gain unauthorized access to systems

This is similar to **opening someone else’s mail** — delivering it is allowed, reading it is not.

---

## How Attackers Perform Packet Sniffing

Attackers may:
- insert themselves between two communicating devices (on-path / man-in-the-middle)
- use packet sniffing tools to inspect every packet passing through their device
- extract valuable information from packet payloads
- modify packet contents (e.g., change a bank account number in a transfer)

Packet sniffing can be done using:
- software applications
- specialized hardware devices

---

## Types of Packet Sniffing Attacks

### Passive Packet Sniffing
- Data packets are **only read**, not changed
- Common on networks where traffic is visible to all devices (e.g., hubs)
- Difficult to detect

**Analogy:**  
A postal worker secretly reading letters while delivering them.

---

### Active Packet Sniffing
- Data packets are **modified or redirected** in transit
- May involve:
  - injecting protocols
  - redirecting packets to unintended ports
  - altering packet payloads

**Analogy:**  
A neighbor intercepts your mail, reads it, changes it, and then delivers it.

---

## Risks of Packet Sniffing
Packet sniffing can lead to:
- credential theft
- financial fraud
- identity theft
- data integrity violations
- loss of confidentiality

---

## How to Prevent Malicious Packet Sniffing

### 🔐 Use a VPN
- Encrypts all data in transit
- Masks IP address and virtual location
- Even if traffic is intercepted, it cannot be decoded

---

### 🔒 Use HTTPS (SSL/TLS)
- Encrypts web traffic
- Prevents eavesdropping
- Protects login credentials and form data

**Always check for:**  
`https://` in the website URL

---

### 📵 Avoid Unprotected Public Wi-Fi
Public Wi-Fi networks often:
- lack encryption
- allow attackers on the same network to sniff traffic easily

**Best practice:**
- Avoid public Wi-Fi when possible
- If necessary, always use **VPN + HTTPS**

---

## Key Takeaways
- Packet sniffing observes data packets traveling across a network
- Security analysts use it for investigation and troubleshooting
- Threat actors use it to steal or manipulate sensitive information
- Packet sniffing can be **passive (read)** or **active (modify)**
- VPNs, HTTPS, and avoiding unprotected Wi-Fi significantly reduce risk

---

**✍️Notes By Abhishek (Ez Abyss)**

