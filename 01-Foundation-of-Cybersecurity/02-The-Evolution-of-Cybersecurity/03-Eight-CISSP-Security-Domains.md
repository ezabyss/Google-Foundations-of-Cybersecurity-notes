# Introduction to the Eight CISSP Security Domains  
_Notes by Abhishek (EzAbyss)_

---

## 1. Why security **domains** matter

As threats evolve, security roles also change. To make sense of all the work security professionals do, CISSP groups core concepts into **eight security domains**.

- Domains = **big categories of security work**
- All domains are **connected** → a gap in one domain can impact the whole organization  
- Knowing the domains helps you:
  - Understand **how an organization stays secure**
  - See **which kind of work you enjoy most** → future career path
  - Prepare for **job interviews** and role descriptions

---

## 2. Quick overview of all 8 domains

| # | Domain                              | One-line idea                                                   |
|---|-------------------------------------|------------------------------------------------------------------|
| 1 | Security and Risk Management        | Define goals, manage risk, law, compliance, business continuity |
| 2 | Asset Security                      | Protect & manage data and physical/digital assets               |
| 3 | Security Architecture & Engineering | Design & build secure systems/tools                             |
| 4 | Communication & Network Security    | Secure networks & communications (wired and wireless)           |
| 5 | Identity & Access Management (IAM)  | Make sure the **right people** have the **right access**        |
| 6 | Security Assessment & Testing       | Test and audit security controls                                |
| 7 | Security Operations                 | Day-to-day monitoring, response, investigations                 |
| 8 | Software Development Security       | Build security into software and apps                           |

---

## 3. Domain 1 – Security and Risk Management

**Focus:**  
Define the organization’s **security goals**, manage **risk**, ensure **compliance**, and keep the business running even during incidents.

**Key topics:**

- Security **goals & objectives**
- **Risk mitigation** (identify, analyze, treat risks)
- **Compliance** (laws, standards, regulations)
- **Business continuity** & **disaster recovery**
- Legal & regulatory requirements (e.g., **HIPAA** for health data)

**Example:**  
A new federal rule changes how private health information must be handled.  
→ Security analyst updates **policies and procedures** so the company stays compliant with HIPAA.

**Think:**  
> “Are we doing the **right things** to manage risks and follow laws?”

---

## 4. Domain 2 – Asset Security

**Focus:**  
Protect and properly handle the organization’s **assets**, especially **data**.

**Key topics:**

- Identifying assets: **digital** (data, software) and **physical** (devices, servers)
- **Storage, maintenance, retention, and destruction** of data
- Data **classification** (public, internal, confidential, etc.)
- Secure disposal of old hardware and media

**Example:**  
Old laptops are being thrown away.  
→ Analyst makes sure drives are **wiped or destroyed** so no confidential data is leaked.

**Think:**  
> “What do we own, where is it, and how do we protect and dispose of it safely?”

---

## 5. Domain 3 – Security Architecture and Engineering

**Focus:**  
Design and build **secure systems**, and make sure the right **tools and processes** are in place.

**Key topics:**

- Designing secure **architectures** (networks, systems, applications)
- Implementing security **controls** (technical, administrative, physical)
- Using devices like **firewalls**, IDS/IPS, etc.
- Ensuring systems are configured securely

**Example:**  
You configure a **firewall** to filter incoming and outgoing traffic.  
→ If configured correctly, it **reduces attacks** and improves productivity.

**Think:**  
> “Is our technical design strong enough to resist attacks?”

---

## 6. Domain 4 – Communication and Network Security

**Focus:**  
Secure **network infrastructure** and **communications** (wired, wireless, remote).

**Key topics:**

- Securing **LANs, WANs, VPNs**
- Securing **wireless** networks
- Network **segmentation**, IDS/IPS, monitoring
- Policies for safe network usage

**Example:**  
You notice users connecting to **unsecured public Wi-Fi**.  
→ You create a **network policy** and technical controls to block or limit such connections and reduce exposure.

**Think:**  
> “Are our network paths and communication channels safe?”

---

## 7. Domain 5 – Identity and Access Management (IAM)

