# analyzer/protocol_analyzer.py


def analyze_protocol(packet_data):

    protocol = packet_data.get("protocol")

    if protocol == "HTTP":
        return "Web Traffic Detected"

    elif protocol == "HTTPS":
        return "Secure Web Traffic"

    elif protocol == "DNS":
        return "Domain Name Lookup Traffic"

    elif protocol == "TCP":
        return "Reliable TCP Communication"

    elif protocol == "UDP":
        return "Fast UDP Communication"

    elif protocol == "ICMP":
        return "Ping/ICMP Packet"

    elif protocol == "FTP":
        return "File Transfer Protocol"

    elif protocol == "SSH":
        return "Secure Remote Login"

    elif protocol == "SMTP":
        return "Email Transfer Traffic"

    elif protocol == "DHCP":
        return "Dynamic Host Configuration"

    else:
        return "Unknown Protocol"