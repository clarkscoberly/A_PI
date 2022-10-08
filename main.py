"""
Created By: Clark Coberly, Dallin Sevy, Grant Holley
Purpose: Hackathon Project
We, ourselves wrote this code
"""
import db as DB
from gui import *
import scanner as SCANNER

def main():
    db = DB()
    scanner = SCANNER()
     
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