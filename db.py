from getpass import getpass
from mysql.connector import connect, Error
import scapy.all as scapy
import argparse
from datetime import date

# The following are the locations of where to store the data and where the data is within a list to be
# Pulled back out
IP = 0
MAC_ADDRESS = 1
MANUFACTERER = 2
OS = 3
FIRMWARE = 4
DATE_AND_TIME = 5


# user = A_PI
# pass = T3@ms_AP1
# host = 0.0.0.0:5555

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

    def update_table(self, data):
        """
        Get formatted information and then send it to the database.
        """
        
        formatted_data = self.format_data(data)

        update_to_send = formatted_data
        insert_data_query = """
        INSERT INTO data
        (ip, mac, manufacterer, os, firmware, start_time, end_time)
        VALUES ( %s, %s, %s, %s, %s, %s )
        """

        ###########################################################################################################
        # The following is an example of the kind of formatted data that should be contained within formatted data.
        #
        # reviewers_records = [
        #     ("Chaitanya", "Baweja"),
        #     ("Mary", "Cooper"),
        #     ("John", "Wayne"),
        #     ("Thomas", "Stoneman")
        # ]
        #
        ###########################################################################################################

        with self.connection.cursor() as cursor:
            cursor.executemany(insert_data_query, formatted_data)
            self.connection.commit()

    def format_data(self):
        """
        Format data retrieved by scanner to be put into
        """
        pass

    # def get_information(self, data): # TODO DATA IS NOT WRITTEN YET
    #     """
    #     Gets info from the scanner or from main after the data is no longer in .csv form 
    #     """
    #     self.send_info(data)
    #     pass

    # TODO get query Selection

    def populate_information(self, query_selection):
        """
        Prepares info from a query, returns result to GUI
        """
        current_date = date.today()

        # TODO THIS MIGHT ALSO SELECT THE AUTOINCREMENT KEY IN WHICH CASE ALL THE NUMS ARE WRONG
        # where date(created_at) = CURDATE() - interval 7 day | <?
        get_data_query = f"SELECT * FROM data WHERE start_date = {current_date} - interval {query_selection} day"
        with self.connection.cursor() as cursor:
            cursor.execute(get_data_query)
            result = cursor.fetchall()

            return result

db = Db()