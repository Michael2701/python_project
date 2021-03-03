from App.Models.DB import DB

class UserModel(DB):


    def get_all_users(self):
        users = []

        try:
            cursor = self.get_cursor()
            cursor.execute("SELECT rowid, * FROM users")
            self.connection.commit()
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
            self.connection.commit()
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
            self.connection.commit()

        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return rows_count

    def create_user(self, data):
        rows_count = 0

        try:
            cursor = self.get_cursor()
            rows_count = cursor.execute("""
                INSERT INTO users (first_name, last_name, user_role, email, password)
                VALUES (:first_name , :last_name,:user_role, :email, :password)
            """, data).rowcount
            self.connection.commit()

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
            self.connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
            return rows_count




