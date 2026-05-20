# capture/interface_manager.py

from scapy.arch.windows import (
    get_windows_if_list
)

from scapy.all import sniff


# -----------------------------------------
# DETECT INTERFACE TRAFFIC
# -----------------------------------------
def interface_has_traffic(interface_name):

    try:

        packets = sniff(

            iface=interface_name,

            timeout=0.3,

            count=1,

            store=True

        )

        # If packets captured
        if len(packets) > 0:

            return True

        return False

    except:

        return False


# -----------------------------------------
# GET AVAILABLE INTERFACES
# -----------------------------------------
def get_available_interfaces():

    interfaces = []

    try:

        available_interfaces = (
            get_windows_if_list()
        )

        for interface in available_interfaces:

            description = interface.get(
                "description",
                "Unknown Adapter"
            )

            interface_name = interface.get(
                "name"
            )

            ips = interface.get(
                "ips",
                []
            )

            # ---------------------------------
            # DEFAULT ACTIVE STATUS
            # ---------------------------------
            active = False

            # ---------------------------------
            # CHECK VALID IP
            # ---------------------------------
            has_valid_ip = False

            if ips:

                for ip in ips:

                    ip = str(ip)

                    # Ignore loopback IP
                    if not ip.startswith("127."):

                        has_valid_ip = True
                        break

            # ---------------------------------
            # TRAFFIC DETECTION
            # ---------------------------------
            has_traffic = interface_has_traffic(
                interface_name
            )

            # ---------------------------------
            # FINAL ACTIVE DETECTION
            # ---------------------------------
            if has_valid_ip or has_traffic:

                active = True

            # ---------------------------------
            # INTERFACE DATA
            # ---------------------------------
            interface_data = {

                "name": interface_name,

                "description": description,

                "active": active

            }

            interfaces.append(
                interface_data
            )

        # ---------------------------------
        # SORT ACTIVE FIRST
        # ---------------------------------
        interfaces.sort(

            key=lambda x: x["active"],

            reverse=True

        )

    except Exception as e:

        print(
            f"[ERROR] Interface Scan Failed: {e}"
        )

    return interfaces