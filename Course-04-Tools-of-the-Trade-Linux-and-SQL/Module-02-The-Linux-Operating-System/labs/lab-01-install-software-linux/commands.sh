#!/bin/bash

# Confirm APT is installed
apt --version

# Update package list
sudo apt update

# Install Suricata
sudo apt install suricata -y

# Remove Suricata
sudo apt remove suricata -y

# Install tcpdump
sudo apt install tcpdump -y

# Reinstall Suricata
sudo apt install suricata -y
