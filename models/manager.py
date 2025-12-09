from models.user import User

class Manager(User):
    def __init__(self, username: str, password_hash: str, role="manager"):
        super().__init__(username, password_hash, role)

    def is_manager(self):
        return True
