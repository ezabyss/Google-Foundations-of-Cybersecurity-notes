# 🧠 Assets in a Digital World

---

## 🌍 Big Question in Security
> **What exactly is valuable about an asset?**

In modern organizations, the most valuable asset is often **information**.

When information is stored, processed, or transmitted by computers, we call it **data**.

---

## 📊 What Is Data?
**Data** is information that is:
- Translated
- Processed
- Stored  
by a computer system.

In today’s connected world:
- Billions of devices are online
- Millions of data transactions happen every second

> 📌 This constant movement creates **new security risks**.

---

## 🔐 Why Data Needs Special Protection
Unlike physical assets, **data**:
- Can be copied instantly
- Can be accessed remotely
- Exists in multiple places at once

Protecting data depends on:
- **Where it is**
- **What it is doing**

---

## 🔁 The Three States of Data 

Security teams protect data in **three states**:

### 1️⃣ Data in Use
- Data being actively accessed
- Viewed, edited, or processed by users

📍 **Example:**  
Checking email on a laptop at a park.

---

### 🧠 SOC Scenario: Data in Use
**Situation:**  
A SOC alert detects unusual keystroke activity while a user is logged into a financial system.

**Risk:**  
- Credential misuse
- Insider threat
- Session hijacking

**SOC Action:**  
- Monitor session behavior
- Trigger identity verification
- Potentially terminate session

---

### 2️⃣ Data in Transit
- Data traveling between systems
- Moves across networks or the internet

📍 **Example:**  
Clicking “Send” on an email message.

---

### 🧠 SOC Scenario: Data in Transit
**Situation:**  
SOC detects unencrypted traffic containing login credentials.

**Risk:**  
- Man-in-the-middle attack
- Data interception

**SOC Action:**  
- Enforce encryption (TLS)
- Block insecure connections
- Alert network security team

---

### 3️⃣ Data at Rest
- Data not actively being accessed
- Stored on devices or servers

📍 **Example:**  
Laptop closed and stored in a bag.

---

### 🧠 SOC Scenario: Data at Rest
**Situation:**  
A laptop containing customer data is stolen.

**Key Questions:**
- Was the disk encrypted?
- What classification level was the data?
- Is breach notification required?

**SOC Action:**  
- Assess exposure
- Notify legal & compliance
- Begin incident response workflow

---

## 🔐 Information Security (InfoSec)

**Information Security (InfoSec)** is the practice of:
- Protecting data in **all three states**
- Preventing unauthorized access, use, disclosure, or destruction

---

## ⚠️ Consequences of Weak InfoSec
Poor data protection can lead to:
- Identity theft
- Financial loss
- Legal penalties
- Reputational damage

These impacts affect:
- Organizations
- Business partners
- Customers

---

## ☁️ The Changing Meaning of “Data at Rest”
Modern devices store data in the **cloud**.

📌 Even if your phone is resting on a table:
- Your data may still be active
- Cloud syncs may still be running

> ❗ Data is rarely truly “at rest” anymore.

---

## 🧠 Why Data States Matter to Asset Management
Understanding data states helps security teams:
- Analyze risk accurately
- Apply correct controls
- Build effective asset management plans

---

# ☁️ The Emergence of Cloud Security

---

## 🌐 What Is Cloud Computing?
Cloud computing is:
> An on-demand, massively scalable service hosted on shared infrastructure and accessed via the internet.

Cloud adoption has:
- Lowered costs
- Increased scalability
- Introduced new security challenges

---

## 🚀 Why Businesses Moved to the Cloud
Before the cloud:
- Companies built everything on-premises
- High cost and maintenance

With the cloud:
- Faster deployment
- Flexible scaling
- Lower upfront investment

---

## ☁️ Cloud-Based Services
Cloud services provide:
- Applications
- Development platforms
- Infrastructure

Delivered **on demand** over the internet.

---

## 🧱 Three Cloud Service Models (Very Important)

### 1️⃣ Software as a Service (SaaS)
- Front-end applications
- Accessed via web browser
- Provider manages everything backend

📍 Examples:
- Email services
- Collaboration tools
- Video conferencing

---

### 🧠 SOC Scenario: SaaS
**Situation:**  
Multiple failed login attempts on a SaaS email platform.

**SOC Focus:**
- Identity & access management
- Account takeover detection

---

### 2️⃣ Platform as a Service (PaaS)
- Development tools hosted in the cloud
- Clients build and deploy applications
- Provider manages infrastructure

📍 Used by developers to:
- Write code
- Deploy applications

---

### 🧠 SOC Scenario: PaaS
**Situation:**  
A web app built on PaaS exposes sensitive logs publicly.

**Root Cause:**  
- Misconfigured access permissions

**SOC Action:**  
- Secure application configuration
- Review developer access controls

---

### 3️⃣ Infrastructure as a Service (IaaS)
- Virtual servers
- Storage
- Networking resources

Clients control:
- Operating systems
- Security configurations

---

### 🧠 SOC Scenario: IaaS
**Situation:**  
SOC detects an exposed cloud storage bucket.

**Risk:**  
- Data leakage
- Regulatory violations

**SOC Action:**  
- Restrict access immediately
- Audit storage permissions
- Notify compliance team

---

## 🔐 Cloud Security Explained
**Cloud security** focuses on protecting:
- Data
- Applications
- Infrastructure  
hosted in the cloud.

---

## 🤝 Shared Responsibility Model (Critical Concept)

In cloud environments:
- **Security responsibility is shared**

### Customers are responsible for:
- Identity & access management
- Resource configuration
- Data handling

### Providers are responsible for:
- Physical infrastructure
- Underlying cloud services

> Responsibility varies by SaaS, PaaS, and IaaS.

---

## ⚠️ Major Cloud Security Challenges

### 🔧 1. Misconfiguration
- Most common cloud risk
- Default settings often insecure

### 🧠 SOC Impact:
- Cloud-native breaches
- Publicly exposed assets

---

### 👀 2. Monitoring & Visibility
- Harder to track access
- Shared infrastructure limits visibility

---

### 📜 3. Regulatory Compliance
Organizations must meet standards like:
- HIPAA
- PCI DSS
- GDPR

Failure = legal and financial consequences.

---

## 📈 Demand for Cloud Security Skills
As cloud adoption grows:
- Cloud security roles are in high demand
- SOC teams increasingly monitor cloud environments

> Cloud security is one of the fastest-growing cybersecurity specializations.

---

## 🧠 Key Takeaways

- Data is one of the most valuable assets
- Data exists in three states: in use, in transit, at rest
- Each state introduces unique risks
- Cloud computing changes how data is protected
- Security responsibility is shared in the cloud
- Misconfiguration is the leading cloud security risk
- Understanding cloud models is essential for SOC analysts

---

✍️ **Notes By Abhishek (Ez Abyss)**
