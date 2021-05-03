#!/bin/bash

# Prevent telnet to Machine B
sudo iptables -A OUTPUT -d 157.240.7.35 -j DROP

# Set default policy as ACCEPT
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

