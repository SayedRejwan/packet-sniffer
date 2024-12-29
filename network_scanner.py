# Network scanner script
from scapy.all import ARP, Ether, srp

def scan_network(network):
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    for element in answered:
        print(f"IP: {element[1].psrc}, MAC: {element[1].hwsrc}")

if __name__ == "__main__":
    scan_network("192.168.1.0/24")
