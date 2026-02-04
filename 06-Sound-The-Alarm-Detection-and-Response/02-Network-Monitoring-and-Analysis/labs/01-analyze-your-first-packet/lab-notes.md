# 🧪 Lab Notes — Network Traffic Analysis Using Wireshark

## Analyst Context
**Role:** Security Analyst  
**Objective:** Analyze captured network traffic associated with a user accessing a website and extract relevant indicators using Wireshark.

This analysis focuses on:
- Identifying communicating hosts
- Determining protocols in use
- Inspecting packet structure across layers
- Using filters to isolate relevant traffic efficiently

---

## Scenario Overview
A packet capture file was provided containing network traffic generated during a web browsing session.  
The goal of this analysis was to inspect the traffic to understand how systems communicate during a web connection and what data is exchanged at the packet level.

---

## Task 1 — Initial Packet Review

### Actions Taken
- Opened the provided packet capture file in Wireshark
- Maximized the application window for full visibility
- Reviewed the complete packet list prior to applying filters

### Observations
The packet list provided high-level metadata for each packet, including:
- Packet index number
- Timestamp
- Source and destination IP addresses
- Protocol type
- Packet size
- Summary of packet contents

Wireshark coloring rules were used to quickly differentiate traffic types:
- DNS traffic appeared in light blue
- TCP and HTTP traffic appeared in green

### Finding
Packets labeled as **“Echo (ping) request”** were identified as **ICMP traffic**, indicating network reachability testing.

---

## Task 2 — Filtered Packet Inspection

### Filter Applied
`ip.addr == 142.250.1.139`

### Result
Applying this filter reduced the dataset to packets where the specified IP address appeared as either the source or destination, allowing focused analysis of the web session.

### Packet Analysis
A TCP packet was selected for detailed inspection. The following protocol layers were reviewed:
- Frame
- Ethernet II
- Internet Protocol Version 4 (IPv4)
- Transmission Control Protocol (TCP)

### Findings
- Source and destination TCP ports matched those shown in the packet summary
- TCP flags were present and visible, indicating connection establishment behavior
- The destination TCP port observed was **80**, confirming the packet was associated with an HTTP web request

---

## Task 3 — Traffic Selection by IP and MAC Address

### Source IP Filter
`ip.src == 142.250.1.139`

**Result:** Displayed packets originating from the specified IP address.

### Destination IP Filter
`ip.dst == 142.250.1.139`

**Result:** Displayed packets sent to the specified IP address.

### MAC Address Filter
`eth.addr == 42:01:ac:15:e0:02`

### Packet Analysis
- The specified MAC address was confirmed under the Ethernet II layer
- The IPv4 layer was expanded to identify the encapsulated protocol

### Finding
The internal protocol carried within the IPv4 packet was identified as **TCP**.

---

## Task 4 — DNS Traffic Analysis

### Filter Applied
`udp.port == 53`

### DNS Query Analysis
- DNS query packets were inspected
- The queried domain name was identified as:

`opensource.google.com`

### DNS Response Analysis
- DNS response packets were reviewed
- The resolved IP address returned for the queried domain was:

`142.250.1.139`

### Finding
This confirmed successful name resolution for the requested website.

---

## Task 5 — TCP Web Traffic Analysis

### Filter Applied
`tcp.port == 80`

### Packet Analysis
The first TCP packet associated with web traffic was inspected in detail.

### Findings
- **Time To Live (TTL):** 64  
- **Frame Length:** 74 bytes  
- **IP Header Length:** 20 bytes  
- **Destination IP Address:** 169.254.169.254  

These values are consistent with standard IPv4 TCP web traffic.

---

### Payload Content Filtering

### Filter Applied
`tcp contains "curl"`

### Result
Packets containing payload data associated with the `curl` command were identified, indicating command-line-based web requests in the captured traffic.

---

## Analyst Summary
This analysis demonstrated how display filters and protocol layer inspection can be used to efficiently identify relevant network traffic, extract indicators, and understand system communication during a web session.

Key outcomes:
- Identified DNS resolution activity
- Confirmed HTTP traffic over TCP port 80
- Verified packet structure across Ethernet, IP, and TCP layers
- Used payload filtering to locate specific application behavior

---

## Lab Status
- Analysis completed successfully
- All required filters applied and validated
- Relevant network indicators identified

---

**✍️ Notes By Abhishek (Ez Abyss)**
