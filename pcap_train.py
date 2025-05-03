# Stub for future pcap-based learning
# Dependencies: pip install scapy
from scapy.all import rdpcap

def parse_pcap(file_path):
    packets = rdpcap(file_path)
    print(f"Loaded {len(packets)} packets.")
    for pkt in packets[:10]:
        if pkt.haslayer('IP'):
            print(pkt['IP'].src, "->", pkt['IP'].dst)

# Example:
# parse_pcap("sample.pcap")
