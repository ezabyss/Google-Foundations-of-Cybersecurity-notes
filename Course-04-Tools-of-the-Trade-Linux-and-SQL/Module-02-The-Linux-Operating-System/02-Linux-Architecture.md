# 🏗️ Linux Architecture

### *Components of Linux & How They Work Together*

---

## 🎯 Big Picture

Just like a **building** is designed with different structural parts, **Linux** is built using multiple components that work together to form a complete operating system.

> Understanding Linux architecture helps security analysts understand **how tasks flow**, **where problems occur**, and **where attacks may happen**.

---

## 🔄 Linux Architecture Flow 

A task in Linux flows through the system in this order:

**User → Applications → Shell → Filesystem Hierarchy Standard (FHS) → Kernel → Hardware**

Keep this flow in mind — it’s essential for troubleshooting and security analysis.

---

## 👤 1. User

### 📌 Definition

The **user** is the person interacting with the Linux system.

* Users initiate tasks and commands
* Linux is a **multi‑user system**

🧠 **Security insight:**

> Multiple users can share system resources at the same time, which makes access control and permissions very important.

---

## 📦 2. Applications

### 📌 Definition

An **application** is a program that performs a specific task.

Examples:

* Text editors (Nano)
* Calculators
* Web browsers

In Linux, applications are often installed using a **package manager**.

### 📌 Package Manager

A **package manager**:

* Installs applications
* Updates software
* Removes unused programs

🧠 Applications and programs are often used interchangeably.

---

## ⌨️ 3. Shell

### 📌 Definition

The **shell** is the **command‑line interpreter**.

It:

* Accepts text‑based commands
* Translates them for the kernel
* Displays output to the user

🧠 You can think of the shell as a **translator** between the user and the system.

---

## 🗂️ 4. Filesystem Hierarchy Standard (FHS)

### 📌 Definition

The **Filesystem Hierarchy Standard (FHS)** defines how data is **organized and stored** in Linux.

Think of the FHS as a **filing cabinet**:

* Files are stored in specific locations
* Directories (folders) organize files

---

### 📁 Directories

* A **directory** is a file that stores other files or directories
* Directories help the OS know where to find data

🧠 **Security insight:**

> Knowing where files live helps analysts locate logs, configs, and sensitive data.

---

## 🧠 5. Kernel

### 📌 Definition

The **kernel** is the **core** of the Linux operating system.

The kernel:

* Manages processes
* Manages memory
* Communicates with hardware
* Uses drivers to control devices

---

### 🔐 Why the Kernel Matters

* Controls resource allocation
* Improves system performance
* Ensures commands are executed efficiently

🧠 The Linux kernel is unique and critical to system security.

---

## 🖥️ 6. Hardware

### 📌 Definition

**Hardware** refers to the physical components of a computer.

Examples:

* CPU
* RAM
* Hard drives
* Keyboard and mouse

Hardware is divided into **peripheral** and **internal** components.

---

## 🖱️ Peripheral Hardware

Peripheral devices:

* Are attached to the computer
* Are not required for the system to run
* Can be added or removed easily

Examples:

* Monitor
* Printer
* Keyboard
* Mouse

---

## 🧩 Internal Hardware

Internal hardware is required for the computer to function.

### 🔹 Central Processing Unit (CPU)

* Main processor of the computer
* Executes instructions from programs

---

### 🔹 Random Access Memory (RAM)

* Short‑term memory
* Stores data temporarily while programs run
* Data is erased when the system powers off

---

### 🔹 Hard Drive

* Long‑term storage
* Stores files and programs
* Data persists after shutdown
* Systems can have multiple hard drives

---

## 🔐 Why Linux Architecture Matters for Security Analysts

Understanding Linux architecture helps analysts:

* Trace how commands are executed
* Investigate system issues
* Identify misconfigurations
* Understand attack paths

> Strong security begins with understanding system structure.

---

## 🧠 Summary

* Linux architecture is layered
* Tasks flow from user → hardware
* The shell enables user interaction
* The kernel controls system resources
* FHS organizes data
* Hardware executes instructions

---

## 📝 One‑Line 

> *Linux architecture consists of the user, applications, shell, Filesystem Hierarchy Standard, kernel, and hardware, all working together to execute tasks efficiently and securely.*

---

✨ *Understanding Linux architecture makes security analysis clearer and more effective.*

---
**✍️Notes by Abhishek (Ez Abyss)**
