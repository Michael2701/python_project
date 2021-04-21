from passlib.context import CryptContext


class Encoder:

    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    ) 

    @classmethod
    def encrypt_password(cls, password: str) -> str:
        return cls.pwd_context.encrypt(password)

    @classmethod
    def check_encrypted_password(cls, password: str, hashed: str) -> bool:
        return cls.pwd_context.verify(password, hashed)

