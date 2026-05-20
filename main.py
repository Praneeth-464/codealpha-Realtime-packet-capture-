# main.py

from capture.sniffer import start_sniffing

from parser.packet_parser import parse_packet

from analyzer.protocol_analyzer import analyze_protocol

from ui.dashboard import display_packet

from utils.logger import save_log


def process_packet(packet):

    # Parse packet
    packet_data = parse_packet(packet)

    # Ignore empty packets
    if not packet_data:
        return

    # Analyze protocol
    analysis = analyze_protocol(packet_data)

    # Display in dashboard
    display_packet(packet_data, analysis)

    # Save log
    save_log(packet_data)


if __name__ == "__main__":

    print("=" * 50)
    print(" REALTIME PACKET ANALYZER STARTED ")
    print("=" * 50)

    start_sniffing(process_packet)