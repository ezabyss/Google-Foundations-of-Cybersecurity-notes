# 🛡️ Security Zones & Network Segmentation
**Module:** Network Security Measures  
**Focus:** Security Zones, Network Segmentation, DMZ, Access Control  

---

## 1️⃣ What Are Security Zones?
A **security zone** is a segmented portion of a network that applies specific **access controls** and **security rules** to protect systems and data.

Security zones are part of a broader strategy called **network segmentation**.

> **Simple idea:** Security zones divide a network so **not everyone can access everything**.

---

## 2️⃣ Why Security Zones Matter
Without segmentation:
- A compromised device can spread malware
- Attackers can move laterally across the network
- Sensitive data is harder to isolate and protect

With security zones:
- Access is **controlled**
- Damage is **contained**
- Privacy is **maintained**
- Attacks are **isolated**

📌 **Security goal:** limit the **blast radius** of an incident.

---

## 3️⃣ Network Segmentation Explained
**Network segmentation** divides a network into multiple segments (subnets/VLANs), each with:
- Its own security rules
- Its own access permissions
- Firewall/ACL controls between segments

### Real-world examples
**🏨 Hotel Wi‑Fi**
- Guest Wi‑Fi (untrusted)
- Staff Wi‑Fi (secured/encrypted)
- Separated so guest malware can’t reach staff systems

**🎓 University**
- Faculty subnet
- Student subnet
- Admin subnet  
If one subnet is compromised, others stay protected.

---

## 4️⃣ Zone Types (Big Picture)
Organizations classify networks into two main categories:

### 🌐 Uncontrolled zone
Any network **outside** the organization’s control (ex: **the internet**). Treat as **untrusted**.

### 🏢 Controlled zone
Networks **inside** the organization’s control, protected by policies and firewalls. This usually contains multiple layers/zones.

---

## 5️⃣ DMZ (Demilitarized Zone)
The **DMZ** is the “public-facing” zone inside the controlled network.

### What typically lives in the DMZ?
Services that must talk to the internet:
- Web servers
- DNS servers
- Proxy servers / reverse proxies
- Email gateways
- File transfer gateways (for external exchange)

> **Purpose:** expose needed services **without exposing internal systems**.

---

## 6️⃣ Internal Network Zone
The **internal zone** contains private systems used by employees and business operations, such as:
- Internal applications
- Databases (often not directly internet-facing)
- Employee devices
- Internal file shares

This zone should be protected from:
- The uncontrolled zone (internet)
- Compromised DMZ hosts

---

## 7️⃣ Restricted Zone (High-Security Zone)
The **restricted zone** contains the most sensitive assets:
- Highly confidential data
- Financial/HR systems
- Critical databases
- Intellectual property

Access here is **least-privilege**:
- Strong authentication
- Tight firewall rules
- Extra monitoring/logging

> **Mental model:** Restricted zone = the **vault** inside the building.

---

## 8️⃣ Firewalls & Zone Placement (Defense in Depth)
Security zones are enforced using **multiple firewalls** (or segmented firewall policies).

### Ideal layout 
```text
Internet (Uncontrolled)
        |
    [Firewall 1]
        |
       DMZ
        |
    [Firewall 2]
        |
  Internal Network
        |
    [Firewall 3]
        |
  Restricted Zone
```

**Why multiple firewalls?**
- Layered defense (defense-in-depth)
- Reduces lateral movement
- Contains compromises inside a zone

---

## 9️⃣ Traffic Control Between Zones
Security teams control traffic between zones using:
- **Port-based rules** (e.g., allow TCP 443 only)
- **IP allowlists/denylists**
- **Least privilege** (deny-by-default)
- **Monitoring + logging** for investigation

### Example
Allow only **HTTPS (TCP 443)** from the internet to the **web server in the DMZ**, block everything else.

📌 Rule style: **Allow what you need. Deny the rest.**

---

## 🔐 Security Analyst Responsibilities
A security analyst may:
- Help design segmentation and zone boundaries
- Configure/validate firewall rules and access control policies
- Monitor traffic crossing zones (logs/alerts)
- Investigate lateral movement attempts
- Contain incidents by isolating affected zones

---

## 🎯 Summary
> “Security zones are a network segmentation method that controls access between different areas of a network. Organizations typically separate the internet (uncontrolled) from controlled zones such as the DMZ, internal network, and restricted zone. Firewalls enforce rules between zones to prevent attacks from spreading and to protect sensitive assets.”

---

## 🧠 Memory Anchors
- **Uncontrolled zone = internet**
- **DMZ = public services**
- **Internal zone = private business systems**
- **Restricted zone = crown jewels**
- **Firewalls = zone enforcers**

---

✍️ **Notes by Abhishek (Ez Abyss)**
