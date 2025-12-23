# 🌐 OSI Model — Layers, Functions & Security Perspective  

---

## 🧠 Why the OSI Model Matters

So far, network communication has been explained using the **TCP/IP model**, which is commonly used in real-world networking.  
The **OSI (Open Systems Interconnection) model** expands on this by providing a **more detailed, seven-layer view** of how data moves across a network.

Security and network professionals use the OSI model to:
- Understand network communication in detail  
- Identify where problems or attacks occur  
- Communicate clearly during troubleshooting and incident response  

📌 The OSI model is **conceptual**, meaning it explains processes — not physical implementations.

---

## 📌 TCP/IP Model vs OSI Model

| Model | Layers | Purpose |
|----|----|----|
| TCP/IP | 4 layers | Practical, used in real networks |
| OSI | 7 layers | Detailed, used for learning and analysis |

📌 The TCP/IP model is a **condensed version** of the OSI model.

---

## 🧩 The Seven Layers of the OSI Model  
---

## 7️⃣ Application Layer

The **application layer** is where the **user interacts with the network**.

### What happens here:
- Applications request and receive network services
- User-facing communication occurs

### Examples:
- Web browsing using HTTP or HTTPS  
- Email using SMTP  
- Website lookups using DNS  

🔐 **Security relevance:**  
Most attacks that involve users (phishing, malicious downloads, web attacks) occur at this layer.

---

## 6️⃣ Presentation Layer

The **presentation layer** focuses on **data formatting and security**.

### Key functions:
- Data translation
- Encryption and decryption
- Compression

📌 Ensures data sent by one system can be understood by another.

### Example:
- SSL/TLS encryption used by HTTPS

🔐 **Security relevance:**  
This layer protects data confidentiality during transmission.

---

## 5️⃣ Session Layer

The **session layer** manages **connections (sessions)** between devices.

### Responsibilities:
- Establishing a session
- Maintaining the session during communication
- Closing the session after completion
- Authentication and reconnection
- Setting checkpoints during data transfer

📌 If a connection drops, checkpoints allow communication to resume from the last point.

🔐 **Security relevance:**  
Session hijacking and unauthorized access often target this layer.

---

## 4️⃣ Transport Layer

The **transport layer** controls **data delivery between devices**.

### Responsibilities:
- Segmenting large data into smaller pieces
- Controlling flow and speed
- Ensuring data reaches the correct service
- Reassembling data at the destination

### Protocols:
- **TCP** — reliable, connection-based  
- **UDP** — fast, connectionless  

🔐 **Security relevance:**  
Port scanning, unauthorized connections, and traffic abuse occur at this layer.

---

## 3️⃣ Network Layer

The **network layer** determines **where data packets should go**.

### What happens here:
- IP addresses are used to identify destinations
- Routers forward packets between networks
- Communication between different networks occurs

📌 Data packets include IP addresses to guide routing decisions.

🔐 **Security relevance:**  
IP spoofing, routing attacks, and network-level scanning occur here.

---

## 2️⃣ Data Link Layer

The **data link layer** manages communication **within a local network**.

### Responsibilities:
- Organizing packet delivery on the same network
- Managing MAC addresses
- Controlling switches and network interface cards (NICs)

### Example protocols:
- Network Control Protocol (NCP)
- High-Level Data Link Control (HDLC)
- Synchronous Data Link Control (SDLC)

🔐 **Security relevance:**  
ARP spoofing and local network attacks occur at this layer.

---

## 1️⃣ Physical Layer

The **physical layer** represents the **actual hardware** used to transmit data.

### Includes:
- Cables and wiring
- Hubs and modems
- Electrical or radio signals

📌 Data is converted into **0s and 1s** and sent across physical media.

🔐 **Security relevance:**  
Physical access to devices or cables can compromise network security.

---

## 🔐 Why Security Professionals Use the OSI Model

Security teams use the OSI model to:
- Identify which layer an attack occurred in
- Understand which protocols were affected
- Narrow down troubleshooting efforts
- Communicate clearly during investigations

Each layer represents a **potential attack surface**.

---

## ✅ Key Takeaways

- The OSI model has seven layers
- It provides a detailed view of network communication
- TCP/IP is a simplified version of the OSI model
- Each OSI layer has specific responsibilities
- Security issues can be mapped to individual layers
- The OSI model helps with analysis and communication

---

## 🎯 One-Line 
**The OSI model is a seven-layer conceptual framework that explains how data is transmitted across networks and helps security professionals identify where problems or attacks occur.**

---

✍️ *Notes By Abhishek (Ez Abyss)*
