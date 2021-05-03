#!/bin/bash

# Prevent Machine B from accessing web server
sudo iptables -A INPUT -s 10.0.2.129 -p tcp --dport 80 -j DROP

# Prevent Machine B from accessing SSH server
sudo iptables -A INPUT -s 10.0.2.129 -p tcp --dport 22 -j DROP

# Set default policy as ACCEPT
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

