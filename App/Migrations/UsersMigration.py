from App.Models.SimpleUser import SimpleUser

class UsersMigration():
    def __init__(self):
        super().__init__()
        self.create_users_table()
        self.insert_dummy_user()

    def create_users_table(self):
        try:
            SimpleUser.createTable()
        
        except Exception as e:
            print(str(e))

    def insert_dummy_user(self):
        try:
            SimpleUser._connection.debug = True
            person = SimpleUser(first_name="Foo",last_name="Kuku",email="t@t.com",user_role="admin", password="123")
        except Exception as e:
            print(str(e))