#!/usr/bin/python3

from scapy.all import *
import random


# Construct the DNS header and payload
Qdsec = DNSQR(qname='twysw.example.com')
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec)

# Construct the IP, UDP headers, and the entire packet
ip = IP(dst='10.0.2.129', src="10.0.2.123")
udp = UDP(dport=53, sport=33333, chksum=0)
pkt = ip/udp/dns

# Save the packet to a file
with open('ip_req.bin', 'wb') as f:
  f.write(bytes(pkt))

