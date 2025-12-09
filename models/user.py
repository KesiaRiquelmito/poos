from config.database import Database
from models.security import Security


class User:
    def __init__(self, username: str = None, password_hash: str = None, role: str = "user"):
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def is_admin(self):
        return False

    def is_manager(self):
        return False

    def create_user(self, db: Database, password_hash: str):
        try:
            hashed = Security.hash_password(password_hash)
            cursor = db.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (%s,%s,%s)",
                (self.username, hashed, self.role),
            )
            print("Usuario creado exitosamente")
            return cursor.lastrowid
        except Exception as exc:
            print(f"Error creando usuario: {exc}")

    @staticmethod
    def authenticate(db: Database, username: str, password: str):
        from models.administrator import Administrator
        from models.manager import Manager

        try:
            rows = db.fetch_all(
                "SELECT id, username, password_hash, role FROM users WHERE username = %s",
                (username,),
            )
            if not rows:
                return None

            user_id, uname, saved_hash, role = rows[0]

            if not Security.check_password(password, saved_hash):
                return None

            if role == "admin":
                return Administrator(uname, saved_hash, role="admin")

            if role == "manager":
                return Manager(uname, saved_hash, role="manager")

            return User(uname, saved_hash, role)

        except Exception as exc:
            print(f"Error de autenticación: {exc}")
            return None
