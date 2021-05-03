#!/bin/bash

# Prevent telnet to Machine B
sudo iptables -A OUTPUT -p tcp --dport 23 -j DROP

# Set default policy as ACCEPT
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

