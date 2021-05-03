#!/usr/bin/python3

from scapy.all import *

def send_spoof(pkt):
    #pkt.show()
    a = IP()

    ip_src = pkt[IP].src
    x = pkt[IP].dst

    a.src = x
    a.dst = ip_src
    
    b = ICMP()
    p = a/b
    send(p)
