from config.database import Database
from models.security import Security


class Project:
    def __init__(self, name: str, description: str, start_date: str = None, project_id: int = None):
        self.name = Security.clean_text(name)
        self.description = Security.clean_text(description)
        self.start_date = start_date
        self.project_id = project_id

    def create_project(self, db: Database):
        try:
            cursor = db.execute(
                "INSERT INTO projects (name, description, start_date) VALUES (%s,%s,%s)",
                (self.name, self.description, self.start_date),
            )
            self.project_id = cursor.lastrowid
            return self.project_id
        except Exception as exc:
            print(f"Error creando proyecto: {exc}")

    @staticmethod
    def edit_project(db: Database, project_id: int, name: str, description: str, start_date: str):
        db.execute(
            "UPDATE projects SET name = %s, description = %s, start_date = %s WHERE id = %s",
            (Security.clean_text(name), Security.clean_text(description), start_date, project_id),
        )

    @staticmethod
    def delete_project(db: Database, project_id: int):
        db.execute("DELETE FROM projects WHERE id = %s", (project_id,))

    @staticmethod
    def list_projects(db: Database):
        return db.fetch_all("SELECT id, name, description, start_date FROM projects", ())
