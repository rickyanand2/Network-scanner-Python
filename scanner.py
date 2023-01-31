# Import the required Scapy modules
from scapy.all import ARP, Ether, srp

# Define the target IP range to scan
target_ip = "192.168.1.1/24"

# Create an ARP packet to request the MAC addresses of devices in the network
arp = ARP(pdst=target_ip)

# Create an Ethernet broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine the ARP and Ethernet packets
packet = ether/arp

# Send the packet and receive the response, with a timeout of 3 seconds and verbosity turned off
result = srp(packet, timeout=3, verbose=0)[0]

# Create an empty list to store the found devices
clients = []

# Iterate through the received responses
for sent, received in result:
    # Add the IP and MAC addresses of each device to the list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# Print the found devices
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
