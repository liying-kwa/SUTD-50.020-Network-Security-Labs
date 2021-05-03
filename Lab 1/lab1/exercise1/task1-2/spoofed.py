#!/usr/bin/python3

from scapy.all import *

a = IP()
a.src = '12.130.2.1'
a.dst = '10.0.2.129'
a.show()

b = ICMP()
p = a/b
send(p)
