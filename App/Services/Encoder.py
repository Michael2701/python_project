from passlib.context import CryptContext


class Encoder:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        ) 

    def encrypt_password(self, password: str) -> str:
        return self.pwd_context.encrypt(password)

    def check_encrypted_password(self, password: str, hashed: str) -> bool:
        return self.pwd_context.verify(password, hashed)
