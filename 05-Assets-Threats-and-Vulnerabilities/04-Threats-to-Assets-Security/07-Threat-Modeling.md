# 🛡️ Threat Modeling: Preparing for Attacks  

---

## 1️⃣ Why Threat Modeling Matters

Preparing for attacks is a **shared responsibility across the entire security team**.  
Threat actors adapt their tools and techniques based on the **type of target**:

- A **small business** may face phishing, ransomware, or basic web attacks  
- A **public utility** may face nation-state actors, sabotage, or critical infrastructure threats  

💡 **Key idea:**  
Security is not reactive. The strongest defenses come from **anticipating attacks before they happen**.

This anticipation process is called **threat modeling**.

---

## 2️⃣ What Is Threat Modeling?

**Threat modeling** is the process of:
- Identifying **assets**
- Understanding their **vulnerabilities**
- Determining how they are **exposed to threats**

Threat modeling can be applied to:
- Entire systems
- Applications
- Networks
- Business processes

⚠️ It is considered an **advanced security skill** because it requires:
- Experience
- Collaboration
- Deep understanding of systems and attackers

However, **SOC analysts are often involved**, especially during analysis, detection, and validation phases.

---

## 3️⃣ Who Performs Threat Modeling?

Threat models are usually created by:
- Security engineers
- SOC analysts
- Developers
- System architects
- Risk and compliance teams

🧠 This collaborative approach ensures:
- Technical accuracy
- Business relevance
- Realistic threat assumptions

---

## 4️⃣ The Six Core Steps of Threat Modeling

---

### 🟢 Step 1: Define the Scope

The team decides **what is being protected**.

This includes:
- Creating an inventory of assets
- Classifying assets by importance and sensitivity

📌 Examples of assets:
- Databases
- Applications
- Servers
- Customer data
- Business processes

---

### 🟢 Step 2: Identify Threats

The team identifies all **potential threat actors**.

A **threat actor** is any person or group that presents a security risk.

#### Threat actor types:
- **Internal**: Employees, contractors, insiders  
- **External**: Hackers, competitors, cybercriminal groups

After identifying threat actors, the team creates an **attack tree**.

🧩 **Attack tree**:
- A diagram that maps threats to assets
- Shows possible attack paths
- Built with as much detail as possible

---

### 🟢 Step 3: Characterize the Environment

The team applies an **attacker mindset** to the organization.

They examine:
- How employees use systems
- How customers interact with applications
- Third-party vendors and external partners
- Trust relationships between systems

🎯 Goal: Identify weak points attackers could exploit.

---

### 🟢 Step 4: Analyze Threats

At this stage, the team:
- Reviews existing security controls
- Identifies gaps in protection
- Assigns **risk scores** to threats

Threats are ranked based on:
- Likelihood
- Impact
- Exploitability

📊 This helps prioritize what needs immediate attention.

---

### 🟢 Step 5: Mitigate Risk

The team decides how to handle each identified risk.

Risk response options:
- **Avoid** the risk (change design or remove asset)
- **Transfer** the risk (insurance, third-party responsibility)
- **Reduce** the risk (add controls and defenses)
- **Accept** the risk (acknowledge and monitor)

This step results in a **defensive action plan**.

---

### 🟢 Step 6: Evaluate Findings

Everything from the exercise is:
- Documented
- Reviewed
- Applied where necessary

The team records:
- Fixes implemented
- Successful controls
- Lessons learned

📌 These lessons improve **future threat models** and security maturity.

---

## 5️⃣ SOC Relevance (Real-World View)

For SOC teams, threat modeling helps:
- Predict likely attack paths
- Tune detection rules
- Improve alert prioritization
- Understand attacker behavior

Threat models directly influence:
- SIEM use cases
- Incident response playbooks
- Risk-based alerting

---

## 🔑 Key Takeaways

- Threat modeling is proactive security planning
- It identifies assets, vulnerabilities, and threats
- The process has six structured steps
- Attack trees help visualize attacker paths
- Risk decisions guide defensive strategy
- Lessons learned strengthen future security efforts

---

**✍️ Notes By Abhishek (Ez Abyss)**
