from getpass import getpass
from mysql.connector import connect, Error
import scapy.all as scapy
import argparse

# The following are the locations of where to store the data and where the data is within a list to be
# Pulled back out
IP = 0
MAC_ADDRESS = 1
MANUFACTERER = 2
OS = 3
FIRMWARE = 4
DATE_AND_TIME = 5


# user = A_PI
# pass = T3@ms_ap1
# host = 

class Db:

    def __init__(self):
        self.connection = self.connect_db()


    def connect_db(self):
        try:
            with connect(
                host= "0.0.0.0:5555",
                user=input("Enter username: "),
                password=input("Enter password: "),
            ) as connection:
                print(connection)
                return connection

        except Error as e:
            print(e)

    def update_table(self, formatted_data):
        """
        Get formatted information and then send it to the database.
        """

        update_to_send = formatted_data
        insert_data_query = """
        INSERT INTO data
        (ip, mac, manufacterer, os, firmware, start_time, end_time)
        VALUES ( %s, %s, %s, %s, %s, %s )
        """

        ###################################################################################################
        # The following is an example of the kind of formatted data that should be contained within formatted data.
        reviewers_records = [
            ("Chaitanya", "Baweja"),
            ("Mary", "Cooper"),
            ("John", "Wayne"),
            ("Thomas", "Stoneman")
        ]
        ###################################################################################################

        with self.connection.cursor() as cursor:
            cursor.executemany(insert_data_query, formatted_data)
            self.connection.commit()

    def get_information(self, data): # TODO DATA IS NOT WRITTEN YET
        """
        Gets info from the scanner or from main after the data is no longer in .csv form 
        """
        self.send_info(data)
        pass

    def populate_information(self):
        """
        Takes information from get_information and prepares it to be sent to GUI
        """
        #                            TODO THIS STATEMENT MAY ME INCORRECT
        # get_data_query = f"SELECT * FROM data WHERE start_date < "
        get_data_query = f"SELECT * FROM data"
        with self.connection.cursor() as cursor:
            cursor.execute(get_data_query)
            result = cursor.fetchall()


            return self._format_info()
            
            # TODO send result to gui for population

    def _format_info(self):
        """
        Takes a list of lists and formats them accordingly then returns a list of lists
        """
        
        pass

db = Db()