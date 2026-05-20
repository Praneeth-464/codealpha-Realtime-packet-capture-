# Realtime Packet Analyzer

A professional realtime network packet analyzer built using Python, Streamlit, and Scapy.

## Features

- Realtime packet capturing
- Active network interface detection
- Live packet flow monitoring
- Protocol filtering
- Packet search
- Packet details viewer
- Modern professional dashboard UI
- Start / Stop packet capture
- IP packet parsing
- TCP / UDP / DNS / HTTP detection

---

## Workflow

1. User selects a network interface from the dashboard.

2. The application detects active network adapters.

3. Packet capturing starts on the selected interface.

4. Scapy captures realtime network packets.

5. Captured packets are parsed using the packet parser.

6. Important packet information is extracted:
   - Source IP
   - Destination IP
   - Source Port
   - Destination Port
   - Protocol
   - Payload

7. Parsed packets are stored temporarily.

8. The Streamlit dashboard displays live packet flow.

9. Users can:
   - Search packets
   - Filter protocols
   - View packet details
   - Monitor realtime traffic

10. Packet capture can be stopped anytime using the dashboard.

---

## Technologies Used

- Python
- Streamlit
- Scapy
- Pandas

## Installation

Install dependencies:

```bash
pip install -r requirements.txt