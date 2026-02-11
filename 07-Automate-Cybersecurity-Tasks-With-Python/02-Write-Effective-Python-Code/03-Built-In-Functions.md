# 🧰 Python Built-in Functions for Security Automation

---

# 🧠 Big Idea

Built-in functions are:
→ Pre-written tools inside Python  
→ Ready to use immediately  
→ Designed to reduce repetitive work  

You don’t build them.
You just call them.

Think of them like built-in security tools in a SIEM:
- You don’t build the parser
- You configure and use it

Same with Python.

---

# 🔹 1. print() — Output Data

print() displays objects to the screen.

It accepts:
✔ Any data type  
✔ Multiple arguments  
✔ Mixed data types  

Example:

    month = "September"
    print("Investigate failed login attempts during", month, "if more than", 100)

Output:
Investigate failed login attempts during September if more than 100

🔎 Security Use Case:
- Display alert summaries
- Print investigation results
- Debug scripts

---

# 🔹 2. type() — Identify Data Type

type() returns the data type of an object.

It:
✔ Accepts only one argument  
✔ Returns a data type object  

Example:

    print(type("security"))
    print(type(73.2))

Output:
<class 'str'>
<class 'float'>

🔎 Why This Matters in Security:
- Prevents type errors
- Validates log field types
- Ensures numeric comparisons work properly

---

# 🔁 Passing One Function Into Another

Python evaluates inside-out.

Example:

    print(type("Hello"))

Process:
1. type("Hello") → returns str
2. print(str) → prints it

This pattern is common in automation pipelines.

Think:
Data → Process → Output

---

# 🔹 3. max() — Largest Value

max() returns the largest numeric input.

Example:

    a = 3
    b = 9
    c = 6
    print(max(a, b, c))

Output:
9

It also works with lists:

    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(max(time_list))

🔎 Security Use Case:
- Longest login session
- Highest failed attempt count
- Peak traffic value

---

# 🔹 4. min() — Smallest Value

min() returns the smallest numeric value.

    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(min(time_list))

Output:
2

🔎 Security Use Case:
- Shortest login session
- Lowest latency
- Minimum response time

---

# 🔹 5. sorted() — Sort Data

sorted() sorts an iterable (like a list or string).

By default:
→ Ascending order

Example:

    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(sorted(time_list))

Output:
[2, 12, 14, 19, 22, 32, 57]

---

# 🔍 Important: sorted() Does NOT Modify Original List

    time_list = [12, 2, 32, 19, 57, 22, 14]
    print(sorted(time_list))
    print(time_list)

Output:
[2, 12, 14, 19, 22, 32, 57]
[12, 2, 32, 19, 57, 22, 14]

Original list remains unchanged.

---

# 🔤 Sorting Strings Alphabetically

    usernames = ["zcarter", "akhan", "mlopez"]
    print(sorted(usernames))

Output:
['akhan', 'mlopez', 'zcarter']

🔎 Security Use Case:
- Sort usernames alphabetically
- Sort IP addresses
- Organize assets

---

# ⚠ sorted() Limitation

Cannot mix data types:

❌ Invalid:

    sorted([1, 2, "hello"])

Python will raise a type error.

Why?
Because it cannot compare integers and strings.

---

# 🧠 Understanding Inputs & Outputs

Before using a function, ask:

1. How many parameters does it accept?
2. What data types does it accept?
3. What data type does it return?

Example Summary:

| Function | Input | Output |
|----------|-------|--------|
| print()  | Any type, multiple | None (prints) |
| type()   | One argument | Data type |
| max()    | Numbers or iterable | Largest value |
| min()    | Numbers or iterable | Smallest value |
| sorted() | Iterable | New sorted list |

---

# 🔐 Real Cybersecurity Scenario Example

Suppose you are analyzing login durations:

    session_times = [12, 4, 67, 32, 9]

    print("Shortest session:", min(session_times))
    print("Longest session:", max(session_times))
    print("Sorted sessions:", sorted(session_times))

This helps:
✔ Detect anomalies
✔ Identify abnormal long sessions
✔ Investigate outliers

---

# 🏗 Built-in Functions Improve Automation

Instead of writing:

- Manual comparison logic
- Custom sorting algorithms
- Lengthy value scanning code

You call one function.

Efficiency ↑  
Code length ↓  
Error rate ↓  

---

# 🏆 Key Takeaways

✔ Built-in functions already exist in Python  
✔ They reduce complexity  
✔ Functions can be nested (inside-out execution)  
✔ Always understand required parameters  
✔ Always understand return type  
✔ sorted() does not modify original list  
✔ min() and max() work on iterables  

Mastering built-in functions →
Makes your scripts shorter, safer, and more professional.

---

**✍️ Notes By Abhishek (Ez Abyss)**
