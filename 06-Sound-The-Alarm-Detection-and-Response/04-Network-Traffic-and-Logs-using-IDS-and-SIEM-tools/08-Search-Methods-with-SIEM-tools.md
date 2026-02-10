# 🔍 Search Methods with SIEM Tools

---

## 📌 What is a SIEM?
A **Security Information and Event Management (SIEM)** system is an application that:
- Collects log data from multiple sources
- Normalizes and indexes the data
- Enables analysts to search, correlate, and investigate security events

SIEMs are essential for:
- Alert triage  
- Threat detection  
- Incident investigation  
- Compliance monitoring  

---

## 🧠 Why Search Methods Matter
SIEM platforms store **massive volumes of data**, sometimes spanning years.

Broad searches (e.g., searching only for `failed login`) can:
- Return thousands of results
- Slow down investigations

Efficient analysts use **targeted search methods** to:
- Reduce noise  
- Improve performance  
- Find relevant events faster  

---

## 🟦 Splunk Searches

### 🔹 Search Processing Language (SPL)
Splunk uses **Search Processing Language (SPL)** to query and manipulate data.

SPL allows analysts to:
- Search indexed data
- Filter results
- Transform results into charts or tables

---
<img width="1600" height="680" alt="image" src="https://github.com/user-attachments/assets/a186d3c1-6bf3-457b-8668-13b7b1c35f7b" />

### 🔹 Basic SPL Search Example

    index=main fail

**Explanation:**
- `index=main` → Search only the `main` index  
- `fail` → Return events containing the word *fail*  

⚠️ This is a **broad search** and may return many results.

---

### 🔹 Pipes in SPL

SPL uses the pipe symbol `|` to chain commands together  
(similar to Linux piping).

    index=main fail | chart count by host

**What’s happening:**
1. Search for events containing `fail`
2. Pass results to the next command
3. Count failures grouped by `host`

✅ Useful for identifying hosts with repeated failures.

---

### 🔹 Wildcards

Wildcards expand search results using `*`.

    index=main fail*

This matches:
- `fail`
- `failed`
- `failure`

📌 Helpful when logs use different wording.

---

### 🔹 Exact Phrase Searches

Use double quotes for exact matches:

    "login failure"

This matches only events containing **that exact phrase**.

---

## 🟨 Google Security Operations (Chronicle)

> Formerly known as **Chronicle**, now rebranded as **Google Security Operations (Google SecOps)**

Google SecOps focuses on:
- Cloud-scale log ingestion
- Fast search through normalized data
- Unified security analytics

---

## 🔹 Search Types in Google SecOps

There are **two primary search types**:

### 1️⃣ Unified Data Model (UDM) Search (Default)

- Searches **normalized and indexed** data
- Faster and more structured
- Best for most investigations

Example:

    metadata.event_type = "USER_LOGIN"

**What this does:**
- Searches authentication-related events
- Uses normalized UDM fields

---

### 🔹 Common UDM Field Categories

| Field Category | Description |
|---------------|-------------|
| **Entities** | Devices, users, IPs, processes |
| **Event Metadata** | Event type, timestamps |
| **Network Metadata** | Protocols, ports, connections |
| **Security Results** | Outcomes like malware detected or quarantined |

---

### 2️⃣ Raw Log Search

- Searches **raw, unparsed logs**
- Slower than UDM searches
- Useful when normalized fields are unavailable

Supports:
- Filenames
- Hashes
- Usernames
- Regular expressions (regex)

📌 Use this when UDM search does not return expected results.

---

## 🧩 When to Use Which Search

| Scenario | Recommended Search |
|--------|--------------------|
| Authentication events | UDM Search |
| Network activity | UDM Search |
| Unparsed logs | Raw Log Search |
| Pattern matching | Raw Log Search + Regex |

---

## ✅ Key Takeaways
- SIEM tools differ, but core concepts remain the same
- Efficient searches save time and reduce noise
- SPL (Splunk) and UDM (Google SecOps) are optimized for speed
- Raw searches are powerful but slower

Mastering SIEM search techniques is a **core SOC analyst skill**.

---

## 📚 Further Reading

- Splunk Search Manual  
- Google Security Operations Quickstart  
- Google SecOps UDM Field Reference  

---

**✍️ Notes By Abhishek (Ez Abyss)**
