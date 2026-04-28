# Firewall-Project
Created Python scripts for log parsingand pattern detection 
to simulate intrusion detection use cases. 
Experimented with AI/LLM integration for basic automation tasks. 

NETWORK SECURITY TOOLS
======================

This project contains two Python scripts for network security monitoring and firewall simulation.

FILES
-----

DoS_blocker.py
- Real-time DoS attack prevention tool
- Monitors packet rates from incoming IP addresses
- Automatically blocks IPs that exceed 40 packets per second
- Uses iptables to block malicious IPs
- Requires root privileges (sudo) to run

firewall.py
- Firewall rule simulator
- Generates random IP addresses in the 192.168.1.x range
- Checks IPs against a predefined blocklist
- Prints whether each IP is allowed or blocked
- Does not require root privileges (simulation only)

HOW TO USE
----------

Run the firewall simulator:
python3 firewall.py

Run the DoS blocker (requires root):
sudo python3 DoS_blocker.py

REQUIREMENTS
------------

For DoS_blocker.py:
- Linux operating system
- Python 3
- Scapy library (install with: pip install scapy)
- Root/sudo access

For firewall.py:
- Python 3 only (no extra libraries needed)

NOTES
-----

- DoS_blocker.py modifies actual iptables rules on your system
- Blocked IPs remain blocked until you manually clear iptables rules
- To unblock an IP: sudo iptables -D INPUT -s [IP_ADDRESS] -j DROP
- firewall.py is a simulation and does not change any real firewall settings

THRESHOLD
---------

The DoS blocker uses a threshold of 40 packets per second. You can change this by editing the THRESHOLD variable in DoS_blocker.py. Lower values make the script more sensitive.

AUTHOR
------

Network Security Tools - For educational purposes only
