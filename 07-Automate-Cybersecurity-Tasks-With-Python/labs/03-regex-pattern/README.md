# 🧪 Regex Pattern Extraction for Security Logs (Python)

## 📌 Overview

Security analysts often automate detection tasks by extracting patterns from logs, such as:

- Device IDs that indicate outdated operating systems
- IP addresses related to suspicious login attempts

This lab uses Python regular expressions to:

1) Extract device IDs starting with `r15` (devices requiring an OS update)  
2) Extract valid IPv4-like addresses from a login log  
3) Compare extracted IPs against a known list of flagged IP addresses

---

## 🎯 Skills Demonstrated

- `re` module fundamentals
- Regex pattern creation for structured strings
- `re.findall()` for bulk extraction
- Filtering and comparison with lists
- Iteration + conditional logic for security decisions

---

## ▶️ How to Run

```
python3 regex_patterns.py
```

## 🧩 Part A — Device Update Targeting
### Goal
- Extract device IDs that start with r15.
- Pattern Used `r15\w+`
  
### Meaning:
- r15 must appear at the start of the device ID
- \w matches alphanumeric characters and _
- + means “one or more” characters after r15

Example Matches
`r151dm4, r15xk9h, r15u9q5, r159r1u`

## 🧩 Part B — Extract Valid IPv4-like Addresses from Logs
### Goal
- Extract IP addresses in the form x.x.x.x where each segment contains 1 to 3 digits.
- Pattern Used `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

### Meaning:
- `\d{1,3}` matches 1–3 digits per segment
- `\.` matches a literal period

## Four segments total

Note:
This validates segment length (1–3 digits), but does not confirm the numeric range (0–255).

## 🧩 Part C — Flagged IP Comparison

### Goal
Loop through extracted IPs and check if each is in the flagged list.

If flagged:

The IP address ____ has been flagged for further analysis.
If not flagged:
The IP address ____ does not require further analysis.

## 🛡 Real-World Security Relevance
This workflow maps directly to:
- SIEM rule-building (extracting IOCs)
- Threat hunting (pattern discovery)
- Patch management targeting (device identifiers)
- Investigation triage (flagged vs non-flagged IPs)


## 🧠 Key Takeaways
- Regular expressions help extract structured indicators quickly.
- re.findall() returns all matches as a list.
- \w, \d, \., +, and {x,y} are core building blocks.
- Curly braces {1,3} help filter out common invalid patterns.
- Lists + conditionals make it easy to flag indicators for review.

---
✍️ Notes By Abhishek (Ez Abyss)
