# 🧪 Tcpdump Deep Dive: Capturing, Filtering & Interpreting Packets  
**Command-Line Packet Analysis**

---

## 1️⃣ What Is tcpdump?

**tcpdump** is a **command-line network protocol analyzer** used to:
- Capture live network traffic
- Inspect packets in real time
- Save traffic for later analysis (PCAP files)

Why analysts use tcpdump:
- Pre-installed on many Linux systems
- Lightweight and fast
- Great for servers and remote troubleshooting
- Powerful filtering for investigations

---

## 2️⃣ Permissions: Why `sudo` Is Required

Packet sniffing requires elevated privileges, so tcpdump is commonly run with `sudo`.  
Example: `sudo tcpdump -i any -v -c 1`

---

## 3️⃣ Basic tcpdump Syntax

General format: `sudo tcpdump [-i interface] [options] [expressions]`

- `-i` selects the interface (example: `-i any`)
- options control output/behavior
- expressions filter traffic

---

## 4️⃣ List Network Interfaces

To view available interfaces, use `sudo tcpdump -D`.

Common interfaces:
- `eth0`, `wlan0`, `lo`
- `any` (captures from all interfaces)

---

## 5️⃣ Simple Capture Command (Explained)

Command: `sudo tcpdump -i any -v -c 1`

Meaning:
- `-i any` → capture traffic from all interfaces
- `-v` → verbose output (more packet/IP header details)
- `-c 1` → capture only one packet

---

## 6️⃣ How to Read tcpdump Output (What You’ll See)

Each packet prints as one line starting with:

- **Timestamp** (useful for timelines)
- **IP** indicates IPv4 (or `IP6` for IPv6)
- **ToS** shown in hex (traffic handling/priority)
- **TTL** time-to-live (hop limit)
- **ID/Flags/Offset** fragmentation-related fields (example: `DF` = don’t fragment)
- **proto** protocol field (example: TCP is `6`)
- **length** packet size (header + data)
- **SourceIP.Port > DestIP.Port** direction + ports
- **cksum** header checksum validation
- TCP details like **flags** (example: `P` push, `.` ACK)

---

## 7️⃣ Save Traffic to a PCAP File (`-w`)

Write captures to a file using `-w`.

Example: `sudo tcpdump -i any -w packetcapture.pcap`

Why this matters:
- Offline analysis later
- Share with teammates
- Open in Wireshark

---

## 8️⃣ Read a PCAP File (`-r`)

To read a saved capture: `sudo tcpdump -r packetcapture.pcap`

Add verbose output: `sudo tcpdump -r packetcapture.pcap -v`

---

## 9️⃣ Verbosity Levels

- `-v` = more detail
- `-vv` = more than `-v`
- `-vvv` = maximum detail

Example: `sudo tcpdump -r packetcapture.pcap -vv`

---

## 🔟 Packet Count Control (`-c`)

Limit how many packets tcpdump captures:
- `sudo tcpdump -i any -c 3`

---

## 1️⃣1️⃣ Best Practice: Disable Name Resolution (`-n`, `-nn`)

By default, tcpdump may convert:
- IP → hostname (reverse DNS)
- port → service name (like `80` → http)

This can be misleading and can alert attackers via DNS lookups.

Best practice:
- `-n` disables hostname resolution
- `-nn` disables hostname + port/service resolution

Example: `sudo tcpdump -r packetcapture.pcap -v -nn`

---

## 1️⃣2️⃣ Filtering with Expressions (SOC-Useful)

Filter IPv6: `ip6`  
Filter IPv4: `ip`  
Filter by port: `port 80`  
Filter TCP: `tcp`  
Filter UDP: `udp`

Combine filters:
- `sudo tcpdump -r packetcapture.pcap -nn 'ip and port 80'`
- `sudo tcpdump -r packetcapture.pcap -nn 'ip and (port 80 or port 443)'`

---

## 1️⃣3️⃣ Mini SOC Scenario (Data Exfil Triage)

Goal: quickly review web traffic paths where exfil might hide.

Use: `sudo tcpdump -r packetcapture.pcap -nn 'tcp and (port 80 or port 443)'`

Then look for:
- unusual destinations
- large bursts of outbound packets
- traffic at odd hours (compare with baseline)

---

## 🔑 Key Takeaways

- tcpdump is a core CLI tool for packet capture and analysis
- `sudo` is usually required
- use `-w` to save PCAPs and `-r` to read them
- `-nn` is best practice to avoid misleading resolution
- filter expressions help you find what matters fast

---

**✍️ Notes By Abhishek (Ez Abyss)**
