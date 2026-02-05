# 🧪 Live Network Traffic Analysis Using tcpdump

## Analyst Context
**Role:** Network / Security Analyst  
**Objective:** Capture, filter, and analyze live network traffic from a Linux system using `tcpdump`, and perform offline analysis on saved packet data.

---

## Scenario Overview
A Linux virtual machine was provided with an active network connection.  
The task was to identify network interfaces, capture live traffic, store HTTP packets in a capture file, and analyze the captured data using command-line packet analysis.

---

## Task 1 — Identify Network Interfaces

### Actions
- Enumerated available network interfaces using `sudo ifconfig`
- Identified `eth0` as the primary Ethernet interface
- Verified available capture interfaces using `sudo tcpdump -D`

### Findings
- `eth0` is the active interface used for external network communication
- `lo` is the loopback interface used for local traffic
- `tcpdump -D` confirmed `eth0` as a valid capture interface

---

## Task 2 — Inspect Live Network Traffic

### Actions
- Captured a small sample of live traffic using `sudo tcpdump -i eth0 -v -c5`

### Findings
- tcpdump successfully listened on `eth0`
- Packet output included timestamps, protocols, ports, and TCP flags
- Bidirectional TCP communication was observed
- TCP flags indicated active data transfer
- Push (`P`) and acknowledgment (`ACK`) flags confirmed payload delivery

---

## Task 3 — Capture HTTP Traffic to a File

### Actions
- Started background capture of HTTP traffic using  
  `sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &`
- Generated HTTP traffic using `curl opensource.google.com`
- Verified file creation using `ls -l capture.pcap`

### Findings
- Packet capture file `capture.pcap` was successfully created
- Captured traffic was limited to TCP port 80
- Background capture terminated automatically after 9 packets

---

## Task 4 — Analyze Captured Packet Headers

### Actions
- Read captured packet headers using `sudo tcpdump -nn -r capture.pcap -v`

### Findings
- Observed TCP three-way handshake:
  - SYN
  - SYN-ACK
  - ACK
- Source system initiated connection to an external web server on port 80
- TTL values and packet lengths aligned with standard TCP/IP behavior

---

## Task 5 — Inspect Packet Payload Data

### Actions
- Examined packet payloads using `sudo tcpdump -nn -r capture.pcap -X`

### Findings
- Packet data displayed in hexadecimal and ASCII formats
- Payload structure was consistent with HTTP request traffic
- No anomalies or suspicious patterns were observed

---

## Analyst Summary
This lab demonstrated effective use of `tcpdump` to:
- Identify active network interfaces
- Capture and filter live network traffic
- Store packet data for offline analysis
- Interpret packet headers, flags, and payload data

These skills are essential for incident response, network troubleshooting, and security investigations.


---

**✍️ Notes By Abhishek (Ez Abyss)**
