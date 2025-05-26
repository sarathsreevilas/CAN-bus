from scapy.all import *
import sys

log_file = sys.argv[1]
pcap_file = sys.argv[2]

packets = []

with open(log_file) as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3 and '#' in parts[2]:
            can_id, payload = parts[2].split('#')
            if payload == '':
                continue  # Skip empty frames
            data = bytes.fromhex(payload)
            pkt = Ether() / IP(src="10.0.0.1", dst="10.0.0.2") / UDP(sport=1234, dport=1234) / Raw(load=data)
            packets.append(pkt)

print(f"✅ {len(packets)} CAN messages converted.")
wrpcap(pcap_file, packets)
print(f"💾 PCAP saved to: {pcap_file}")
