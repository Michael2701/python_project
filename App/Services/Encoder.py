from passlib.context import CryptContext


class Encoder:

    """
    password encoding definition
    """
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    ) 

    @classmethod
    def encrypt_password(cls, password: str) -> str:
        """
        encrypt given password
        :param password: string to encrypt
        :return: encrypted password
        """
        return cls.pwd_context.encrypt(password)

    @classmethod
    def check_password(cls, password: str, hashed: str) -> bool:
        """
        check given and encrypted passwords for match
        :param password: string password to check
        :param hashed: string hashed password from DB
        :return: True if passwords match and False otherwise
        """
        return cls.pwd_context.verify(password, hashed)

