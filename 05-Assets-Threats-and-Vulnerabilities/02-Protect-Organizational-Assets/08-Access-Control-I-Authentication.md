# 🔐 Access Controls I: Authentication, SSO & MFA  
*Managing Identity, Access, and Trust (AAA Framework – Part 1)*

---

## 🌍 Why Access Controls Matter
Hashing and encryption protect data, but they are **not enough** on their own.

A critical question remains:
> **Who is allowed to access the information?**

This is where **access controls** come in.

Access controls manage:
- Access
- Authorization
- Accountability

When implemented correctly, they maintain:
- Confidentiality
- Integrity
- Availability  
while still allowing users to work efficiently.

---

## 🧩 The AAA Framework
Access controls are commonly organized into three related functions:

1. **Authentication** – Who are you?
2. **Authorization** – What are you allowed to do?
3. **Accounting** – What did you do?

This section focuses on **authentication**.

---

## 🔑 What Is Authentication?
**Authentication** is the process of verifying identity.

It answers one simple but critical question:
> **Who are you?**

Any person, device, or application attempting access must prove its identity before moving forward.

---

## 🧠 The Three Factors of Authentication
Authentication systems typically rely on one or more of these factors:

---
1. Knowledge - Something You Know
2. Ownership - Something You Have
3. Characteristics - Something You Are
---

### 1️⃣ Knowledge (Something You Know)
Information the user remembers.

Examples:
- Password
- PIN
- Answer to a security question

📌 Most common — and most frequently attacked.

---

### 2️⃣ Ownership (Something You Have)
Something the user possesses.

Examples:
- One-time passcode (OTP)
- Security token
- Mobile authentication app

📌 Often used to strengthen passwords.

---

### 3️⃣ Characteristic (Something You Are)
Biological or physical traits.

Examples:
- Fingerprint
- Facial recognition
- Iris scan

📌 Hardest to impersonate, increasingly common.

---

## ✅ Authentication Outcomes
- **Match found** → Access granted
- **No match** → Access denied

Incorrect denial is frustrating.  
Incorrect approval is **dangerous**.

---

## 🔁 Single Sign-On (SSO)

### What Is SSO?
**Single Sign-On (SSO)** allows a user to:
- Authenticate once
- Access multiple systems without re-logging in

📌 Like introducing yourself once instead of every time you meet the same friend.

---

### Why Organizations Use SSO
SSO is widely adopted because it:

- Improves user experience
- Reduces password fatigue
- Lowers IT management costs
- Reduces the number of attack entry points

---

## 🧠 Password Fatigue
Password fatigue occurs when:
- Users must remember many passwords
- Passwords are reused across services

This behavior creates serious security risks.

SSO solves this by shifting authentication complexity away from users.

---

## ⚙️ How SSO Works (High-Level)
SSO establishes trust by:
- Using a trusted identity provider
- Exchanging encrypted access tokens
- Allowing one login to authenticate multiple services

This works both:
- On-premises
- In the cloud

---

## ⚠️ Limitations of SSO
SSO **alone** can be risky.

### Main Risk:
- One compromised password
- Access to many systems

> Fewer logins ≠ stronger security by default.

---

## 🛡️ Multi-Factor Authentication (MFA)

### What Is MFA?
**Multi-Factor Authentication (MFA)** requires:
> **Two or more authentication factors** to verify identity.

MFA dramatically reduces the risk of unauthorized access.

---

### Real-World Analogy
ATM withdrawal:
1. Debit card (something you have)
2. PIN (something you know)

Both are required to access funds.

---

## 🔐 MFA Authentication Factors
MFA combines multiple factors, such as:

- **Something you know**  
  Username + password

- **Something you have**  
  OTP via SMS or app

- **Something you are**  
  Biometrics

This can be:
- 2FA (two factors)
- 3FA (three factors)

---

## 🧠 Why MFA Is So Effective
MFA:
- Prevents password-only compromise
- Protects cloud environments
- Makes impersonation extremely difficult
- Reduces brute-force success

Even if one factor is stolen, attackers still fail.

---

## 🔁 SSO + MFA = Layered Defense
SSO and MFA are often used together.

### Benefits:
- **SSO** → convenience and fewer passwords
- **MFA** → strong identity verification

Together they provide:
- Fast access for authorized users
- Strong protection against unauthorized users

---

## 🧠 SOC Scenario: Authentication Attack
**Situation:**  
Attacker steals employee password.

**Without MFA:**
- Full system access granted

**With MFA:**
- Login blocked
- SOC alerted
- Breach prevented

---

## 🎯 Key Takeaways
- Access controls manage who can access data
- Authentication answers “Who are you?”
- Authentication relies on knowledge, ownership, and characteristics
- Passwords alone are weak
- SSO reduces password fatigue but increases blast radius
- MFA significantly strengthens authentication
- Combining SSO and MFA balances usability and security
- SOC teams monitor authentication failures constantly

---

✍️ **Notes By Abhishek (Ez Abyss)**
