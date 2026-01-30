# 💉 SQL Injection Attacks & Prevention  
**Web-Based Exploits**

---

## 1️⃣ Why SQL Injection Still Matters

Most web applications rely on **databases**.  
Actions like logging in, searching, or adding items to a cart silently trigger **SQL queries** in the background.

⚠️ If user input is not handled safely, attackers can **inject malicious SQL code** and manipulate databases.

---

## 2️⃣ SQL Refresher (Backend Reality)

### What is SQL?
**Structured Query Language (SQL)** is used to:
- Retrieve data (`SELECT`)
- Insert data (`INSERT`)
- Modify data (`UPDATE`)
- Delete data (`DELETE`)

### Real-world example
An online clothing store database may store:
- Product inventory
- User accounts
- Orders and payment references

Clicking **“Add to Cart”** triggers a SQL query behind the scenes—without the user ever seeing it.

---

## 3️⃣ What Is SQL Injection?

**SQL injection** is an attack that executes **unexpected SQL queries** on a database due to unsanitized user input.

### Why it happens
Developers often assume users will enter valid input.  
Attackers exploit this assumption by injecting additional SQL code.

---

## 4️⃣ Common SQL Injection Entry Points

SQL injection usually occurs in **input fields**, such as:
- Login forms
- Search bars
- Comment sections
- URL parameters

📌 Vulnerable logic:
User input → directly appended to SQL query → database executes blindly

---

## 5️⃣ Real SOC Scenario

### Retail Website Breach
- Attacker injects malicious input into a product search field
- Backend executes unintended SQL queries
- Database leaks customer emails and password hashes

**SOC indicators:**
- Abnormally long or malformed inputs
- Repeated database errors
- Unusual query execution patterns

**Impact:** Data breach, compliance violations, reputational damage

---

## 6️⃣ SQL Injection Categories

### 🟢 In-Band SQL Injection (Most Common)
- Same channel used to launch the attack and receive results
- Example: Malicious search input returns sensitive data on the same page

SOC Tip: Watch for abnormal responses in normal UI elements.

---

### 🔵 Out-of-Band SQL Injection (Rare)
- Uses a different communication channel to extract data
- Example: Database connects to an attacker-controlled server

SOC Tip: Monitor unexpected outbound connections from database servers.

---

### 🟡 Inferential (Blind) SQL Injection
- No direct data returned
- Attacker infers database structure from errors or response timing

SOC Tip: Detect repetitive requests that trigger subtle behavior changes.

---

## 7️⃣ Why SQL Injection Is So Common

- SQL is widely used
- Developers prioritize functionality over security
- Weak or missing input validation
- Legacy systems lack modern protections

---

## 8️⃣ Preventing SQL Injection

### ✅ Prepared Statements (Best Defense)
- SQL logic executes **before** user input is applied
- Input is treated strictly as data, not executable code

---

### ✅ Input Sanitization
- Removes or escapes suspicious characters
- Filters SQL keywords and symbols

---

### ✅ Input Validation
- Ensures input matches expected formats
- Example: Email must follow `name@domain.com`

---

### 🔐 Best Practice
Use **all three together**:
- Prepared statements  
- Input sanitization  
- Input validation  

---

## 9️⃣ SOC & Developer Collaboration

SQL injection prevention is a **shared responsibility**.

**SOC teams:**
- Monitor logs and alerts
- Detect abnormal queries
- Identify attack patterns

**Developers:**
- Fix vulnerable code
- Implement secure query handling
- Apply security testing

---

## 🔑 Key Takeaways

- SQL injection exploits unsanitized user input
- Attacks can steal, modify, or destroy data
- Three types: In-band, Out-of-band, Inferential
- Prepared statements are the strongest defense
- Collaboration is essential for prevention

---

**✍️ Notes By Abhishek (Ez Abyss)**
