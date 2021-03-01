import sqlite3

class DB:
    
    def __init__(self, make_insert=False):
        self.connection = None

        self.create_connection_if_not_exists()
        self.create_users_table()
        
        if make_insert:
            self.insert_dummy_user()

    def create_users_table(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                CREATE TABLE users (
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    email text UNIQUE NOT NULL,
                    password text NOT NULL,
                    user_role text NOT NULL
                )
            """)
            connection.commit()
            print("Users table created")
        except Exception as e:
            print(str(e))
        
    def insert_dummy_user(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO users VALUES ('Petr', 'Zalupkin', 'test2@test.com', '1233', 'huy')")
            connection.commit()
            print("Dummy user inserted")
        except Exception as e:
            print(str(e))

    def get_connection(self):
        self.create_connection_if_not_exists()
        return self.connection

    def get_cursor(self):
        self.create_connection_if_not_exists()
        return self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.connection = None

    def create_connection_if_not_exists(self):
        if self.connection is None:
            self.connection = sqlite3.connect('App/DB/project.db')


