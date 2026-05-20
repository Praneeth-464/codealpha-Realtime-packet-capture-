# utils/packet_storage.py

# -----------------------------------------
# GLOBAL PACKET STORAGE
# -----------------------------------------

captured_packets = []


# -----------------------------------------
# ADD PACKET
# -----------------------------------------
def add_packet(packet_data):

    captured_packets.append(packet_data)


# -----------------------------------------
# GET PACKETS
# -----------------------------------------
def get_packets():

    return captured_packets


# -----------------------------------------
# CLEAR PACKETS
# -----------------------------------------
def clear_packets():

    captured_packets.clear()