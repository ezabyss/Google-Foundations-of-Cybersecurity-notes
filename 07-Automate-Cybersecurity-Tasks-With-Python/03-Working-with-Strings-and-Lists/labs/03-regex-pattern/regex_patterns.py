#!/usr/bin/env python3
"""
regex_patterns.py
Use Regular Expressions to Find Patterns (Security Automation)

Lab Goals:
1) Extract device IDs that start with 'r15' (OS requires update)
2) Extract valid IPv4 addresses from login logs
3) Compare extracted IPs against a flagged list

Key Regex Symbols Used:
- \w      any alphanumeric/underscore character
- \d      any digit
- \.      literal period
- +       one or more occurrences
- {x,y}   between x and y repetitions

"""

import re

def extract_r15_devices(devices: str) -> list[str]:
    """
    Extract device IDs that start with 'r15' followed by one or more word chars.
    Example match: r151dm4, r15xk9h
    """
    target_pattern = r"r15\w+"
    return re.findall(target_pattern, devices)


def extract_valid_ipv4(log_file: str) -> list[str]:
    """
    Extract IP addresses of the form d{1,3}.d{1,3}.d{1,3}.d{1,3}.
    Note: This validates segment length (1–3 digits), not numerical range (0–255).
    """
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.findall(pattern, log_file)


def analyze_flagged_ips(valid_ips: list[str], flagged_addresses: list[str]) -> None:
    """
    Print whether each valid IP is flagged or not.
    """
    for address in valid_ips:
        if address in flagged_addresses:
            print(f"The IP address {address} has been flagged for further analysis.")
        else:
            print(f"The IP address {address} does not require further analysis.")


def main() -> None:
    # ----------------------------
    # Part A: Device update targeting (r15*)
    # ----------------------------
    devices = (
        "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk "
        "253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac "
        "i4l56nq g07h55q 081qc9t r159r1u"
    )

    print("=== Part A: Devices requiring update (prefix 'r15') ===")
    r15_devices = extract_r15_devices(devices)
    print("Matched devices:", r15_devices)
    print()

    # ----------------------------
    # Part B: Extract valid IPv4-like addresses from logs
    # ----------------------------
    log_file = (
        "eraab 2022-05-10 6:03:41 192.168.152.148 \n"
        "iuduike 2022-05-09 6:46:40 192.168.22.115 \n"
        "smartell 2022-05-09 19:30:32 192.168.190.178 \n"
        "arutley 2022-05-12 17:00:59 1923.1689.3.24 \n"
        "rjensen 2022-05-11 0:59:26 192.168.213.128 \n"
        "aestrada 2022-05-09 19:28:12 1924.1680.27.57 \n"
        "asundara 2022-05-11 18:38:07 192.168.96.200 \n"
        "dkot 2022-05-12 10:52:00 1921.168.1283.75 \n"
        "abernard 2022-05-12 23:38:46 19245.168.2345.49 \n"
        "cjackson 2022-05-12 19:36:42 192.168.247.153 \n"
        "jclark 2022-05-10 10:48:02 192.168.174.117 \n"
        "alevitsk 2022-05-08 12:09:10 192.16874.1390.176 \n"
        "jrafael 2022-05-10 22:40:01 192.168.148.115 \n"
        "yappiah 2022-05-12 10:37:22 192.168.103.10654 \n"
        "daquino 2022-05-08 7:02:35 192.168.168.144"
    )

    print("=== Part B: Extract valid IPv4-like addresses ===")
    valid_ip_addresses = extract_valid_ipv4(log_file)
    print("Extracted valid_ip_addresses:", valid_ip_addresses)
    print()

    # ----------------------------
    # Part C: Compare to flagged list
    # ----------------------------
    flagged_addresses = [
        "192.168.190.178",
        "192.168.96.200",
        "192.168.174.117",
        "192.168.168.144",
    ]

    print("=== Part C: Flagged IP Analysis ===")
    analyze_flagged_ips(valid_ip_addresses, flagged_addresses)


if __name__ == "__main__":
    main()
