from scapy.all import ARP, Ether, srp
from m_dict import *

def scan():
    # target_ip = "10.244.149.69"
    target_ip = "10.244.0.1/24"
    arp = ARP(pdst=target_ip)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp
    result = srp(packet, timeout=3)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

def get_manufacturer(mac):
    a_mac = mac.replace(":", "")

    try:
        thing = mac_dict[a_mac.upper()]
    except:
        return "Unknown"
    else:
        return thing


# DEBUGGING
# print("Available devices in the network:")
# print("IP" + " "*18+"MAC")
# for client in clients:
#     print("{:16}    {}".format(client['ip'], client['mac']))
