import hashlib


class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def clean_text(value: str) -> str:
        if value is None:
            return ""
        return value.strip()
