# get_interfaces.py

from scapy.all import get_if_list

print("\nAvailable Network Interfaces:\n")

for interface in get_if_list():

    print(interface)