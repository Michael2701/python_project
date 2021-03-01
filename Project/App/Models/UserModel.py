from App.Models.DB import DB

class UserModel(DB):


    def get_all_users(self):
        users = []

        try:
            cursor = self.get_cursor()
            cursor.execute("SELECT rowid, * FROM users")
            users = cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return users


    def get_user_by_id(self, id):
        user = {}

        try:
            cursor = self.get_cursor()
            cursor.execute("SELECT rowid, * FROM users WHERE rowid=?", str(id))
            user = cursor.fetchone()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return user

    def update_user_by_id(self, data):
        rows_count = 0

        try:
            cursor = self.get_cursor()
            rows_count = cursor.execute("""
                UPDATE users SET 
                    first_name=:first_name,
                    last_name=:last_name,
                    user_role=:user_role,
                    email=:email
                WHERE rowid=:rowid
            """, data).rowcount

        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return rows_count

    def delete_user_by_id(self, id):
        rows_count = 0

        try:
            cursor = self.get_cursor()
            rows_count = cursor.execute("DELETE FROM users WHERE rowid=?", str(id)).rowcount
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return rows_count




