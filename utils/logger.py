# utils/logger.py

from datetime import datetime


def save_log(packet_data):

    with open("logs/captured_packets.log", "a") as file:

        log = (
            f"{datetime.now()} | "
            f"SRC={packet_data.get('src_ip')} | "
            f"DST={packet_data.get('dst_ip')} | "
            f"PROTO={packet_data.get('protocol')} | "
            f"SPORT={packet_data.get('src_port')} | "
            f"DPORT={packet_data.get('dst_port')}\n"
        )

        file.write(log)