**Focus:**  
Make sure that **only the right people** get the **right type of access** to physical and digital resources.

**Key topics:**

- User **identities** (who you are)
- **Authentication** (proving you are who you say you are)
- **Authorization** (what you can do)
- Physical access (keycards, doors, offices)
- Logical access (applications, networks, systems)
- User roles and permissions documentation

**Example:**  
You configure **keycard access** so only authorized employees can enter certain buildings or rooms.

**Think:**  
> “Who are you, and what are you allowed to access?”

---

## 8. Domain 6 – Security Assessment and Testing

**Focus:**  
**Check** and **test** if security controls are working as expected.

**Key topics:**

- Security **control testing**
- **Vulnerability assessments**
- **Security audits**
- Collecting and analyzing security data
- Regular reviews of **user permissions**

**Example:**  
You audit payroll system access.  
→ You check that only HR and finance have access, and no unauthorized user can see salaries.

**Think:**  
> “Are our security controls effective and correctly implemented?”

---

## 9. Domain 7 – Security Operations

**Focus:**  
Day-to-day running of security: **monitoring**, **incident response**, and **investigation**.

**Key topics:**

- Monitoring systems and alerts (SIEM, logs)
- **Incident response** processes
- **Forensics** and investigations
- Applying **preventive measures** (blocking IPs, isolating systems)
- Operational tasks (backups, patching, account management)

**Example:**  
You get an alert that an **unknown device** is on the internal network.  
→ You follow incident response procedures to **investigate and contain** the threat quickly.

**Think:**  
> “What is happening **right now**, and how do we respond?”

---

## 10. Domain 8 – Software Development Security

**Focus:**  
Build and maintain **secure software** by using **secure coding practices**.

**Key topics:**

- **Secure coding** guidelines and standards
- Security in the **software development lifecycle (SDLC)**
- Code reviews & security testing
- Protecting user data in applications

**Example:**  
A partner team builds a new **mobile app**.  
→ You help define **password policies**, secure storage of user data, and security checks during development.

**Think:**  
> “Is security built into our software from the beginning?”

---

## 11. How the domains work together

- **Security and Risk Management** (1) sets the **direction and rules**
- **Asset Security** (2) decides **what** needs protection
- **Architecture & Engineering** (3) builds the **technical foundation**
- **Communication & Network Security** (4) protects **data in transit**
- **IAM** (5) controls **who** can access **what**
- **Assessment & Testing** (6) checks if controls **really work**
- **Operations** (7) handles **real-time events and incidents**
- **Software Development Security** (8) ensures apps are **secure by design**

If one domain is weak (for example, poor IAM), an attacker might get access even if your network and architecture are strong.

---

## 12. Memory helpers

### 12.1 Order of the 8 domains

**S A S C I S S S**

You can remember it with a sentence (make your own, but here’s one):

> **S**mart **A**nalysts **S**ecure **C**ommunications, **I**nspect **S**ystems, **S**top **S**hocks.

Or just repeat the order:

1. **S**ecurity and Risk Management  
2. **A**sset Security  
3. **S**ecurity Architecture & Engineering  
4. **C**ommunication & Network Security  
5. **I**dentity & Access Management  
6. **S**ecurity Assessment & Testing  
7. **S**ecurity Operations  
8. **S**oftware Development Security  

### 12.2 1–4 vs. 5–8

- **1–4** → Foundations and infrastructure  
  - Policies, assets, architecture, networks  
- **5–8** → People, checking, doing, and building  
  - Users, testing, operations, secure coding  

---

## 13. Quick revision checklist

When revising, try to answer these in your own words:

- **Domain 1:** How does an organization decide what is “acceptable risk”?  
- **Domain 2:** How do we securely handle old hard drives or files?  
- **Domain 3:** What is the role of a firewall in security architecture?  
- **Domain 4:** Why is connecting to public Wi-Fi risky for a company?  
- **Domain 5:** What’s the difference between authentication and authorization?  
- **Domain 6:** What is a security audit and why is it important?  
- **Domain 7:** What steps do we follow when a suspicious device appears on the network?  
- **Domain 8:** Why should security be considered at the **start** of software development?

---
