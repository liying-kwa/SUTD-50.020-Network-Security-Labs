#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
        pkt.show()

pkt = sniff(filter='tcp and host 10.0.2.129',prn=print_pkt)
