import sqlite3
from sqlite3 import Error


class SQLiteConnector:

    @staticmethod
    def create_connection():
        """
        create a database connection to the SQLite database
        specified by the db_file
        :return: Connection object or None
        """
        connection_string = 'App/DB/project.db'
        conn = None
        try:
            conn = sqlite3.connect(connection_string)
        except Error as e:
            print(e)

        return conn
