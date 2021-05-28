from App.Models.SimpleUser import SimpleUser
from App.Services.Encoder import Encoder


class UsersMigration:
    def __init__(self):
        """
        create users table and insert one admin user
        """
        self.create_users_table()
        self.insert_dummy_user()

    def create_users_table(self) -> None:
        """
        create users table
        :return: None
        """
        try:
            SimpleUser.createTable()

        except Exception as e:
            print(str(e))

    def insert_dummy_user(self) -> None:
        """
        insert one admin user
        :return: None
        """
        try:
            # SimpleUser._connection.debug = True
            password = Encoder.encrypt_password("123")
            SimpleUser(first_name="Super", last_name="Admin", email="email", user_role="admin", password=password)
        except Exception as e:
            print(str(e))
