# 🔐 Access Controls II: Authorization  
*Defining What Users Are Allowed To Do (AAA Framework – Part 2)*

---

## 🌍 Why Authorization Matters
Access control is not just about **who you are** (authentication), but also about:

> **What you are allowed to do**

Authorization assigns responsibility, permissions, and limits across:
- Users
- Systems
- Networks
- Applications
- Processes

Strong authorization protects sensitive data while enabling productivity.

---

## 🧩 Authentication vs Authorization
These two controls work **together**, but they are not the same.

| Control | Question Answered |
|------|------------------|
| Authentication | Who are you? |
| Authorization | What can you do? |

Authentication always comes **first**.  
Authorization follows **only after identity is verified**.

---

## 🔑 Authorization & Least Privilege
Authorization is tightly linked to the **principle of least privilege**.

### Least Privilege Means:
- Access is **limited**
- Access is **temporary**
- Access exists **only while needed**

> Permissions should be revoked when the task is complete.

---

## 🧠 Separation of Duties (SoD)
Authorization is also guided by **separation of duties**.

### Separation of Duties:
A security principle stating that:
> No single user should have enough permissions to misuse a system.

---

### Examples:
- A customer service employee **should not** evaluate their own performance
- A developer **should not** be the only person testing their own security system

📌 Separation of duties reduces:
- Fraud
- Abuse
- Undetected failures

---

## 🌐 Authorization Applies to More Than People
Authorization controls apply to:
- Users
- Applications
- Databases
- Networks
- Automated processes

Any system that accesses data must be **explicitly authorized**.

---

## 🌐 Authorization in Networked Systems
When securing data over networks, two common authorization technologies are:

- HTTP Basic Authentication
- OAuth

---

## 🌐 HTTP Basic Authentication (Basic Auth)

### What Is It?
A simple authorization mechanism used by web servers.

Basic auth:
- Sends a user identifier with each request
- Often includes username and password

---

### Security Risk
Basic auth is considered **insecure** because:
- Credentials are transmitted openly
- Vulnerable to interception

📌 Still found in legacy systems.

---

## 🔐 HTTPS: A Secure Upgrade
Most modern websites use **HTTPS** instead of HTTP.

### HTTPS:
- Encrypts communication
- Protects credentials in transit
- Prevents exposure of usernames and passwords

> HTTPS is essential for secure authorization online.

---

## 🔐 OAuth (Open Authorization)

### What Is OAuth?
**OAuth** is an open-standard **authorization protocol** that:
- Shares limited access between applications
- Avoids sharing usernames and passwords

---

### Common Example
You allow a website to:
- “Sign in with Google”

Instead of sharing your password:
- OAuth uses **API tokens**

---

## 🪙 API Tokens Explained
An **API token** is:
- A small encrypted block of code
- Used to verify authorization

API tokens may include:
- User identity
- Permissions
- Scope of access
- Expiration details

---

## 🔁 How OAuth Works (Simplified)
1. User authenticates with trusted provider
2. Provider issues API token
3. Token is sent to requesting application
4. Application gains **limited access**

📌 Password is never shared.

---

## 🛡️ Why OAuth Is Secure
OAuth:
- Limits access scope
- Reduces credential exposure
- Protects passwords during third-party breaches

Even if another platform is compromised:
- Your main account remains protected

---

## 🔐 OAuth + MFA
OAuth does **not** replace authentication security.

If MFA is enabled:
- MFA is still enforced
- OAuth inherits those protections

This creates **layered defense**.

---

## 🧠 SOC Scenario: Third-Party App Access
**Situation:**  
A third-party app is breached.

**Without OAuth:**  
- Passwords exposed

**With OAuth:**  
- Token access limited
- Password remains secure
- Access can be revoked instantly

---

## 🧠 Authorization Best Practices
Strong authorization systems:
- Follow least privilege
- Enforce separation of duties
- Use secure protocols (HTTPS, OAuth)
- Limit scope and duration of access
- Allow fast revocation

---

## 🎯 Key Takeaways

- Authorization determines what users can do
- It always follows authentication
- Least privilege limits access duration and scope
- Separation of duties prevents abuse
- HTTP basic auth is insecure
- HTTPS protects credentials in transit
- OAuth enables secure delegated access
- API tokens reduce password exposure
- SOC teams monitor authorization misuse closely

---

✍️ **Notes By Abhishek (Ez Abyss)**
