# tests/test_parser.py

from scapy.layers.inet import IP, TCP
from parser.packet_parser import parse_packet


# Create Dummy Packet
dummy_packet = IP(
    src="192.168.1.10",
    dst="142.250.183.14"
) / TCP(
    sport=5050,
    dport=443
)


# Parse Packet
parsed_data = parse_packet(dummy_packet)


print("[TEST] Parsed Packet Data:\n")

for key, value in parsed_data.items():

    print(f"{key} : {value}")