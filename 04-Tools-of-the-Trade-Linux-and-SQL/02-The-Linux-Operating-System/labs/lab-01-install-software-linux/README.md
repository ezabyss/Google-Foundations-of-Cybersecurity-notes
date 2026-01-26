# 📦 Lab 01: Install Software in a Linux Distribution

## Overview
This lab demonstrates how to install, remove, and manage software on a Debian-based Linux system using the **Advanced Package Tool (APT)**. The activity focuses on installing security-related tools commonly used in network monitoring and security operations.

All tasks were completed using the **Bash shell** in a Linux environment.

---

## Scenario
As a security analyst, you are required to install and manage network security tools on a Linux system. In this scenario, you must:

- Verify that the APT package manager is installed
- Install and uninstall the Suricata application
- Install the tcpdump application
- Confirm which applications are currently installed
- Reinstall Suricata and verify both tools are present

These tasks reflect common responsibilities in security operations and system administration roles.

---
## Tools & Applications Used

### 🔹 APT (Advanced Package Tool)
APT is a package management system used in Debian-based Linux distributions. It simplifies the installation, removal, and updating of software by automatically handling dependencies and package versions.

---

### 🔹 Suricata
Suricata is an open-source **Intrusion Detection System (IDS)** and **Intrusion Prevention System (IPS)**. It is commonly used in cybersecurity environments to monitor network traffic, detect malicious activity, and analyze network threats in real time.

Suricata is widely deployed in Security Operations Centers (SOC) and enterprise networks.

---

### 🔹 tcpdump
tcpdump is a command-line packet analysis tool used for capturing and inspecting network traffic. It helps security analysts and network engineers troubleshoot network issues, analyze packet flows, and detect suspicious activity.

---

## Tasks Performed

### 1. Confirm APT Installation
```bash
apt --version
```

### 2. Install Suricata
```
sudo apt update
sudo apt install suricata -y
```

### 3. Unistall Suricata
```
sudo apt remove suricata -y
```
### 4. Install tcpdump
```
sudo apt install tcpdump -y
```

### 5. Reinstall Suricata
```
sudo apt install suricata -y
```
