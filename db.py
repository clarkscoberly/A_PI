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


# user = root
# pass = Concat_@nine30
# host = d
def connect_db():
    try:
        with connect(
            host= "127.0.0.1",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        ) as connection:
            print(connection)

    except Error as e:
        print(e)

def create_table():
    create_movies_table_query = """
    CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        connection.commit()

def update_table(formatted_data):
    """
    Get formatted information and then send it to the database.
    """

    update_to_send = formatted_data

    pass

def get_information():
    pass

def send_info():
    """
    Takes information from get_information and prepares it to be sent to GUI
    """
    pass

def format_info():
    """
    Takes a list of lists and formats them accordingly then returns a list of lists
    """
    pass

connect_db()