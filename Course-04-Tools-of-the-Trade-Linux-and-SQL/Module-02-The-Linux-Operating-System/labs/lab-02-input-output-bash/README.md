# Lab 02: Examine Input and Output in the Bash Shell


## Activity Overview
This lab explores how the Bash shell handles **input and output** when communicating with the Linux operating system. 
Commands entered into the shell act as input, and the shell responds with output or error messages.
In this activity, basic shell commands are used to demonstrate how users interact with the operating system. 

---

## Scenario
In this scenario, you are required to:
- Generate output using the `echo` command
- Perform basic mathematical calculations using the `expr` command
- Clear the shell interface using the `clear` command
- Interpret how the shell responds to user input

These tasks simulate real-world situations where analysts must quickly process command output and system responses.

---

## Commands Used

### echo
The `echo` command outputs a specified string of text to the shell. It is commonly used to display messages, variables, or command results.

---

### expr
The `expr` command evaluates expressions and performs basic integer arithmetic. It supports addition, subtraction, multiplication, and division when operators and operands are separated by spaces.

---

### clear
The `clear` command clears all existing output from the shell window, providing a clean workspace for continued tasks.

---

## Tasks Performed

### Task 1: Generate Output with `echo`

```bash
echo hello
```

### Task 2: Generate Output with `expr`
```
expr 32 - 8
```

### Calculate yearly login attempts
```
expr 3500 \* 12
```
### Expected output:
```42000```
> Note: The multiplication operator * is escaped using \* to prevent shell interpretation.

