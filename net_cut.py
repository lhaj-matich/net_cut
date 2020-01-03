#!/usr/bin/env python

from netfilterqueue import NetfilterQueue
import scapy.all as scapy


def Processed_packets(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print (scapy_packet.show())
    packet.accept()

queue = NetfilterQueue()
queue.bind(0, Processed_packets)
queue.run()
