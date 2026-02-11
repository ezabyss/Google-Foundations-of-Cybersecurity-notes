# 🔁 Python Loops for Security Automation
---

## 🧠 Big Idea: Automation Needs Repetition

Earlier:
- Conditionals → allow decision-making
- Now → Loops allow repetition

A loop:
> Repeats a set of instructions automatically.

Why loops matter in security:
- Review thousands of log entries
- Scan hundreds of devices
- Process multiple alerts
- Retry failed connections
- Monitor login attempts

Humans get tired.
Computers don’t.

---

# 🔄 What Is an Iterative Statement?

An iterative statement:
> Code that repeatedly executes instructions.

Also called:
- Loop

Two main types:
- for loop → iterate over a sequence
- while loop → iterate while condition is True

---

# 🔁 FOR LOOPS (Sequence-Based Iteration)

Use a for loop when:
- You have a list
- You have a known number of repetitions
- You want to iterate through items

## Structure

    for variable in sequence:
        action

---

# 🧪 Example: Printing Usernames

    for user in ["abhishek", "ezabyss", "ravi", "ompra"]:
        print(user)

Loop variable: user  
Sequence: list of usernames  
Action: print(user)

SOC Equivalent:
- Loop through list of compromised accounts
- Notify each user

---

# 🖥️ Looping Through Assets (Real Security Example)

    computer_assets = ["laptop1", "desktop20", "smartphone03"]

    for asset in computer_assets:
        print(asset)

Real-world meaning:
- Scan each asset
- Apply compliance check
- Run vulnerability scan

One loop → all assets processed.

---

# 🔡 Looping Through Strings

Strings are sequences too.

    word = "security"

    for character in word:
        print(character)

Output:
s
e
c
u
r
i
t
y

Security use:
- Password validation
- Character filtering
- Pattern detection

---

# 🔢 Using range() with for Loops

range(start, stop, increment) 

Important:
- Start = included
- Stop = excluded
- Increment = By default 1
 
Example:

    for i in range(0, 5, 1):
        print(i)

Output:
0
1
2
3
4

5 is excluded.

---

## Default Behavior

    for i in range(5):
        print(i)

Same output:
0–4

Because:
- Default start = 0
- Default increment = 1

---

# 🚨 SOC Example: Retry Connection 10 Times

    for i in range(10):
        print("Cannot connect to destination")

Instead of writing:
print(...) ten times.

Automation efficiency.

---

# 🔄 WHILE LOOPS (Condition-Based Iteration)

Use while when:
- You don’t know exact number of repetitions
- Loop depends on condition

Structure:

    while condition:
        action

Loop continues as long as condition is True.

---

# 🧪 Example: Simple Counter

    i = 1

    while i < 5:
        print(i)
        i = i + 1

Important:
You must update the loop variable.
Otherwise → infinite loop.

Output:
1
2
3
4

---

# 🔐 Real SOC Example: Login Attempts

    login_attempts = 0

    while login_attempts < 5:
        print("Login attempt:", login_attempts)
        login_attempts = login_attempts + 1

Stops automatically when:
login_attempts reaches 5.

Used in:
- Brute-force protection
- Rate limiting
- Account lockout logic

---

# 🧠 Boolean-Based While Loop

    count = 0
    login_status = True

    while login_status == True:
        print("Try again.")
        count = count + 1

        if count == 4:
            login_status = False

Logic:
- Loop runs until login_status becomes False
- Boolean controls loop termination

Advanced automation pattern.

---

# 🛑 Controlling Loops

Sometimes you need more control.

Two powerful tools:
- break
- continue

---

# ⛔ break → Exit Loop Immediately

    computer_assets = ["laptop1", "desktop20", "smartphone03"]

    for asset in computer_assets:
        if asset == "desktop20":
            break
        print(asset)

Output:
laptop1

Loop stops when:
Condition is met.

Use case:
- Stop scanning once threat found
- Exit after detecting malware

---

# ⏭️ continue → Skip Current Iteration

    computer_assets = ["laptop1", "desktop20", "smartphone03"]

    for asset in computer_assets:
        if asset == "desktop20":
            continue
        print(asset)

Output:
laptop1
smartphone03

Difference:
- break → stops loop completely
- continue → skips only one iteration

---

# ⚠ Infinite Loops

If loop condition never becomes False:

    while True:
        print("Running...")

This runs forever.

Stop it using:
CTRL + C

Used intentionally in:
- Servers
- Continuous monitoring systems
- Real-time log processors

---

# 🧠 Mental Model

Conditionals = Decision logic  
Loops = Repetition logic  

Together:
They form automation engines.

Example:

    for user in user_list:
        if user_failed_attempts > 5:
            lock_account()

That’s detection + response.

---

# 🛡️ Cybersecurity Automation Use Cases

✔ Iterate through log entries  
✔ Check every device in asset inventory  
✔ Scan IP ranges  
✔ Retry API requests  
✔ Monitor login attempts  
✔ Process alert queues  

Without loops:
Manual effort explodes.

With loops:
Security scales.

---

# 🚀 Key Takeaways

✔ for → iterate over sequences  
✔ while → iterate while condition is True  
✔ range() generates number sequences  
✔ break exits loop  
✔ continue skips iteration  
✔ Always prevent infinite loops  

Master loops →
You move from scripting  
to real automation engineering.

---

**✍️ Notes By Abhishek (Ez Abyss)**
