#!/usr/bin/env python3
"""
lab_import_parse.py
Exemplar: Import and parse a text file (Security Log Handling)

What this script demonstrates:
1) Read a log file using a with-statement + open(..., "r")
2) Store file contents as a string using .read()
3) Split the log string into a list using .split()
4) Append a missing entry using open(..., "a") + .write()
5) Create an allow-list file using open(..., "w") + .write()
6) Read back allow-list contents using .read()
7) Optional: reset login.txt to original contents

Folder structure expected:
- data/login.txt
- data/allow_list.txt
"""

import os
import sys


LOGIN_PATH = "data/login.txt"
ALLOW_LIST_PATH = "data/allow_list.txt"


ORIGINAL_LOGIN_FILE = """username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmitchel,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.168.144,7:02:35,2022-05-08
eraab,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.90,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuduike,192.168.131.147,17:50:00,2022-05-11
abellmas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
eraab,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-09
"""


def ensure_data_dir() -> None:
    os.makedirs("data", exist_ok=True)


def reset_login_file() -> None:
    ensure_data_dir()
    with open(LOGIN_PATH, "w") as file:
        file.write(ORIGINAL_LOGIN_FILE)


def seed_login_file_if_missing() -> None:
    ensure_data_dir()
    if not os.path.exists(LOGIN_PATH):
        reset_login_file()


def read_file_as_text(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


def append_missing_entry(path: str, missing_entry: str) -> None:
    # Ensure the missing entry starts on a new line (best practice)
    entry_to_write = "\n" + missing_entry if not missing_entry.startswith("\n") else missing_entry

    with open(path, "a") as file:
        file.write(entry_to_write)


def write_allow_list(path: str, ip_addresses: str) -> None:
    ensure_data_dir()
    with open(path, "w") as file:
        file.write(ip_addresses)


def main() -> None:
    # Optional reset flag
    if "--reset" in sys.argv:
        reset_login_file()
        print("Reset complete: data/login.txt restored to original contents.")
        return

    # Make sure the login file exists (helps run this lab outside Coursera)
    seed_login_file_if_missing()

    # ----------------------------
    # Task 1 & 2: Import + read file
    # ----------------------------
    print("=== Task 1 & 2: Import and Read Security Log File ===")
    import_file = LOGIN_PATH
    text = read_file_as_text(import_file)
    print(text)

    # ----------------------------
    # Task 3: Split the string into a list
    # ----------------------------
    print("\n=== Task 3: Split Imported Log into List ===")
    print(text.split())

    # ----------------------------
    # Task 4: Append missing entry
    # ----------------------------
    print("\n=== Task 4: Append Missing Entry ===")
    missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
    append_missing_entry(import_file, missing_entry)

    updated_text = read_file_as_text(import_file)
    print(updated_text)

    # ----------------------------
    # Task 5: Create variables for allow list file
    # ----------------------------
    print("\n=== Task 5: Prepare Allow List File Variables ===")
    import_file = ALLOW_LIST_PATH
    ip_addresses = (
        "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 "
        "192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 "
        "192.168.116.187 192.168.15.110 192.168.39.246"
    )
    print(import_file)
    print(ip_addresses)

    # ----------------------------
    # Task 6: Write allow list to file
    # ----------------------------
    print("\n=== Task 6: Write Allow List to File ===")
    write_allow_list(import_file, ip_addresses)

    # ----------------------------
    # Task 7: Read allow list from file
    # ----------------------------
    print("\n=== Task 7: Read Allow List File ===")
    text = read_file_as_text(import_file)
    print(text)


if __name__ == "__main__":
    main()
