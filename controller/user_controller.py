from config.database import Database
from models.security import Security
from models.user import User
import pwinput


class UserController:
    def __init__(self, db, current_user):
        self.db = db
        self.current_user = current_user

    def create_user(self):
        rows = self.db.fetch_all("SELECT COUNT(*) FROM users", ())
        is_empty = rows[0][0] == 0

        cleaned_username = Security.clean_text(input("Ingresa el usuario: "))
        if not cleaned_username:
            print("El nombre de usuario no puede estar vacío.")
            return
        password = pwinput.pwinput("Ingresa la contraseña: ", mask="*")
        if len(password) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            return
        role = Security.clean_text(input("Ingresa el rol (admin/user/manager): "))
        if role not in ["admin", "user", "manager"]:
            print("Rol inválido. Usando 'user' por defecto.")
            role = "user"
        if is_empty:
            if role != "admin":
                print("El primer usuario del sistema DEBE ser administrador.")
                return
            user = User(cleaned_username, password, role=role)
            return user.create_user(self.db, password)

        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden crear usuarios.")
            return
        user = User(cleaned_username, password, role=role)
        return user.create_user(self.db, password)

    @staticmethod
    def login(db: Database, username: str, password: str):
        user = User.authenticate(db, username, password)
        if not user:
            print("Autenticación fallida. Usuario o contraseña incorrectos.")
            return None
        print(f"Bienvenido, {user.username}! Rol: {user.role}")
        return user