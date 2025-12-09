from models.user import User

class Administrator(User):
    def __init__(self, username: str, password_hash: str, role="admin"):
        super().__init__(username, password_hash, role)

    def is_admin(self):
        return True
