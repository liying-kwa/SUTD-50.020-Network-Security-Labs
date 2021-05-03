#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(filter='tcp and src host 10.0.2.130 and dst port 23',prn=print_pkt)
