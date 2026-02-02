# 📦 Packet Captures & Network Traffic Analysis  
**Network Monitoring**

---

## 1️⃣ Why Packet Captures Matter

Whether it’s:
- An employee sending an email  
- Or a malicious actor exfiltrating confidential data  

👉 **All actions on a network leave traces in network traffic flows**.

By examining these flows, security analysts gain:
- Visibility into what’s happening
- Context for investigations
- Evidence to confirm or dismiss threats

Packet captures allow analysts to **observe network communications directly**, instead of relying only on alerts or summaries.

---

## 2️⃣ Network Traffic Refresher

- **Network traffic**: The amount and type of data moving across a network
- **Network data**: The actual data transmitted between devices

Traffic analysis helps answer:
- Who is communicating?
- With whom?
- How often?
- Using which protocols?
- At what times?

---

## 3️⃣ What Is a Packet?

When data is sent over a network, it is **broken into packets**.

📬 **Mail analogy**
- Envelope → Packet
- Address → IP addresses
- Letter inside → Payload (data)

Packets are the **fundamental unit of network communication**.

---

## 4️⃣ Packet Components (Very Important)

Each packet has **three main components**:

---

### 🧾 Header
The header contains routing and control information, such as:
- Source IP address
- Destination IP address
- Protocol used (TCP, UDP, etc.)
- Port numbers
- Packet length and identifiers

📌 Think of this as the *name and address on an envelope*.

Packets may contain multiple headers:
- Ethernet header
- IP header
- TCP/UDP header

---

### 📦 Payload
The payload contains the **actual data** being transmitted.

Examples:
- Website content
- Email text
- Uploaded images
- File data

📌 This is the *letter inside the envelope*.

---

### 🏁 Footer (Trailer)
The footer:
- Marks the end of the packet
- Provides error-checking information (Ethernet)

⚠️ Note:
- Many protocols (like IP) do **not** use footers
- Footers may not always appear in packet analysis due to configuration

---

## 5️⃣ Why Packets Matter in Security

Packets provide **deep visibility** into:
- How data moves
- What protocols are used
- Whether behavior matches expectations

Detecting intrusions often starts **at the packet level**.

Example:
- Uploading an image → multiple packets sent
- Exfiltration → many outbound packets with unusual patterns

Understanding packet behavior helps analysts:
- Identify anomalies
- Reconstruct timelines
- Build attack narratives

---

## 6️⃣ Network Protocol Analyzers (Packet Sniffers)

A **network protocol analyzer**, also known as a **packet sniffer**, is a tool that:
- Captures network traffic
- Displays packets in human-readable format
- Allows detailed inspection of communications

Common tools:
- `tcpdump`
- `Wireshark`
- `TShark`

Uses include:
- Security investigations
- Network troubleshooting
- Performance analysis

⚠️ These tools can also be abused by attackers to steal sensitive data.

---

## 7️⃣ How Packet Sniffers Work

### Step 1: Capturing Traffic via NIC
- Network Interface Cards (NICs) send and receive traffic
- By default, NICs only process traffic addressed to them

To capture *all visible traffic*, NICs use:
- **Promiscuous mode** (wired networks)
- **Monitor mode** (wireless networks)

⚠️ Promiscuous mode increases risk and must be used responsibly.

---

### Step 2: Position Matters
- Packet sniffers must be placed in the correct network segment
- They only capture traffic they can “see”

---

### Step 3: Binary → Human-Readable
- Captured packets are raw binary (0s and 1s)
- Packet analyzers decode and display them in readable form

This allows analysts to:
- Inspect headers
- Review payloads (when possible)
- Analyze protocol behavior

---

## 8️⃣ Packet Captures (PCAPs)

A **packet capture (p-cap)** is:
> A file containing intercepted network packets

PCAPs provide:
- A snapshot of network communications
- Evidence for incident investigations
- Data for filtering and analysis

Example use:
- Filter PCAP to show packets from a specific IP
- Identify suspicious outbound connections

📌 Intercepting traffic **without permission** is illegal in many regions.

---

## 9️⃣ Packet Capture Formats & Libraries

You should be familiar with these:

### 🐧 Libpcap
- Used on Linux and macOS
- Default for tools like `tcpdump`

### 🪟 WinPcap
- Older Windows capture library
- Largely deprecated

### 🧰 Npcap
- Modern Windows capture library
- Developed by Nmap
- Widely used today

### 🆕 PCAPng
- “Next-generation” format
- Stores packets + metadata
- Supports advanced capture features

---

## 10️⃣ Analyst Pro Tip

🧪 **Practice on your own network**
- Capture traffic responsibly
- Analyze normal behavior
- Learn protocols and patterns

This builds intuition for spotting abnormal activity in real environments.

---

## 🔑 Key Takeaways

- Packet captures provide deep network visibility
- Packets are the foundation of network communication
- Headers, payloads, and footers each serve a purpose
- Packet sniffers capture and decode network traffic
- PCAPs are critical during incident investigations
- Proper placement and permissions are essential
- Understanding packets improves detection and defense

---

**✍️ Notes By Abhishek (Ez Abyss)**
