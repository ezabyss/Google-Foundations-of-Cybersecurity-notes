# ☁️🔐 Cryptography & Cloud Security


---

## 🎯 Big Picture

Cloud networks must be secured using a **combination of security hardening practices and cryptography**.

Just like on-premise networks, cloud environments face risks related to:

* Unauthorized access
* Misconfiguration
* Data exposure

> Cryptography plays a **critical role** in protecting cloud data and resources.

---

## 🧠 Cloud Security Hardening (Overview)

Cloud security hardening refers to the techniques used to:

* Secure cloud infrastructure
* Protect cloud data and applications
* Reduce attack surfaces

### Common Cloud Hardening Techniques

* Identity Access Management (IAM)
* Hypervisors
* Baselining
* Cryptography
* Cryptographic erasure

---

## 👤 Identity Access Management (IAM)

### 📌 Definition

**IAM** is a collection of processes and technologies that:

* Manage digital identities
* Control how users access cloud resources

🔐 Proper IAM ensures users only access what they are authorized to use.

---

## 🖥️ Hypervisors

### 📌 What Is a Hypervisor?

A **hypervisor** abstracts physical hardware from the operating system.

---

### 🔢 Types of Hypervisors

#### Type 1 (Bare-Metal)

* Runs directly on hardware
* Used by CSPs
* Example: VMware ESXi

#### Type 2 (Hosted)

* Runs on top of a host OS
* Example: VirtualBox

---

### ☁️ Hypervisors in the Cloud

* CSPs commonly use **Type 1 hypervisors**
* CSPs are responsible for:

  * Managing hypervisors
  * Applying patches and updates

---

### ⚠️ VM Escape Risk

A **VM escape** occurs when:

* A malicious actor escapes a virtual machine
* Gains access to the hypervisor or other VMs

> Customers rarely interact directly with hypervisors, but misconfigurations can still pose risks.

---

## 📐 Baselining in the Cloud

### 📌 Definition

A **baseline** is a fixed reference configuration used to:

* Compare changes
* Detect unauthorized modifications

---

### 🧱 Examples of Cloud Baselines

* Restricting admin portal access
* Enabling password management
* Enabling file encryption
* Enabling SQL threat detection

🔐 Proper baselining improves both **security and performance**.

---

## 🔐 Cryptography in the Cloud

### 📌 Purpose

Cryptography secures cloud data by ensuring:

* Confidentiality
* Integrity

It relies on:

* Encryption
* Secure key management

---

### 🔑 Encryption Explained

**Encryption** converts readable data into **ciphertext**.

* Ciphertext cannot be read without the encryption key
* Modern encryption relies on **key secrecy**, not algorithm secrecy

---

### 📍 Where Encryption Is Used

* Data at rest (stored data)
* Data processed in the cloud

> Encryption is one of the most effective ways to protect sensitive cloud data.

---

## 🧨 Cryptographic Erasure (Crypto-Shredding)

### 📌 Definition

**Cryptographic erasure** destroys data by:

* Deleting the encryption keys
* Making encrypted data unreadable

---

### 🔥 Why It’s Used in the Cloud

* Traditional data destruction is ineffective in cloud environments
* Destroying all copies of the key ensures data cannot be recovered

> Once the key is gone, the data is permanently inaccessible.

---

## 🗝️ Key Management

Modern encryption depends on **secure key storage and handling**.

---

### 🔐 Trusted Platform Module (TPM)

* Hardware chip
* Securely stores:

  * Passwords
  * Certificates
  * Encryption keys

---

### ☁️ Cloud Hardware Security Module (CloudHSM)

* Dedicated cloud-based hardware
* Performs:

  * Encryption
  * Decryption
  * Secure key storage

---

## ⚖️ CSP & Customer Responsibilities (Keys)

* CSPs encrypt customer data
* Customers may:

  * Use CSP-managed keys
  * Provide their own encryption keys

⚠️ If customers manage their own keys:

* They are responsible for key security
* CSP support is limited if keys are lost or compromised

---

## 🧾 Audits & Compliance

* Customers can request:

  * CSP audits
  * Security reports

* Federal contractors may rely on **FEDRAMP** for verified CSPs

---

## 🧠 Key Takeaways

* Cloud security requires both hardening and cryptography
* IAM controls access to cloud resources
* CSPs manage hypervisors, but misconfigurations still pose risk
* Baselining detects unauthorized changes
* Encryption protects data confidentiality
* Crypto-shredding permanently destroys cloud data

---

## 📝 Key Line

> *Cloud security is strengthened through IAM, secure hypervisor management, baselining, cryptography, and cryptographic erasure, ensuring confidentiality, integrity, and controlled access to cloud infrastructure and data.*

---

✨ Cryptography is the backbone of cloud data security
---
**✍️ Notes By Abhishek (Ez Abyss)**
