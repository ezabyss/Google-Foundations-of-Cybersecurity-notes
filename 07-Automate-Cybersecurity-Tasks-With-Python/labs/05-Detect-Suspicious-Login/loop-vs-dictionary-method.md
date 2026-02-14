## 🧠 Loop vs Dictionary Approach (Failure Counting)

Two methods were used to detect suspicious login attempts:

### 1️⃣ Loop Method
- Scans the entire log each time
- Counts failures for the current user
- Simple and easy to understand
- Slower for large datasets

### 2️⃣ Dictionary Method
- Scans the log once
- Stores results as: `username → failure count`
- Allows instant lookups
- Faster and scalable for real-world systems

### ⚡ Key Difference

- Loop = count every time  
- Dictionary = count once, reuse many times  

The dictionary approach is more efficient and better suited for SOC-level automation.

---

**✍️ Notes By Abhishek (Ez Abyss)**
