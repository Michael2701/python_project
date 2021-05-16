from cryptography.fernet import Fernet
from typing import Union
from os import path


class FileEncryptor:

    def __init__(self, file_path: str = None):
        self.storage_path = "App/Storage/"
        self.filekey_name = "filekey.key"

        if file_path is None:
            self.session_file = 'session.csv'
        else:
            self.session_file = file_path

        self.filekey_path = f"{self.storage_path}{self.filekey_name}"
        self.session_file_path = f"{self.storage_path}{self.session_file}"

        self.create_filekey()

    def create_filekey(self) -> None:
        """
        create new encoding key if not exists
        in Storage/file.key
        :return: void
        """
        if not path.exists(self.filekey_path) and not path.isfile(self.filekey_path):
            key = Fernet.generate_key()
            with open(self.filekey_path, 'wb') as filekey:
                filekey.write(key)

    def encrypt_file(self) -> None:
        """
        encrypt given csv file
        :return: void
        """
        with open(self.filekey_path, 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(self.session_file_path, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(self.session_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt_file(self):
        """
        decrypt given csv file
        :return: void
        """
        with open(self.filekey_path, 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(self.session_file_path, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(self.session_file_path, 'wb') as dec_file:
            dec_file.write(decrypted)
