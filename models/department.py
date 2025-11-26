from config.database import Database
from models.employee import Employee
from models.security import Security


class Department:
    def __init__(self, name: str, manager_id: int, department_id: int = None):
        self.name = Security.clean_text(name)
        self.manager_id = manager_id
        self.department_id = department_id

    def create_department(self, db: Database):
        try:
            cursor = db.execute(
                "INSERT INTO departments (name, manager_employee_id) VALUES (%s, %s)",
                (self.name, self.manager_id),
            )
            self.department_id = cursor.lastrowid
            return self.department_id
        except Exception as exc:
            print(f"Error creando departamento: {exc}")

    @staticmethod
    def update_department(db: Database, department_id: int, new_name: str, manager_id: int):
        db.execute(
            "UPDATE departments SET name = %s, manager_employee_id = %s WHERE id = %s",
            (Security.clean_text(new_name), manager_id, department_id),
        )

    @staticmethod
    def delete_department(db: Database, department_id: int):
        db.execute("DELETE FROM departments WHERE id = %s", (department_id,))

    @staticmethod
    def list_departments(db: Database):
        return db.fetch_all(
            """
            SELECT d.id, d.name, d.manager_employee_id, e.name
            FROM departments d
                     LEFT JOIN employees e ON d.manager_employee_id = e.id
            ORDER BY d.id
            """,
            (),
        )

    def assign_manager(self, employee: Employee):
        self.manager_id = employee.employee_id
