#!/usr/bin/python3

from scapy.all import *

m_ip='10.0.2.130'
broadcast_mac='ff:ff:ff:ff:ff:ff'

E = Ether(dst=broadcast_mac)
A = ARP(op='is-at', psrc=m_ip, pdst=m_ip, hwdst=broadcast_mac)

pkt = E/A
ls(pkt)
sendp(pkt)
