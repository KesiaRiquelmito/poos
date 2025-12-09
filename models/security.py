import bcrypt

class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(14))
        return hashed.decode("utf-8")

    @staticmethod
    def check_password(password: str, stored_hash: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))

    @staticmethod
    def clean_text(value: str) -> str:
        if value is None:
            return ""
        return value.strip()
