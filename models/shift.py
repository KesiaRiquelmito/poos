from datetime import date

from config.database import Database
from models.security import Security


class Shift:
    def __init__(
            self,
            worked_hours: int,
            shift_date: date,
            task_description: str,
            employee_id: int,
            project_id: int,
            shift_id: int = None,
    ):
        self.worked_hours = worked_hours
        self.shift_date = shift_date
        self.task_description = Security.clean_text(task_description)
        self.employee_id = employee_id
        self.project_id = project_id
        self.shift_id = shift_id

    def log_worked_hours(self, db: Database):
        try:
            cursor = db.execute(
                """
                INSERT INTO shifts (employee_id, project_id, shift_date, worked_hours, task_description)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.employee_id, self.project_id, str(self.shift_date), self.worked_hours, self.task_description),
            )
            self.shift_id = cursor.lastrowid
            return self.shift_id
        except Exception as exc:
            print(f"Error guardando registro de tiempo: {exc}")

    @staticmethod
    def list_shifts(db: Database):
        return db.fetch_all(
            """
            SELECT s.id, e.name, pr.name, s.shift_date, s.worked_hours, s.task_description
            FROM shifts s
                     JOIN employees e ON s.employee_id = e.id
                     JOIN projects pr ON s.project_id = pr.id
            ORDER BY s.shift_date DESC
            """,
            (),
        )
