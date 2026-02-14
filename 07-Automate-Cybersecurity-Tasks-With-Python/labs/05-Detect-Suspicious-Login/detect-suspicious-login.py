#!/usr/bin/env python3
"""
detect-suspicious-logins.py

This program checks a log file that contains failed login attempts.
If a user fails to log in 3 or more times, their account is locked.
"""

# Name of the log file that contains failed login attempts
LOG_FILE = "failed_logins.txt"

# Maximum number of allowed failed attempts
THRESHOLD = 3


def read_failed_logins(path: str) -> list[str]:
    """
    Open the log file and return a list of usernames.

    Each line in the file represents one failed login attempt.
    """
    # Open the file in read mode ("r")
    with open(path, "r") as file:
        # Read the entire file as one string
        # Then split it into a list of usernames
        return file.read().split()


def login_check(login_list: list[str], current_user: str, threshold: int = 3) -> None:
    """
    Check how many times a specific user failed to log in.
    This version uses a simple loop to count failures.
    """

    # Start a counter at 0
    counter = 0

    # Go through every username in the log
    for user in login_list:
        # If the username matches the current user
        if user == current_user:
            # Increase the counter by 1
            counter += 1

    # After checking all entries, decide what to do
    if counter >= threshold:
        print(f"🚨 ALERT: Account Locked (user={current_user}, failures={counter})")
    else:
        print(f"✅ Login Allowed (user={current_user}, failures={counter})")


def build_failure_counts(login_list: list[str]) -> dict[str, int]:
    """
    Create a dictionary that stores:
    username -> number of failed attempts

    This makes checking faster because we count only once.
    """

    # Create an empty dictionary
    counts: dict[str, int] = {}

    # Loop through each username in the log
    for user in login_list:
        # If the user already exists in the dictionary,
        # increase their failure count by 1.
        # If not, start their count at 1.
        counts[user] = counts.get(user, 0) + 1

    return counts


def login_check_fast(counts: dict[str, int], current_user: str, threshold: int = 3) -> None:
    """
    Check login attempts using the pre-built dictionary.
    This is faster than looping every time.
    """

    # Get the number of failures for this user.
    # If the user is not in the dictionary, default to 0.
    failures = counts.get(current_user, 0)

    # Decide whether to lock the account
    if failures >= threshold:
        print(f"🚨 ALERT: Account Locked (user={current_user}, failures={failures})")
    else:
        print(f"✅ Login Allowed (user={current_user}, failures={failures})")


def main() -> None:
    """
    Main function that runs the program.
    """

    # Read usernames from the failed login file
    usernames = read_failed_logins(LOG_FILE)

    print("=== Parsed Failed Login Usernames ===")
    print(usernames)
    print()

    # Example users to test
    # You can change these names to test different users
    test_users = ["elarson", "eraab", "bmoreno"]

    print("=== Simple Check (counts each time using loop) ===")
    for u in test_users:
        login_check(usernames, u, THRESHOLD)
    print()

    print("=== Fast Check (uses dictionary for speed) ===")
    # Build the dictionary once
    counts = build_failure_counts(usernames)

    # Check each test user using the faster method
    for u in test_users:
        login_check_fast(counts, u, THRESHOLD)


# This makes sure the program runs only when executed directly
if __name__ == "__main__":
    main()
