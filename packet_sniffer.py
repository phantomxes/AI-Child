from scapy.all import sniff, IP, TCP, DNSQR
from datetime import datetime
import json
from pathlib import Path

memory_file = Path.home() / "1man.army" / "memory" / "experience_log.json"
memory_file.parent.mkdir(parents=True, exist_ok=True)

try:
    with open(memory_file, "r") as f:
        memory = json.load(f)
except:
    memory = []

def packet_callback(pkt):
    label = "sniffer"
    command = ["packet_sniffer"]

    output = []
    if pkt.haslayer(IP):
        ip_layer = pkt[IP]
        output.append(f"{ip_layer.src} → {ip_layer.dst}")

    if pkt.haslayer(TCP):
        tcp = pkt[TCP]
        output.append(f"TCP Port {tcp.dport} | Flags: {tcp.flags}")

    if pkt.haslayer(DNSQR):
        dns = pkt[DNSQR]
        output.append(f"DNS Query: {dns.qname.decode()}")

    if not output:
        return

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "label": label,
        "command": command,
        "output_snippet": "\\n".join(output)
    }

    memory.append(entry)
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"[+] Packet logged: {entry['output_snippet'].splitlines()[0]}")

print("🕷️ Packet sniffer started. CTRL+C to stop.\n")
sniff(filter="ip", prn=packet_callback, store=0)
