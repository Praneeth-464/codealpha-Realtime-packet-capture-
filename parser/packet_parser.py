# parser/packet_parser.py

from scapy.layers.inet import (
    IP,
    TCP,
    UDP,
    ICMP
)

from scapy.layers.dns import DNS

from scapy.packet import Raw


# -----------------------------------------
# PARSE PACKET
# -----------------------------------------
def parse_packet(packet):

    # -------------------------------------
    # DEFAULT PACKET STRUCTURE
    # -------------------------------------
    packet_data = {

        "src_ip": "N/A",

        "dst_ip": "N/A",

        "src_port": "N/A",

        "dst_port": "N/A",

        "protocol": "UNKNOWN",

        "payload": "No Payload"

    }


    try:

        # ---------------------------------
        # IP LAYER
        # ---------------------------------
        if packet.haslayer(IP):

            packet_data["src_ip"] = (
                packet[IP].src
            )

            packet_data["dst_ip"] = (
                packet[IP].dst
            )


        # ---------------------------------
        # ICMP
        # ---------------------------------
        if packet.haslayer(ICMP):

            packet_data["protocol"] = (
                "ICMP"
            )


        # ---------------------------------
        # TCP
        # ---------------------------------
        elif packet.haslayer(TCP):

            packet_data["protocol"] = (
                "TCP"
            )

            packet_data["src_port"] = (
                packet[TCP].sport
            )

            packet_data["dst_port"] = (
                packet[TCP].dport
            )


            # HTTPS
            if (

                packet[TCP].sport == 443

                or

                packet[TCP].dport == 443

            ):

                packet_data["protocol"] = (
                    "HTTPS"
                )


            # HTTP
            elif (

                packet[TCP].sport == 80

                or

                packet[TCP].dport == 80

            ):

                packet_data["protocol"] = (
                    "HTTP"
                )


        # ---------------------------------
        # UDP
        # ---------------------------------
        elif packet.haslayer(UDP):

            packet_data["protocol"] = (
                "UDP"
            )

            packet_data["src_port"] = (
                packet[UDP].sport
            )

            packet_data["dst_port"] = (
                packet[UDP].dport
            )


            # DNS
            if packet.haslayer(DNS):

                packet_data["protocol"] = (
                    "DNS"
                )


        # ---------------------------------
        # PAYLOAD
        # ---------------------------------
        if packet.haslayer(Raw):

            try:

                payload = (
                    packet[Raw].load
                )

                packet_data["payload"] = (
                    str(payload[:50])
                )

            except:

                packet_data["payload"] = (
                    "Payload Error"
                )


    except Exception as e:

        print(
            f"[ERROR] Packet Parsing Failed: {e}"
        )


    return packet_data