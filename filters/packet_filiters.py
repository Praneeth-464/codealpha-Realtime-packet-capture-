# filters/packet_filters.py


def apply_filter(packet_data, selected_protocol=None):

    # No filter selected
    if selected_protocol is None:
        return True

    # Compare protocol
    packet_protocol = packet_data.get("protocol")

    if packet_protocol == selected_protocol:
        return True

    return False
