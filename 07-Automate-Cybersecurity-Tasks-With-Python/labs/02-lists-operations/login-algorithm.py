#!/usr/bin/env python3
"""
lab_login_algorithm.py
User-Device Access Verification Algorithm (Security Automation)

Concepts:
- List indexing
- .append(), .remove(), .index()
- Membership testing: in
- Conditionals + nested conditionals
- Functions for automation (login workflow)
"""

# ----------------------------
# Base datasets (synchronized lists)
# approved_users[i] -> approved_devices[i]
# ----------------------------

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]


def show_pair_at_index(i: int) -> None:
    """Task 1: Display the username and device at the same index."""
    print("Task 1 — List Indexing")
    print("approved_users[{}]: {}".format(i, approved_users[i]))
    print("approved_devices[{}]: {}".format(i, approved_devices[i]))
    print()


def add_user_device(new_user: str, new_device: str) -> None:
    """Task 2: Add a new user + device (keeps lists synchronized)."""
    print("Task 2 — Add New Approved User")
    approved_users.append(new_user)
    approved_devices.append(new_device)

    print("Updated approved_users:", approved_users)
    print("Updated approved_devices:", approved_devices)
    print()


def remove_user_device(user_to_remove: str, device_to_remove: str) -> None:
    """Task 3: Remove user + device."""
    print("Task 3 — Remove Departed User")

    if user_to_remove in approved_users:
        approved_users.remove(user_to_remove)
    if device_to_remove in approved_devices:
        approved_devices.remove(device_to_remove)

    print("Updated approved_users:", approved_users)
    print("Updated approved_devices:", approved_devices)
    print()


def is_user_approved(username: str) -> bool:
    """Task 4: Check if username is approved."""
    return username in approved_users


def get_assigned_device(username: str) -> str:
    """
    Task 5/6: Find index of username and return corresponding device.
    Assumes username exists in approved_users.
    """
    ind = approved_users.index(username)
    return approved_devices[ind]


def login(username: str, device_id: str) -> None:
    """
    Task 9: Automated login algorithm using nested conditional logic.

    Logic:
    - If username not approved -> deny
    - If approved -> verify device matches assigned device
    """
    print("Login Attempt — username={}, device_id={}".format(username, device_id))

    if username in approved_users:
        print("The user {} is approved to access the system.".format(username))

        ind = approved_users.index(username)
        assigned = approved_devices[ind]

        if device_id == assigned:
            print("{} is the assigned device for {}".format(device_id, username))
        else:
            print("{} is not their assigned device.".format(device_id))
    else:
        print("The username {} is not approved to access the system.".format(username))

    print("-" * 55)


def main() -> None:
    # Task 1: Index exploration (change index to experiment)
    show_pair_at_index(0)

    # Task 2: Add new approved user
    add_user_device("gesparza", "3rcv4w6")

    # Task 3: Remove a departing user
    remove_user_device("tshah", "2ye3lzg")

    # Task 4: Membership check
    print("Task 4 — Approval Check")
    username = "sgilmore"
    if is_user_approved(username):
        print("The user {} is approved to access the system.".format(username))
    else:
        print("The user {} is not approved to access the system.".format(username))
    print()

    # Task 5/6: Index + matching device lookup
    print("Task 5/6 — Index + Device Mapping")
    ind = approved_users.index(username)
    print("Index of {} is {}".format(username, ind))
    print("Assigned device for {} is {}".format(username, approved_devices[ind]))
    print()

    # Task 7/8/9: Login scenarios
    print("Task 7/8/9 — Login Algorithm Tests")
    login("bmoreno", "hl0s5o1")   # correct
    login("elarson", "r2s5r9g")   # wrong device
    login("abernard", "4n482ts")  # not approved


if __name__ == "__main__":
    main()
