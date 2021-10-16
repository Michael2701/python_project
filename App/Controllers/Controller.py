from typing import Any
from App.Services.FileEncryptor import FileEncryptor
from App.Services.FileHelper import FileHelper


class Controller:
    user = None

    @staticmethod
    def clear_view(view: Any) -> None:
        """
        clear view from it's child elements
        :param view:
        :return:
        """
        master_children = view.winfo_children()
        if len(master_children) > 0:
            for child in master_children:
                child.destroy()

    def get_logged_user(self) -> dict:
        user = {}
        try:
            FileEncryptor("session.csv").decrypt_file()
            user = FileHelper.read_csv("App/Storage/session.csv")[0]
            FileEncryptor("session.csv").encrypt_file()

        except Exception as e:
            print(e)
        finally:
            self.user = user
            return user

    @staticmethod
    def print_list(rows):
        for row in rows:
            print(row)
