# 📚 Python Libraries, Modules & PEP 8

---

# 🧠 Big Picture

Built-in functions = tools already inside Python  
Modules = Python files containing extra tools  
Libraries = Collections of modules  

Think like security tools:

- Built-in → Basic OS utilities
- Standard Library → Pre-installed enterprise tools
- External Libraries → Third-party security tools you install

Python gives you layers of power.

---

# 🗂 What Is a Module?

A module is:
→ A Python file  
→ Contains functions, variables, classes  
→ Reusable code  

Example modules from Python Standard Library:

- re → pattern searching (log analysis)
- csv → work with CSV files
- os → interact with operating system
- glob → file pattern matching
- time → time-related operations
- datetime → timestamps
- statistics → numeric calculations

🔐 Security Connection:
- Parse logs
- Analyze failed login attempts
- Extract patterns from network data
- Work with system files

---

# 📦 What Is a Library?

A library is:
→ A collection of modules  
→ Designed for specific tasks  

Example:
Python Standard Library = built-in collection of modules

External libraries:
- BeautifulSoup → HTML parsing
- numpy → numerical analysis
- pandas → data analysis

Libraries save:
✔ Development time  
✔ Repetitive coding  
✔ Complexity  

---

# 🏗 Importing Modules (Standard Library)

## 🔹 Import Entire Module

    import statistics

Then use:

    statistics.mean(data)

Example:

    import statistics

    monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]

    mean_failed_attempts = statistics.mean(monthly_failed_attempts)
    print("mean:", mean_failed_attempts)

Output:
mean: 35.25

🔎 Notice:
You must prefix with module name → statistics.mean()

---

## 🔹 Import Specific Functions

Instead of importing entire module:

    from statistics import mean, median

Now you can write:

    mean(monthly_failed_attempts)
    median(monthly_failed_attempts)

Full Example:

    from statistics import mean, median

    monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]

    print("mean:", mean(monthly_failed_attempts))
    print("median:", median(monthly_failed_attempts))

✔ Cleaner  
✔ Shorter  
✔ More readable  

---

# 🔍 Real-World Cybersecurity Scenario

Imagine analyzing failed login attempts:

- One month has 178 attempts (outlier)
- Others are normal range

Use:
- mean() → overall average
- median() → typical behavior

Why median matters:
It reduces impact of extreme anomalies.

This is basic anomaly detection thinking.

---

# 🌐 Installing External Libraries

Standard Library → Already installed  
External Library → Must install first  

Example:

    %pip install numpy

Then import:

    import numpy

External libraries are powerful for:
- Network packet analysis
- Log parsing
- Statistical anomaly detection
- Machine learning

---

# 🎯 Import Strategy Summary

| Method | Syntax | When to Use |
|--------|--------|-------------|
| Entire module | import statistics | When using many functions |
| Specific functions | from statistics import mean | When using few functions |

---

# ✨ Code Readability & PEP 8

Clean code = professional code  
Readable code = scalable code  

Python follows PEP 8 style guide.

PEP = Python Enhancement Proposal  
PEP 8 = Style guidelines for Python

Not mandatory — but industry standard.

---

# 📝 Comments (PEP 8 Guidance)

A comment explains:
- What the code does
- Why it exists

Example without comment:

    failed_attempts = 6
    if failed_attempts > 5:
        print("Account locked")

Example with comment:

    # Lock account if failed login attempts exceed 5
    failed_attempts = 6
    if failed_attempts > 5:
        print("Account locked")

✔ Clear intent  
✔ Easier debugging  
✔ Team-friendly  

---

# 📏 Indentation (Critical in Python)

Indentation:
→ Spaces at start of line  
→ Defines code structure  

PEP 8 recommends:
→ 4 spaces per indent

Example:

    if status == 200:
        print("OK")

If not indented:

    if status == 200:
    print("OK")

❌ This causes error.

Indentation:
- Groups logic
- Prevents accidental execution
- Controls flow

---

# 🏢 Real Industry Lesson

Without style guide:
- Code becomes messy
- Hard to scale
- Hard to maintain
- Hard for teams to collaborate

In security teams:
- Scripts evolve
- Tools expand
- Analysts change roles

Clean style ensures:
✔ Future maintainability
✔ Professional credibility
✔ Reduced technical debt

---

# 🔐 Security Professional Mindset

When writing Python for security:

✔ Use modules instead of reinventing logic  
✔ Follow PEP 8 for team compatibility  
✔ Comment clearly  
✔ Use 4-space indentation  
✔ Keep imports organized  
✔ Avoid unnecessary global variables  

---

# 🏆 Key Takeaways

✔ Module = Python file with reusable code  
✔ Library = Collection of modules  
✔ Standard Library comes with Python  
✔ External libraries require installation  
✔ Use import or from ... import  
✔ statistics.mean() vs mean() difference  
✔ Follow PEP 8 for clean code  
✔ Indentation is not optional in Python  

Mastering modules + clean style →
Makes your automation scripts professional and scalable.

---

**✍️ Notes By Abhishek (Ez Abyss)**
