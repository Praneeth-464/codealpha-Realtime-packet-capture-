# capture/sniffer.py

from scapy.all import sniff

from scapy.layers.inet import IP

from parser.packet_parser import (
    parse_packet
)

from utils.packet_storage import (
    add_packet
)

from utils.capture_state import (
    is_capturing
)


# -----------------------------------------
# PROCESS PACKET
# -----------------------------------------
def process_packet(packet):

    try:

        # ---------------------------------
        # ONLY PROCESS IP PACKETS
        # ---------------------------------
        if not packet.haslayer(IP):

            return


        # ---------------------------------
        # PARSE PACKET
        # ---------------------------------
        packet_data = parse_packet(
            packet
        )


        # ---------------------------------
        # STORE PACKET
        # ---------------------------------
        add_packet(
            packet_data
        )

    except Exception as e:

        print(
            f"[ERROR] Packet Processing Failed: {e}"
        )


# -----------------------------------------
# STOP FILTER
# -----------------------------------------
def stop_filter(packet):

    return not is_capturing()


# -----------------------------------------
# START SNIFFING
# -----------------------------------------
def start_sniffing(interface):

    print(
        f"[INFO] Capturing on: {interface}"
    )

    sniff(

        iface=interface,

        prn=process_packet,

        store=False,

        stop_filter=stop_filter

    )

    print(
        "[INFO] Packet Capture Stopped"
    )