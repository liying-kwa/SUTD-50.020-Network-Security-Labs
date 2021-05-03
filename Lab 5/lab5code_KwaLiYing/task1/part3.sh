#!/bin/bash

# Prevent telnet to Machine B
sudo iptables -A OUTPUT -d 159.203.188.92 -p tcp -j DROP
sudo iptables -A OUTPUT -d 162.243.169.120 -p tcp -j DROP
sudo iptables -A OUTPUT -d 159.203.184.51 -p tcp -j DROP
sudo iptables -A OUTPUT -d 67.205.142.78 -p tcp -j DROP

# Set default policy as ACCEPT
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

