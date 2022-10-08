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
    # print(data)

    for line in data:
        u_data = line.to_dict()
        formatted_data += f"IP Address: {u_data['ip']:12} | Mac Address: {u_data['mac']:10} | Manufacturer: {u_data['manufacturer']:1} \n"

    return formatted_data


def main():
    clients = scan()
    gui = App()
    gui.mainloop()
    for client in clients:
        compile_device_list(client)





if __name__ == "__main__":
    main()