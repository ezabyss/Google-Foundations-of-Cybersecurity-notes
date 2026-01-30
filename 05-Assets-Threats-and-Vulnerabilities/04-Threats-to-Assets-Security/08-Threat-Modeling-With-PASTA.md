# 🧠 Threat Modeling with PASTA  

---

## 1️⃣ Scenario Overview: Fitness Mobile App

A **fitness company** is preparing to launch its **first mobile application**.  
Before going live, leadership asks the security team one critical question:

> “Will this app protect our customers’ data?”

To answer this, the security team performs **threat modeling** using the **PASTA framework**.

---

## 2️⃣ What Is PASTA?

**PASTA** stands for **Process for Attack Simulation and Threat Analysis**.

It is a **widely used threat modeling framework** designed to:
- Simulate real attacker behavior
- Identify vulnerabilities
- Analyze business risk
- Align security decisions with organizational goals

📌 PASTA is especially effective because it connects **technical threats** to **business impact**.

---

## 3️⃣ The 7 Stages of the PASTA Framework

---

### 🟢 Stage 1: Define Business & Security Objectives

Before any technical work begins, the team defines **what matters most**.

#### In our scenario:
- **Primary objective:** Protect customer data
- **Key questions asked:**
  - What customer data is collected?
  - How is personally identifiable information (PII) handled?
  - What would the impact of a data breach be?

🎯 This stage sets the foundation for evaluating risk later.

---

### 🟢 Stage 2: Define the Technical Scope

The team identifies **what technology must be evaluated**.

This includes the **attack surface** of the mobile app:
- Data at rest (databases)
- Data in use (application logic)
- Data in transit (network communication)
- APIs and backend services
- Security controls and protocols

📌 For a mobile app, both **client-side and server-side components** are in scope.

---

### 🟢 Stage 3: Decompose the Application

Here, the team breaks the application into **functional components**.

This is usually done by:
- Collaborating with developers
- Creating a **data flow diagram (DFD)**

The diagram shows:
- How data flows from the user’s device
- How it travels through the network
- Where it is stored in databases
- What security controls protect it at each step

🎯 Goal: Understand **how and where data could be exposed**.

---

### 🟢 Stage 4: Perform Threat Analysis

Now the team switches into an **attacker mindset**.

They research:
- Common mobile application attacks
- Current threat trends
- Known attack vectors against similar apps

Examples include:
- SQL injection
- Insecure authentication
- API abuse
- Credential theft

📌 Threat intelligence sources are critical here because attack techniques evolve rapidly.

---

### 🟢 Stage 5: Perform Vulnerability Analysis

At this stage, the team investigates **why threats could succeed**.

They look for:
- Weak input validation
- Misconfigured databases
- Insecure API endpoints
- Missing encryption
- Poor authentication controls

🎯 Focus: Identify the **root causes** of vulnerabilities, not just symptoms.

---

### 🟢 Stage 6: Conduct Attack Modeling

This is where threats are **tested conceptually**.

The team:
- Builds **attack trees** (flowchart-style diagrams)
- Simulates how attacks could occur

#### Example attack tree branch:
- **Target:** Customer credentials (username & password)
- **Asset location:** Database
- **Attack vector:** SQL injection
- **Root cause:** Unsanitized user input
- **Threat actor action:** Inject malicious SQL through a login form

📌 Each branch represents a different possible attack path.

---

### 🟢 Stage 7: Analyze Risk & Impact

Finally, the team brings everything together.

They:
- Review findings from stages 1–6
- Assess likelihood and impact
- Prioritize risks
- Make security recommendations

🎯 Outcome:
Actionable **risk management decisions** that align with business goals.

These recommendations are shared with **business stakeholders**, not just technical teams.

---

## 4️⃣ SOC & Business Value of PASTA

For SOC and security teams, PASTA helps:
- Anticipate real-world attack paths
- Improve detection and prevention strategies
- Justify security investments using business impact
- Reduce surprise incidents after launch

PASTA ensures security is **planned**, not patched later.

---

## 🔑 Key Takeaways

- PASTA is a 7-stage, risk-driven threat modeling framework
- It connects attacker behavior to business impact
- Attack trees help visualize how real attacks occur
- Collaboration with developers is essential
- The final goal is informed, business-aligned risk decisions

---

**✍️ Notes By Abhishek (Ez Abyss)**
