# 🌐 Network Protocols & Secure Communication
**Focus:** Network Protocols, TCP/IP Layers, Security Implications  

---

## 1️⃣ What Are Network Protocols?

Networks benefit from **rules**.  
These rules are called **network protocols**.

### 📌 Definition
A **network protocol** is a set of rules that:
- Define **how data is structured**
- Define **how data is transmitted**
- Define **the order of delivery**
- Tell the receiving device **what to do with the data**

> **Mental model:**  
> Protocols are a *common language* that allows devices across the world to communicate correctly.

---

## 2️⃣ Why Protocols Matter for Security

Even though protocols enable communication, they can also be **abused**.

### 🔐 Security perspective
- Malicious actors exploit **protocol misuse**
- Traffic may look legitimate but use the **wrong protocol**
- Detecting protocol misuse can stop attacks early

> **Real-world insight:**  
> “Correct IP + correct volume + wrong protocol = red flag”

---

## 3️⃣ Real-World Scenario: Visiting a Website

When you type a website like:
`www.yummyrecipesforme.org`

Your system silently uses **multiple protocols together**.

### 🔁 Protocol flow (high-level)
1. **DNS** → Resolves domain name to IP address  
2. **TCP** → Establishes a reliable connection (handshake)  
3. **ARP** → Finds the next device’s MAC address on the path  
4. **HTTPS** → Securely requests and receives web content  

> **Key insight:**  
> One simple action uses **multiple protocols across layers**.

---

## 4️⃣ Categories of Network Protocols

Network protocols fall into **three main categories**:

| Category | Purpose |
|------|------|
| Communication | Transfer data between devices |
| Management | Monitor and manage networks |
| Security | Protect data in transit |

---

## 5️⃣ Communication Protocols

### 🔹 Transmission Control Protocol (TCP)
- Connection-oriented
- Reliable delivery
- Uses a **three-way handshake**

**Handshake steps:**
1. SYN  
2. SYN-ACK  
3. ACK  

**TCP/IP layer:** Transport  
**Security relevance:** Used when reliability matters (web, email, file transfer)

---

### 🔹 User Datagram Protocol (UDP)
- Connectionless
- Faster but less reliable
- No handshake

**Common use:** DNS queries  
**TCP/IP layer:** Transport  
**Security note:** Easier to spoof than TCP

---

### 🔹 Hypertext Transfer Protocol (HTTP)
- Transfers web content
- Uses **port 80**
- No encryption

**TCP/IP layer:** Application  
**Security risk:** Data sent in plaintext

---

### 🔹 Domain Name System (DNS)
- Translates domain names to IP addresses
- Uses **UDP port 53**
- Switches to TCP for large responses

**TCP/IP layer:** Application  
**Security risk:** DNS spoofing and redirection attacks

---

## 6️⃣ Management Protocols

### 🔹 Simple Network Management Protocol (SNMP)
- Monitors and manages network devices
- Can modify device configuration

**TCP/IP layer:** Application  
**Security note:** Weak SNMP configs expose networks

---

### 🔹 Internet Control Message Protocol (ICMP)
- Reports network errors
- Used by `ping`

**TCP/IP layer:** Internet  
**Security note:** Can be abused for reconnaissance

---

## 7️⃣ Security Protocols

### 🔹 HTTPS
- Secure version of HTTP
- Uses **SSL/TLS encryption**
- Uses **port 443**

**TCP/IP layer:** Application  
**Security benefit:** Prevents eavesdropping

---

### 🔹 Secure File Transfer Protocol (SFTP)
- Secure file transfers
- Uses **SSH**
- Uses **port 22**

**TCP/IP layer:** Application  
**Common use:** Cloud storage uploads/downloads

---

## 8️⃣ Additional Critical Protocols

### 🔹 Network Address Translation (NAT)
- Maps private IPs to one public IP
- Performed by routers/firewalls

**Why it exists:**
- Conserves IPv4 addresses
- Adds a layer of obscurity

**TCP/IP layers:** Internet + Transport

---

### 🔹 Dynamic Host Configuration Protocol (DHCP)
- Automatically assigns:
  - IP address
  - DNS server
  - Default gateway

**Ports:**
- Server: UDP 67
- Client: UDP 68

**TCP/IP layer:** Application

---

### 🔹 Address Resolution Protocol (ARP)
- Maps IP addresses to MAC addresses
- Used inside local networks

**TCP/IP layer:** Network Access  
**Security risk:** ARP spoofing attacks

---

## 9️⃣ Remote Access Protocols

### 🔹 Telnet
- Remote command-line access
- Sends data in plaintext
- Uses **port 23**

**Security note:** Insecure, deprecated

---

### 🔹 Secure Shell (SSH)
- Secure remote access
- Encrypted communication
- Uses **port 22**

**Security benefit:** Replaces Telnet

---

## 🔟 Email Protocols

### 🔹 POP3
- Downloads emails to local device
- Uses:
  - Port 110 (unencrypted)
  - Port 995 (encrypted)

**Limitation:** Poor multi-device syncing

---

### 🔹 IMAP
- Keeps email on server
- Syncs across devices
- Uses:
  - Port 143 (unencrypted)
  - Port 993 (encrypted)

---

### 🔹 SMTP
- Sends and routes emails
- Uses:
  - Port 25 (unencrypted)
  - Port 587 (encrypted)

**Security note:** Port 25 often abused by spam

---

## 1️⃣1️⃣ Protocols & Ports Summary

| Protocol | Port |
|------|------|
| DHCP | UDP 67 / 68 |
| ARP | None |
| Telnet | TCP 23 |
| SSH | TCP 22 |
| POP3 | 110 / 995 |
| IMAP | 143 / 993 |
| SMTP | 25 / 587 |
| HTTP | 80 |
| HTTPS | 443 |
| DNS | 53 |

---

## 🔐 Security Takeaways

- Protocols define **intent**
- Port numbers define **behavior**
- Firewalls filter traffic by **protocol + port**
- Misused protocols often indicate attacks

> **Analyst mindset:**  
> “Is this protocol expected, appropriate, and secure?”

---

## 🎯 Summary

> “Network protocols govern how data is transmitted, managed, and secured across networks.  
> Understanding protocols, their ports, and TCP/IP layers allows security analysts to detect misuse, mitigate vulnerabilities, and prevent attacks.”

---

## 🧠 Memory Anchors

- **TCP = reliable**
- **UDP = fast**
- **DNS = name to IP**
- **HTTPS = encrypted web**
- **SSH > Telnet**
- **IMAP > POP3**
- **Ports reveal intent**

---

**✍️ Notes by Abhishek (Ez Abyss)**  
