# Understand Attackers and Attack Types
_Notes by Abhishek (EzAbyss)_

---

## 1. Overview

A **threat actor** = any individual or group that poses a security risk.  
They differ by **motivation**, **skills**, and **intentions**.

Understanding them helps security professionals predict attacks, respond quickly, and protect organizations effectively.

---

# PART 1: THREAT ACTOR TYPES

---

## 2. Advanced Persistent Threats (APTs)

**Definition:**  
Highly skilled, well-funded groups that gain unauthorized access and stay hidden for long periods.

**Target:**  
Large corporations, governments, critical systems.

**Motivations:**

- Damage critical infrastructure (power grid, telecom, natural resources)
- Steal intellectual property (trade secrets, patents)
- Espionage and long-term intelligence gathering

**Remember:**  
APTs = **Stealthy + Patient + Highly Skilled**

---

## 3. Insider Threats

Individuals inside the organization who misuse their **authorized access**.

**Motivations:**

- Sabotage  
- Corruption  
- Espionage  
- Unauthorized data leaks  

**Examples:**  
- Employee steals confidential files  
- Admin grants unauthorized access  
- Contractor misuses credentials  

**Remember:**  
Insiders are dangerous because they already have **legitimate access**.

---

## 4. Hacktivists

Threat actors driven by **political or social agendas**.

**Goals:**

- Online demonstrations  
- Propaganda  
- Social change campaigns  
- Gaining fame or attention  

**Example:**  
A group defaces a government website to protest a policy.

**Remember:**  
Hacktivists = **Activists + Hacking**  

---

# PART 2: HACKER TYPES

---

## 5. Three Main Hacker Categories

### 5.1 Authorized Hackers (Ethical Hackers)
- Work with permission  
- Follow laws and ethics  
- Conduct penetration tests, risk evaluations  
- Goal: **Protect and defend**

### 5.2 Semi-Authorized Hackers (Researchers)
- Find vulnerabilities  
- Do **not exploit** what they discover  
- Often report weaknesses responsibly  

### 5.3 Unauthorized Hackers (Unethical Hackers)
- Malicious intent  
- Break laws  
- Steal and sell confidential data  
- Goal: **Financial gain or destruction**

---

## 6. Other Hacker Variants

### New/Unskilled Hackers ("Script Kiddies")
Motivations:
- Learn hacking  
- Revenge  
- Use existing tools/malware without advanced skills  

### Contract Hackers
- Work **for pay**
- Can be hired for legal or illegal tasks  
- Ethics depend on the job  

### Vigilante Hackers
- Self-assigned “protectors”  
- Try to stop unethical hackers  
- Actions may still be illegal  

---

## ⭐ Key Insight: Threat Actors vs Hackers

| Threat Actor | Hacker |
|--------------|--------|
| Defined by **intent** | Defined by **technical skill** |
| Motivations = political, financial, ideological | Motivations = legal research, illegal access, curiosity |
| Can be groups or individuals | Usually individuals |

---

# PART 3: ATTACK TYPES

---

## 7. Password Attacks  
_Attempt to access password-protected systems._  
Falls under: **Communication & Network Security domain**

Examples:
- **Brute Force Attack** (try all combinations)
- **Rainbow Table Attack** (use precomputed hash lists)

**Goal:**  
Break authentication to gain access.

---

## 8. Social Engineering Attacks  
_Manipulating humans to reveal information by exploiting trust or error._  
Falls under: **Security & Risk Management domain**

Common types:

- **Phishing** (email)
- **Smishing** (SMS)
- **Vishing** (voice calls)
- **Spear Phishing** (targeted)
- **Whaling** (targets executives)
- **Social media phishing**
- **Business Email Compromise (BEC)**
- **Watering Hole attacks** (infect websites users visit)
- **USB baiting**
- **Physical social engineering** (tailgating, impersonation)

**Remember:**  
Social engineering targets **people**, not systems.

---

## 9. Physical Attacks  
_Affect both digital and physical environments._  
Falls under: **Asset Security domain**

Examples:

- Malicious USB/fake chargers  
- Tampered flash drives  
- Card cloning  
- Skimming devices  

---

## 10. Adversarial Artificial Intelligence  
_Techniques that manipulate AI/ML systems to cause incorrect outputs._  
Falls under:  
- Communication & Network Security  
- Identity and Access Management (IAM)

Examples:
- Fooling facial recognition  
- Poisoning ML models  
- Manipulated training data  

---

## 11. Supply-Chain Attacks  
_Attacking vendors or third-party systems to compromise many organizations._

Examples:
- Malware injected during software updates  
- Hardware tampering during manufacturing  

Falls under multiple domains:
- Security & Risk Management  
- Security Architecture & Engineering  
- Security Operations  

**Danger:**  
One attack → Many victims.

---

## 12. Cryptographic Attacks  
_Attacks targeting encryption or secure communications._  
Falls under: **Communication & Network Security domain**

Examples:
- **Birthday attack** (hash collisions)
- **Collision attack** (same hash, different data)
- **Downgrade attack** (force weak encryption)

---

# ⭐ Key Takeaways (Memory Booster)

- **Threat actors = motivations & intent**  
- **Hackers = skills & legality**  
- APTs = long-term, expert attackers  
- Insider threats = biggest internal danger  
- Hacktivists = political motives  
- Attacks fall under specific CISSP domains  
- Social engineering → exploits humans  
- Supply-chain attacks → widespread impact  
- Cryptographic attacks → break secure communication  

---
