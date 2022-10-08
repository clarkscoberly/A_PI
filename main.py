"""
Created By: Clark Coberly, Dallin Sevy, Grant Holley
Purpose: Hackathon Project
We, ourselves wrote this code
"""
from gui import *
from scanner import *
from m_dict import *
from cloud import *


def compile_device_list(client):
    manufacturer = get_manufacturer(client['mac'][:8])
    device = (client['ip'], client['mac'], manufacturer)
    add_item(device)
    

def contact_database(timeframe):
    return get_items(timeframe)


def get_information(timeframe):
    formatted_data = ""
    data = contact_database(timeframe)

    for line in data:
        u_data = line.to_dict()
        formatted_data += f"IP: {u_data['ip']:12}    |    Mac: {u_data['mac']:10}    |    Manufacturer: {u_data['manufacturer']:1} \n"
    return formatted_data

def do_scan():
    clients = scan()
    for client in clients:
        compile_device_list(client)

def main():
    gui = App()
    gui.mainloop()


if __name__ == "__main__":
    main()