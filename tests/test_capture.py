# tests/test_capture.py

from capture.sniffer import start_sniffing


def test_packet(packet):

    print("[TEST] Packet Captured Successfully")


print("[TEST] Starting Capture Test...")

start_sniffing(test_packet)