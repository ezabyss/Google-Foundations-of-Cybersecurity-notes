# 🔎 Investigate Packet Details with Wireshark  
**Packet Analysis**

---

## 1️⃣ Why Packet Analysis Matters

Packets are the **foundation of all network communication**, which means:
> **Detection begins at the packet level.**

As a security analyst, packet analysis helps you:
- Understand what’s happening on a network
- Identify suspicious or malicious activity
- Validate alerts from SIEM, IDS, or EDR
- Build a clear incident timeline

Packet captures can be **large and noisy**, so efficient analysis techniques are critical.

---

## 2️⃣ Internet Protocol (IP) Refresher

The **Internet Protocol (IP)** defines how packets are:
- Addressed
- Routed
- Delivered across networks

IP ensures packets reach the correct destination.

### Two IP Versions in Use
- **IPv4** – Most widely used
- **IPv6** – Newer version with a much larger address space

Both use headers to structure packet information.

---

## 3️⃣ IPv4 Header Overview (13 Fields)

IPv4 headers contain metadata essential for routing and analysis.

| **Field** | **Purpose** |
|---------|-----------|
| Version | Indicates IP version (IPv4). |
| IHL (Internet Header Length) | Length of the IPv4 header including options. |
| ToS (Type of Service) | Packet priority and delivery handling. |
| Total Length | Size of entire packet (header + data). |
| Identification | Identifies packet fragments for reassembly. |
| Flags | Controls and indicates fragmentation. |
| Fragment Offset | Position of a fragment within the original packet. |
| TTL (Time to Live) | Limits packet lifetime to prevent infinite routing. |
| Protocol | Identifies next-layer protocol (e.g., TCP = 6). |
| Header Checksum | Error-checking for the header. |
| Source Address | Sender’s IP address. |
| Destination Address | Receiver’s IP address. |
| Options | Optional diagnostic or security features. |

---

## 4️⃣ IPv6 Header Overview (8 Fields)

IPv6 simplifies the header while expanding addressing capability.

| **Field** | **Purpose** |
|---------|-----------|
| Version | Indicates IP version (IPv6). |
| Traffic Class | Packet priority (similar to IPv4 ToS). |
| Flow Label | Identifies packets belonging to the same flow. |
| Payload Length | Length of the data portion only. |
| Next Header | Type of header that follows (e.g., TCP). |
| Hop Limit | Limits packet travel (similar to TTL). |
| Source Address | Sender’s IPv6 address. |
| Destination Address | Receiver’s IPv6 address. |

📌 Both IPv4 and IPv6 headers provide **valuable investigative context**, even when payloads are encrypted.

---

## 5️⃣ Wireshark: Packet Analysis Made Visual

**Wireshark** is an open-source **network protocol analyzer** with a graphical interface (GUI).

Why analysts love Wireshark:
- Human-readable packet display
- Powerful filtering
- Easy stream reconstruction
- Protocol-based color coding

📌 You’ll focus on **display filters** to efficiently analyze packet captures.

---

## 6️⃣ Display Filters: Your Most Important Skill

Display filters allow you to:
- Reduce noise
- Isolate relevant packets
- Focus on evidence that matters

You can filter by:
- Protocols
- IP addresses
- Ports
- MAC addresses
- Payload content

---

## 7️⃣ Comparison Operators (Quick Reference)

Wireshark supports both **symbols** and **abbreviations**.

| **Operator Type** | **Symbol** | **Abbreviation** |
|------------------|-----------|----------------|
| Equal | `==` | `eq` |
| Not equal | `!=` | `ne` |
| Greater than | `>` | `gt` |
| Less than | `<` | `lt` |
| Greater than or equal | `>=` | `ge` |
| Less than or equal | `<=` | `le` |

Example (both are equivalent):
- `ip.src == 8.8.8.8`
- `ip.src eq 8.8.8.8`

📌 You can combine operators using `and`, `or`, and parentheses.

---

## 8️⃣ Special Filter Operators

### 🔍 Contains
Finds packets containing a **specific string**.

Example:
- Filter HTTP packets containing the word `"moved"`

Useful for:
- Web traffic analysis
- Identifying redirects or messages

---

### 🧬 Matches (Regex)
Uses **regular expressions** to match patterns.

Useful for:
- Complex searches
- Pattern-based detection

📌 Regex skills become powerful as you advance.

---

## 9️⃣ Filtering by Protocol

Simply type the protocol name:

Examples:
- `dns`
- `http`
- `ftp`
- `ssh`
- `arp`
- `icmp`
- `telnet`

📌 Wireshark color-codes protocols for easier visual inspection.

---

## 🔟 Filtering by IP Address

### Any IP address
`ip.addr == 172.21.224.2`

### Source IP only
`ip.src == 10.10.10.10`

### Destination IP only
`ip.dst == 4.4.4.4`

---

## 1️⃣1️⃣ Filtering by MAC Address

MAC addresses uniquely identify network interfaces.

Example:
`eth.addr == 00:70:f4:23:18:c4`

Useful for:
- Layer 2 investigations
- Tracking specific devices

---

## 1️⃣2️⃣ Filtering by Port

### UDP port example (DNS)
`udp.port == 53`

### TCP port example (SMTP)
`tcp.port == 25`

📌 Port filtering helps isolate specific services quickly.

---

## 1️⃣3️⃣ Follow Streams (Power Feature)

A **stream** is a full conversation between devices using a protocol.

Wireshark can:
- Reassemble packets
- Display the conversation clearly
- Show requests and responses together

Examples:
- Follow HTTP stream
- Follow TCP stream

📌 This is extremely useful for:
- Web investigations
- Credential exposure analysis
- Command-and-control inspection

---

## 🔑 Key Takeaways

- Packet analysis provides deep visibility into network activity
- IPv4 and IPv6 headers contain critical metadata
- Wireshark simplifies packet inspection with a GUI
- Display filters are essential for efficiency
- Operators, protocol, IP, MAC, and port filters speed investigations
- Follow streams reconstruct real conversations
- Packet analysis skills improve with practice

---

**✍️ Notes By Abhishek (Ez Abyss)**
