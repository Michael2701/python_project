""" File create connection with data base. """

import sqlite3
from sqlite3 import Error


class SQLiteConnector:

    @staticmethod
    def create_connection(db_path="App/DB/project.db"):
        """
        create a database connection to the SQLite database
        specified by the db_file
        :return: Connection object or None
        """

        conn = None
        try:
            conn = sqlite3.connect(db_path)
        except Error as e:
            print(e)
        finally:
            return conn
