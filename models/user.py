from config.database import Database
from models.security import Security


class User:
    def __init__(self, username: str = None, password_hash: str = None, role: str = "user"):
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def create_user(self, db: Database, password: str):
        try:
            hashed = Security.hash_password(password)
            cursor = db.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (%s,%s,%s)",
                (self.username, hashed, self.role),
            )
            return cursor.lastrowid
        except Exception as exc:
            print(f"Error creando usuario: {exc}")

    @staticmethod
    def authenticate(db: Database, username: str, password: str):
        try:
            rows = db.fetch_all(
                "SELECT id, username, password_hash, role FROM users WHERE username = %s",
                (username,),
            )
            if not rows:
                return None

            user_id, uname, saved_hash, role = rows[0]

            if Security.hash_password(password) == saved_hash:
                return User(uname, saved_hash, role)

            return None
        except Exception as exc:
            print(f"Error de autenticación: {exc}")
            return None

    def get_user_role(self):
        return self.role
