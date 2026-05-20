# payload/payload_extractor.py

from scapy.packet import Raw


def extract_payload(packet):

    try:

        # Check Raw Layer
        if packet.haslayer(Raw):

            payload = packet[Raw].load

            # Convert bytes to readable text
            try:
                readable_payload = payload.decode(errors="ignore")

            except:
                readable_payload = str(payload)

            return readable_payload[:200]

        return "No Payload"

    except Exception as e:

        return f"Payload Error: {str(e)}"