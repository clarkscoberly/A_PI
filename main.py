"""
Created By: Clark Coberly, Dallin Sevy, Grant Holley
Purpose: Hackathon Project
We, ourselves wrote this code
"""
import db as DB
from gui import *
from scanner import *
from m_dict import *

IP = 0
MAC_ADDRESS = 1
MANUFACTERER = 2
OS = 3
FIRMWARE = 4
DATE_AND_TIME = 5

def get_manufacturer(mac):
    a_mac = mac.replace(":", "")
    return mac_dict[a_mac.upper()]
    # print(a_mac)



def main():
    db = DB()
    clients = scan()
    # print("Available devices in the network:")
    # print("IP" + " "*18+"MAC")
    device_info_list = []
    for client in clients:
        manufacturer = get_manufacturer(client['mac'][:8])
        print(manufacturer)
        device = (client['ip'], client['mac'], manufacturer)
        device_info_list.append(device)

    db.update_database()


        # print("{:16}    {}".format(client['ip'], client['mac'][:8]))
     



if __name__ == "__main__":
    main()







# import scapy.all as scapy 
# import argparse


# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-t", "--target", dest="target", help="Specify target IP or IP range")
#     options = parser.parse_args()
#     return options

# def scan(ip):
#     arp_packet = scapy.ARP(pdst=ip)
#     broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_broadcast_packet = broadcast_packet/arp_packet
#     answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
#     client_list = []

    
#     for element in answered_list:
#         client_dict = {"ip": element[1].psrc, "mac":element[1].hwsrc}
#         client_list.append(client_dict)

# def print_result(scan_list):
#     print("IP\t\t\tMAC\n-------------------------------------------")
#     for client in scan_list:
#         print(client["ip"] + "\t\t" + client["mac"])





# def main():
    
#     options = get_arguments()
#     result_list = scan(options.target)
#     print_result(result_list)
    
# if __name__ == "__main__":
#     main()