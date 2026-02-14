#!/usr/bin/env python3
"""
update-allow-list.py

Goal:
- Read a text file containing allowed IP addresses
- Remove IPs that should no longer have access
- Rewrite the file with the updated allow list

Note:
- The allow-list file often stores IPs separated by spaces/newlines.
- This script supports both because we use .split().
"""

from __future__ import annotations


def update_file(import_file: str, remove_list: list[str]) -> None:
    """
    Reads IP addresses from import_file, removes any IPs in remove_list,
    then rewrites the file with the cleaned allow list.
    """

    # 1) Read the file as text
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # 2) Convert the text into a list of IPs
    ip_list = ip_addresses.split()

    # 3) Remove revoked IPs (safe way: build a new list)
    #    This avoids bugs that happen when removing from a list while looping over it.
    updated_list = []
    for ip in ip_list:
        if ip not in remove_list:
            updated_list.append(ip)

    # 4) Convert the list back to a string (space-separated)
    updated_text = " ".join(updated_list)

    # 5) Rewrite the file with updated content
    with open(import_file, "w") as file:
        file.write(updated_text)


def main() -> None:
    # Lab inputs (edit to match your file + removal list)
    import_file = "allow_list.txt"

    remove_list = [
        "192.168.97.225",
        "192.168.158.170",
        "192.168.201.40",
        "192.168.58.57",
    ]

    # Run the update
    update_file(import_file, remove_list)

    # Verify by reading the updated file
    with open(import_file, "r") as file:
        text = file.read()

    print("=== Updated allow_list.txt ===")
    print(text)


if __name__ == "__main__":
    main()
