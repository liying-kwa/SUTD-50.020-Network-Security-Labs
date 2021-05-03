#!/bin/bash

# Clear all rules
sudo iptables -F

# Set default policy as ACCEPT
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT


