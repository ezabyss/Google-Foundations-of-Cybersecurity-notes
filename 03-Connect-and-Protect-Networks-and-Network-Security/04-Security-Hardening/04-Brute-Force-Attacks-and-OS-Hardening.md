# 🔐 Brute Force Attacks & OS Hardening

---

## 🎯 Why This Topic Matters

Brute force attacks directly target **usernames and passwords**, which are one of the **most widely used security controls**.

> If attackers break authentication, they can **compromise the entire network**.

OS hardening plays a **critical role** in preventing brute force and similar attacks.

---

## 🧠 What Is a Brute Force Attack?

### 📌 Definition

A **brute force attack** is a **trial-and-error process** used by attackers to discover private information, such as:

* Passwords
* Login credentials
* Encryption keys

Attackers repeatedly try combinations until they find one that works.

---

## 🔓 Why Login Credentials Are Vulnerable

Usernames and passwords are used on:

* Phones
* Computers
* Organizational systems
* Restricted applications

⚠️ **Main weakness:**

* Passwords can be **guessed, stolen, or reused**

Relying only on credentials makes systems vulnerable.

---

## 🧪 Types of Brute Force Attacks

### 1️⃣ Simple Brute Force Attack

* Attacker manually or automatically tries many username/password combinations
* Continues until correct credentials are found

🧠 *Low sophistication, but still effective against weak passwords*

---

### 2️⃣ Dictionary Attack

* Uses a list of:

  * Common passwords
  * Previously breached credentials

📖 Called a **dictionary attack** because attackers originally used word lists

⚠️ Very effective when users reuse passwords

---

## ⚙️ Automation in Brute Force Attacks

Manual brute force is slow, so attackers use:

* Automated tools
* Scripts
* Credential databases

> Automation makes brute force attacks **fast and scalable**.

---

## 🔍 Assessing Vulnerabilities Before Attacks

Organizations test systems **before real attacks occur**.

Goals:

* Identify vulnerabilities
* Test defenses
* Simulate attack scenarios

---

## 🖥️ Virtual Machines (VMs)

### 📌 Definition

A **virtual machine (VM)** is a **software-based version of a physical computer**.

### 🔐 Why VMs Are Used

* Run code in an **isolated environment**
* Prevent malware from affecting the host system
* Easily deleted and restored using clean images

---

### ⚠️ VM Limitations

* Small risk malware can escape virtualization
* Must still be configured securely

🧠 *VMs reduce risk but do not eliminate it completely*

---

## 🧪 Sandbox Environments

### 📌 Definition

A **sandbox** is a **separate testing environment** used to:

* Execute suspicious software
* Test patches
* Detect vulnerabilities
* Simulate cyberattacks

---

### 🧠 Sandbox Characteristics

* Can be physical or virtual
* Often cloud-based for cost efficiency
* Isolated from production systems

⚠️ Some malware can detect sandboxes and behave harmlessly

---

## 🛡️ Preventing Brute Force Attacks (OS Hardening)

### 1️⃣ Hashing & Salting

* **Hashing:** Converts passwords into irreversible values
* **Salting:** Adds random characters to passwords before hashing

🔐 Makes stolen hashes harder to crack

---

### 2️⃣ Multi-Factor Authentication (MFA) & Two-Factor Authentication (2FA)

* Requires **two or more verification factors**

Authentication factors:

* 🔑 Something you know → Password
* 📱 Something you have → Phone, OTP
* 🧬 Something you are → Fingerprint, face ID

> Even if passwords are compromised, MFA blocks access

---

### 3️⃣ CAPTCHA & reCAPTCHA

* Confirms users are human
* Prevents automated brute force attempts

🧠 reCAPTCHA is a widely used service from Google

---

### 4️⃣ Password Policies

Organizations enforce rules such as:

* Minimum password length
* Complexity requirements
* Password expiration
* Login attempt limits

🚫 Accounts may lock after multiple failed attempts

---

## 🧠 Key Takeaways

* Brute force = trial-and-error password guessing
* Simple & dictionary attacks are common
* VMs & sandboxes help assess vulnerabilities safely
* OS hardening reduces authentication risks
* MFA, hashing, CAPTCHA, and policies are key defenses

---

## 📝 Summary Line

> *Brute force attacks attempt to gain unauthorized access through repeated credential guessing. OS hardening techniques such as hashing and salting, MFA, CAPTCHA, password policies, and vulnerability testing with VMs and sandboxes significantly reduce the likelihood of successful brute force attacks.*

---

✨ Strong OS hardening = strong defense against brute force attacks

---
**Notes By Abhishek (Ez Abyss)**
