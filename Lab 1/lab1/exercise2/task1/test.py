#!/usr/bin/python3

from scapy.all import *

E = Ether()
A = ARP()
pkt = E/A
ls(pkt)
sendp(pkt)
