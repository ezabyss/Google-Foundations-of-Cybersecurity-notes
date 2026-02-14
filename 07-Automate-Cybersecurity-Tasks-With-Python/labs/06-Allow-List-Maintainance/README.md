# 🔐 Allow-List Maintenance Algorithm (Python)
*parse + remove + rewrite*

---

## 🎯 Objective

Automate allow-list cleanup:

- Read `allow_list.txt` (allowed IPs)
- Remove IPs in `remove_list` (revoked access)
- Rewrite the file with the updated allow list

This matches a real SOC workflow: keeping access control lists accurate.

---

## 🧠 Scenario

- `allow_list.txt` contains IP addresses that can access restricted content.
- Some IPs should no longer be allowed.
- We remove those IPs automatically to prevent unauthorized access.

---

## 📌 Inputs

- File: `allow_list.txt`
- List: `remove_list` (IPs to remove)

Example:

    import_file = "allow_list.txt"
    remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

---

## 🧩 Algorithm Pipeline

File → String → List → Filter → String → Rewrite file

1) Read file using `open(..., "r")`  
2) Parse using `.split()`  
3) Remove items found in `remove_list`  
4) Convert list back to text using `" ".join(...)`  
5) Rewrite file using `open(..., "w")`

---

## ✅ Why We Don’t Remove While Looping

A common bug is doing:

    for element in ip_list:
        if element in remove_list:
            ip_list.remove(element)

This can skip items because the list changes while you're looping.

Instead, we safely build a new list:

    updated_list = []
    for ip in ip_list:
        if ip not in remove_list:
            updated_list.append(ip)

---

## 🧑‍💻 Core Function Used

    def update_file(import_file, remove_list):
        with open(import_file, "r") as file:
            ip_addresses = file.read()

        ip_list = ip_addresses.split()

        updated_list = []
        for ip in ip_list:
            if ip not in remove_list:
                updated_list.append(ip)

        updated_text = " ".join(updated_list)

        with open(import_file, "w") as file:
            file.write(updated_text)

---

## ▶️ How to Run

    python3 update_allow_list.py

---

## 🛡 Real-World Security Relevance

This is the same logic used to maintain:

- allow lists / deny lists
- firewall rule sources
- VPN access ranges
- application IP allow rules
- incident response containment lists

---

## 🧠 Key Takeaways

- `.read()` loads file content into a string
- `.split()` turns the string into a list for easy iteration
- Filtering is safer than removing while iterating
- `" ".join(list)` converts the list back into file-ready text
- Wrapping logic in a function makes it reusable

---

**✍️ Notes By Abhishek (Ez Abyss)**
