""" This class encrypt and decrypt csv file with password of current logged user. """

from cryptography.fernet import Fernet
from os import path


class FileEncryptor:

    def __init__(self, file_path: str = None):
        self.storage_path = "App/Storage/"
        self.file_key_name = "filekey.key"

        if file_path is None:
            self.session_file = 'session.csv'
        else:
            self.session_file = file_path

        self.file_key_path = f"{self.storage_path}{self.file_key_name}"
        self.session_file_path = f"{self.storage_path}{self.session_file}"

        self.create_file_key()

    def create_file_key(self) -> None:
        """
        create new encoding key if not exists
        in Storage/file.key
        :return: void
        """
        if not path.exists(self.file_key_path) and not path.isfile(self.file_key_path):
            key = Fernet.generate_key()
            with open(self.file_key_path, 'wb') as file_key:
                file_key.write(key)

    def encrypt_file(self) -> None:
        """
        encrypt given csv file
        :return: void
        """
        with open(self.file_key_path, 'rb') as file_key:
            key = file_key.read()

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
        with open(self.file_key_path, 'rb') as file_key:
            key = file_key.read()

        fernet = Fernet(key)

        with open(self.session_file_path, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(self.session_file_path, 'wb') as dec_file:
            dec_file.write(decrypted)
