import sqlite3 

from sqlite3 import Error


def create_connection(db_file):
    connx = None
    try:
        connx = sqlite3.connect(db_file)
        return connx        
    except Error as e:
        print(e)
    return connx


if __name__ == '__main__':
    cnnx = create_connection("dbfile.db")