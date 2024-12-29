# Packet sniffer script
from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

if __name__ == "__main__":
    sniff(prn=packet_handler, store=False)
