# 🔐 Access Controls III: Accounting  
*Monitoring, Logging, and Detecting Security Events (AAA Framework – Part 3)*

---

## 🌍 Why Accounting Matters
Have you ever wondered if your employer tracks when you log into company systems?

If they follow security best practices, **they do**.

This function is called **accounting**, the third and final part of the:
- Authentication
- Authorization
- Accounting (AAA) framework

Accounting provides **visibility, accountability, and detection**.

---

## 📊 What Is Accounting?
**Accounting** is the practice of:
> Monitoring and reviewing system access logs

These logs record:
- Who accessed a system
- When access occurred
- What resources were used
- How long access lasted

---

## 🔍 Why Security Analysts Rely on Access Logs
Access logs are one of the **most important tools** for security analysts.

They are used to:
- Detect failed login trends
- Identify unauthorized access
- Investigate security incidents
- Confirm or deny data breaches

📌 In many investigations, **log analysis is the first step**.

---

## 🧠 SOC Scenario: Incident Investigation
**Situation:**  
SOC receives an alert about unusual activity.

**First Action:**  
Review access logs.

**Goal:**  
Determine:
- Who accessed the system
- What actions were performed
- Whether access was authorized

---

## 🌐 Sessions: The Foundation of Logging
Every time a user accesses a system, they initiate a **session**.

### Session
A **session** is:
- A sequence of requests and responses
- Associated with a single user and device
- Active from login until logout or timeout

Access logs are essentially **records of sessions**.

---

## 🆔 Session IDs
When a session starts, a **session ID** is created.

### Session ID:
- A unique identifier
- Ties the user and device to the session
- Exists until logout or session expiration

Session IDs allow systems to:
- Track activity
- Attribute actions to users

---

## 🍪 Session Cookies
At the start of a session, servers exchange **session cookies** with the user’s device.

### Session Cookie:
- A token stored in the browser
- Contains or references the session ID
- Helps determine session duration and permissions

Cookies allow websites to:
- Remember users
- Maintain state without resending credentials

---

## 🔐 Why Session Cookies Improve Security
Session cookies:
- Prevent repeated credential sharing
- Reduce exposure of usernames and passwords
- Make web interactions faster and safer

However, cookies are **not risk-free**.

---

## ⚠️ Session Hijacking
**Session hijacking** occurs when:
> An attacker steals a legitimate user’s session ID

With a stolen session cookie, attackers can:
- Impersonate the user
- Access sensitive data
- Perform unauthorized actions

---

## 🧠 SOC Scenario: Session Hijacking
**Situation:**  
SOC notices access from two locations using the same session ID.

**Finding:**  
Possible stolen session cookie.

**Action:**
- Terminate session
- Force re-authentication
- Investigate source of theft

---

## 🔁 SSO + Session Risk
Session hijacking is especially dangerous in **Single Sign-On (SSO)** environments.

If attackers hijack:
- One session
They may gain access to:
- Multiple systems

This makes **accounting and monitoring critical**.

---

## 📈 Detecting Threats with Access Logs
Access logs help detect:
- Impossible travel events
- Excessive login failures
- Unusual access times
- Unexpected resource usage

Patterns in logs often reveal:
- Compromised accounts
- Insider threats
- Active breaches

---

## 🛡️ Why Accounting Completes AAA
Accounting ensures:
- Visibility after access is granted
- Accountability for user actions
- Evidence during investigations

Without accounting:
- Authentication and authorization cannot be verified
- Incidents may go undetected

---

## 🧠 Accounting Best Practices
Effective accounting systems:
- Log all authentication attempts
- Track session creation and termination
- Monitor abnormal behavior
- Retain logs securely
- Support real-time alerts

---

## 🎯 Key Takeaways

- Accounting is the monitoring component of AAA
- Access logs record who, when, and what
- Logs are essential for incident response
- Sessions track user activity
- Session IDs uniquely identify users
- Session cookies enable secure interactions
- Session hijacking exploits stolen cookies
- SSO increases the impact of hijacking
- SOC teams depend heavily on log analysis

---

✍️ **Notes By Abhishek (Ez Abyss)**
