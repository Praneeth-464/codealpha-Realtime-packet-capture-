# tests/test_protocol.py

from analyzer.protocol_analyzer import analyze_protocol


# Test Data Samples
test_packets = [

    {"protocol": "HTTP"},
    {"protocol": "HTTPS"},
    {"protocol": "DNS"},
    {"protocol": "TCP"},
    {"protocol": "UDP"},
    {"protocol": "ICMP"},
    {"protocol": "SSH"},
    {"protocol": "FTP"},
    {"protocol": "SMTP"},
    {"protocol": "DHCP"},
    {"protocol": "UNKNOWN"}

]


print("[TEST] Protocol Analyzer Test\n")


for packet in test_packets:

    result = analyze_protocol(packet)

    print(f"Protocol : {packet['protocol']}")
    print(f"Analysis : {result}")
    print("-" * 40)