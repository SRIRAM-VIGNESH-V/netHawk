# netHawk
NetHawk is a CLI (Windows and linux ) based networking penetration testing tool for active reconnaissance and enumeration of hosts on networks with Scapy 2.5.0 , capable of live host identification, OS detection and service identification of hosts on networks and also capable of stealth scanning networks for Firewall , IDS and IPS bypassing using synthetically crafted packets.
## Arguments 
+ ![image](https://github.com/SRIRAM-VIGNESH-V/netHawk/assets/159048515/9fd45849-3408-472f-8fb2-f13119e423fb)<br>
* -sC : Scan common ports
* -sA : Scan all ports
* -sP : Scan a range ports
* -sO : Scan OS of a target
* -sV : scan service running on host
### Argument options
+ -d | Discover hosts in the network
+ -p | Protocol to use in the scan
+ -i | Interface to use
+ -t | Timeout to each request (reduce to avoid IDS/IPS triggers)
+ -st| Use stealth scan method (TCP)
+ -v | verbose scan<br>


## scapy 
![image](https://github.com/SRIRAM-VIGNESH-V/netHawk/assets/159048515/3fbd5e3e-4fec-46e3-a5d7-ecbfa93225d8)<br>
Scapy is a Python tool for synthetic crafting, analyzing, and manipulating network packets. It supports a wide range of protocols and provides features for packet inspection, sending, sniffing, and custom protocol creation.

## nmap service-probes<br>
![image](https://github.com/SRIRAM-VIGNESH-V/netHawk/assets/159048515/99aa1e78-e569-4722-8a4c-e6c75a66bdb4)<br>
Nmap service probes are essential for the tool's accurate service detection during network scans. These probes, stored in a database, consist of patterns matched against responses to pinpoint specific services and versions running on target hosts. Users can customize probes for flexibility, contributing to Nmap's efficiency in recognizing diverse services and staying up-to-date. The information gathered aids in precise identification, version detection, and efficient network reconnaissance. 
## OS detection with TTL on packets
Analyzing Time-to-Live (TTL) values in received packets is a technique for OS detection. Different operating systems have distinct default TTL values, allowing for educated guesses about the target OS based on these values. This method provides insights into the likely operating system without specific tools like Nmap.
## IDS,IPS and Firewall bypass with stealth TCP scans 
Stealth TCP scans, like SYN scans, operate by sending SYN packets to a target's ports without completing the three-way handshake. This method is stealthy because it avoids establishing a full connection, minimizing detection by intrusion detection systems. SYN scans help identify open ports on a target system without arousing suspicion due to the incomplete connection attempt.
## live host identification
Live host identification using ICMP involves sending ICMP Echo Request (ping) packets to potential hosts and awaiting ICMP Echo Reply responses. A response indicates the host is alive. ICMP is commonly used for basic host reachability checks, aiding in network reconnaissance and troubleshooting.
## installation 
To install netHawk run the install.py file from terminal with root access. After successful installation, run netHawk keyword in terminal to start CLI. Use netHawk-help for CLI argument definitions and functions.
### LICENSE 
This project is licensed under MIT-license
