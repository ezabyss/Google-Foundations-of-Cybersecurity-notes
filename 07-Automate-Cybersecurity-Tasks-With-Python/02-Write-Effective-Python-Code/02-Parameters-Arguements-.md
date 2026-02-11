# 🔁 Python Functions — Parameters, Returns & Variable Scope

---

# 🧠 Big Picture

So far we’ve learned:
- Variables store data
- Conditionals make decisions
- Loops repeat actions
- Functions package reusable logic

Now we upgrade functions with:
✔ Parameters (input into function)  
✔ Arguments (actual values passed in)  
✔ Return statements (send data back out)  
✔ Global vs Local variables (scope control)  

These are foundational for writing real cybersecurity automation scripts.

---

# 🧩 Parameters vs Arguments (Clear Distinction)

🔹 Parameter  
A variable defined inside the function header.

🔹 Argument  
The actual value passed into the function when it is called.

Example:

    def greet_employee(name):
        print("Welcome,", name)

    greet_employee("Abhishek Hamal")

Here:
- name → parameter
- "Abhishek Hamal" → argument

---

# 🏗 Function with One Parameter

    def greet_employee(name):
        print("You're logged in,", name)

    greet_employee("Abhishek Hamal")

Output:
You're logged in, Abhishek Hamal

Notice:
- name is NOT in quotation marks inside print
- It’s a variable

---

# 🏗 Function with Multiple Parameters

    def greet_employee(first_name, last_name):
        print("You're logged in,", first_name, last_name)

    greet_employee("Abhishek", "Hamal")

Output:
You're logged in, Abhishek Hamal

Multiple parameters:
- Separated by commas
- Arguments must match order

Order matters.

---

# 🛡 Real Security Example: Remaining Login Attempts

    def remaining_login_attempts(maximum_attempts, total_attempts):
        print(maximum_attempts - total_attempts)

    remaining_login_attempts(3, 2)

Output:
1

This is basic — but not reusable in automation.

Why?

Because it only prints.
It does not return data.

---

# 🔁 Return Statements (Sending Data Back)

A return statement:
> Sends data from inside a function back to the caller.

Important:
- return is NOT a function
- No parentheses after return
- Code stops executing after return

Example:

    def remaining_login_attempts(maximum_attempts, total_attempts):
        return maximum_attempts - total_attempts

    remaining_attempts = remaining_login_attempts(3, 3)

    if remaining_attempts <= 0:
        print("Your account is locked")

Output:
Your account is locked

This is real automation logic.

---

# 🧮 Advanced Example: Failed Login Percentage

Security Scenario:
Lock account if failed login rate ≥ 50%

    def calculate_fails(total_attempts, failed_attempts):
        fail_percentage = failed_attempts / total_attempts
        return fail_percentage

    percentage = calculate_fails(4, 2)

    if percentage >= 0.5:
        print("Account locked")

Output:
Account locked

Why this matters:
- Function computes
- Program decides

This is modular security logic.

---

# 🌍 Global vs Local Variables (CRITICAL CONCEPT)

🔹 Global Variable  
Defined outside functions.
Accessible everywhere.

🔹 Local Variable  
Defined inside a function.
Exists only while function runs.

---

# 🔹 Global Variable Example

    device_id = "7ad2130bd"

    def identify_device():
        print(device_id)

    identify_device()

Output:
7ad2130bd

Function accessed global variable.

But this is NOT best practice.

---

# 🔹 Local Variable Example

    def greet_employee(name):
        total_string = "Welcome " + name
        return total_string

Here:
- name → local (parameter)
- total_string → local
- Both destroyed after function ends

Using total_string outside function → ERROR

---

# ⚠ Variable Name Conflict Example

    username = "elarson"
    print("1:" + username)

    def greet():
        username = "bmoreno"
        print("2:" + username)

    greet()
    print("3:" + username)

Output:
1:elarson
2:bmoreno
3:elarson

Why?

Because:
- Inside function → local username
- Outside function → global username

They are separate.

This is called variable shadowing.

---

# 🛑 Why Mixing Global & Local Variables Is Dangerous

Problems:
- Confusion
- Debugging difficulty
- Unexpected behavior
- Security logic errors

Best practice:
✔ Pass values using parameters  
✔ Return results explicitly  
✔ Avoid modifying global variables inside functions  

Professional rule:
Functions should not depend on hidden global state.

---

# 🧠 Mental Model Upgrade

Function Flow:

Input → Process → Return → Decision

Example Security Flow:

```
Log Data  
↓  
calculate_failed_percentage()  
↓  
return percentage  
↓  
if percentage >= threshold  
↓  
Lock Account  

```
This is automation architecture.


---

# 🏆 Key Takeaways

✔ Parameter = variable in function header  
✔ Argument = value passed during function call  
✔ return sends data back to caller  
✔ return ends function execution  
✔ Global variables exist everywhere  
✔ Local variables exist only inside functions  
✔ Avoid reusing same variable names globally and locally  
✔ Prefer parameters over globals  

Mastering this →
You move from writing scripts  
to engineering automation logic.

---

**✍️ Notes By Abhishek (Ez Abyss)**
