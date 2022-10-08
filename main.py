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

def main():
    clients = scan()
    for client in clients:
        compile_device_list(client)

    gui = App()
    gui.mainloop()



if __name__ == "__main__":
    main()