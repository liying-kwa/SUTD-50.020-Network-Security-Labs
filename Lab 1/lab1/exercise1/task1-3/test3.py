#!/usr/bin/python3

from scapy.all import *

a = IP()
a.dst = '128.230.0.1'
a.ttl = 2
a.show()

b = ICMP()
send(a/b)
