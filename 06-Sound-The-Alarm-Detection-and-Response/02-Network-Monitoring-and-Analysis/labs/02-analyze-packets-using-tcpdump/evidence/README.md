# 📸 Evidence — tcpdump Network Traffic Analysis Lab

## Overview
This directory contains terminal output screenshots collected during the execution of the **Live Network Traffic Capture and Analysis using tcpdump** lab.

The evidence demonstrates successful completion of each task, including interface identification, live traffic inspection, packet capture, and offline packet analysis.

---

## Task 1 — Identify Network Interfaces

**Command(s) used:**  
`sudo ifconfig`  
`sudo tcpdump -D`

**Evidence file:**  
- `task-1-identify-network-interfaces.png`

**Observed Results:**
- `eth0` identified as the active Ethernet interface
- `lo` identified as the loopback interface
- `tcpdump -D` confirmed available capture interfaces, including `eth0` and `any`

---

## Task 2 — Inspect Live Network Traffic

**Command used:**  
`sudo tcpdump -i eth0 -v -c5`

**Evidence file:**  
- `task-2-inspect-network-traffic-of-network-interface.png`

**Observed Results:**
- tcpdump successfully captured live traffic on `eth0`
- TCP and UDP packets observed
- TCP flags such as `P.` and `ACK` visible
- TTL values and packet lengths displayed
- No packet drops reported by the kernel

---

## Task 3 — Capture Network Traffic to a File

**Command(s) used:**  
`sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &`  
`curl opensource.google.com`  
`ls -l capture.pcap`

**Evidence file:**  
- `task-3-capture-network-traffic.png`

**Observed Results:**
- HTTP traffic successfully generated using `curl`
- `capture.pcap` file created
- Exactly 9 packets captured
- No packets dropped by the kernel
- Capture process terminated automatically after reaching packet count

---

## Task 4 — Analyze Captured Packet Header Data

**Command used:**  
`sudo tcpdump -nn -r capture.pcap -v`

**Evidence file:**  
- `task-4-filter-the-packet-header-data-from-capture.png`

**Observed Results:**
- TCP three-way handshake observed (SYN, SYN-ACK, ACK)
- Source system initiated connection to external IP on port 80
- TTL values consistent with standard TCP/IP behavior
- HTTP request and response packets identified

---

## Task 5 — Inspect Packet Payload Data (Hex & ASCII)

**Command used:**  
`sudo tcpdump -nn -r capture.pcap -X`

**Evidence file:**  
- `task-4-filter-the-extended-packet-data-from-the-capture.png`

**Observed Results:**
- Packet payloads displayed in hexadecimal and ASCII formats
- HTTP GET request visible
- HTTP 301 Moved Permanently response identified
- Redirect location to `https://opensource.google/` observed
- Payload structure consistent with legitimate web traffic

---

## Evidence Summary
The collected evidence confirms:
- Correct identification of capture interfaces
- Successful live packet capture
- Proper filtering of HTTP traffic
- Accurate saving and offline analysis of packet data
- Visibility into both packet headers and payload content

This evidence supports the findings documented in `lab-notes.md`.

---

**✍️ Notes By Abhishek (Ez Abyss)**
