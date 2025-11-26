from models.security import Security
from models.user import User


class UserController:
    def __init__(self, db):
        self.db = db

    def create_user(self):
        cleaned_username = Security.clean_text(input("Ingresa el usuario: "))
        password_hash = Security.clean_text(input("Ingresa la contraseña: "))
        role = Security.clean_text(input("Ingresa el rol (admin/user/manager): "))
        if role not in ["admin", "user", "manager"]:
            print("Rol inválido. Usando 'user' por defecto.")
            role = "user"
        user = User(cleaned_username, password_hash, role=role)
        return user.create_user(self.db, password_hash)
