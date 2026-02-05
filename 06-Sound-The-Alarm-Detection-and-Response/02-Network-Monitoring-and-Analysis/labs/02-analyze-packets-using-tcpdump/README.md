# 🧪 Live Network Traffic Analysis with tcpdump

## Overview
This lab demonstrates how to capture and analyze live network traffic on a Linux system using `tcpdump`. The focus is on identifying network interfaces, filtering traffic during capture, saving packets to a capture file, and performing offline packet analysis.

This lab builds foundational skills required for network monitoring, incident response, and security investigations.

---

## Scenario
You are a **network/security analyst** investigating live traffic on a Linux virtual machine. Your objective is to observe traffic on an active interface, isolate HTTP traffic, and analyze packet headers and payload data.

---

## Objectives
By completing this lab, you will be able to:
- Identify network interfaces available for packet capture
- Inspect live network traffic using `tcpdump`
- Capture filtered traffic to a `.pcap` file
- Analyze packet headers from a saved capture
- Inspect packet payload data in hexadecimal and ASCII formats

---

## Tools & Environment
- Linux virtual machine
- `tcpdump`
- Bash shell
- HTTP traffic generated using `curl`

---

## Lab Tasks
1. Identify network interfaces using `sudo ifconfig` and `sudo tcpdump -D`
2. Inspect live traffic on `eth0` using `sudo tcpdump -i eth0 -v -c5`
3. Capture HTTP traffic using `sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &`
4. Generate traffic with `curl opensource.google.com`
5. Analyze packet headers using `sudo tcpdump -nn -r capture.pcap -v`
6. Inspect packet payload data using `sudo tcpdump -nn -r capture.pcap -X`

Detailed execution steps and findings are documented in `lab-notes.md`.

---

## Repository Structure
- `README.md`
- `lab-notes.md`
- `evidence/`

---

## Evidence
The `evidence/` directory contains screenshots or terminal outputs showing:
- Network interface identification
- Live traffic capture
- Packet capture file creation
- Offline packet analysis

---

## Learning Outcome
This lab provides hands-on experience with command-line packet analysis. The ability to capture, filter, and interpret network traffic using `tcpdump` is a critical skill for security analysts working in real-world environments.

---

## Status
- Lab completed
- Packet capture created and analyzed
- Objectives achieved

---

**✍️ Notes By Abhishek (Ez Abyss)**
