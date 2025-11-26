from config.database import Database
from models.security import Security


class Employee:
    def __init__(
            self,
            name: str,
            email: str,
            phone_number: str,
            address: str,
            contract_start_date: str,
            salary=None,
            department_id=None,
            employee_id=None,
    ):
        self.employee_id = employee_id
        self.name = Security.clean_text(name)
        self.email = Security.clean_text(email)
        self.phone_number = Security.clean_text(phone_number)
        self.address = Security.clean_text(address)
        self.contract_start_date = contract_start_date
        self.salary = salary
        self.department_id = department_id

    def create_employee(self, db: Database):
        try:
            cursor = db.execute(
                "INSERT INTO employees (name, email, phone_number, address, contract_start_date, salary, department_id) VALUES (%s,%s,%s,%s, %s, %s, %s)",
                (
                    self.name, self.email, self.phone_number, self.address,
                    str(self.contract_start_date) if self.contract_start_date else None,
                    self.salary,
                    self.department_id,
                ),
            )
            self.employee_id = cursor.lastrowid
            return self.employee_id
        except Exception as exc:
            print(f"Error creando empleado: {exc}")

    @staticmethod
    def list_employees(db: Database):
        return db.fetch_all(
            """
            SELECT id,
                   name,
                   email,
                   phone_number,
                   address,
                   contract_start_date,
                   salary,
                department_id
            FROM employees
            """,
            (),
        )

    @staticmethod
    def delete_employee(db: Database, employee_id: int):
        db.execute("DELETE FROM employees WHERE id = %s", (employee_id,))

    @staticmethod
    def assign_department(db: Database, employee_id: int, department_id: int):
        db.execute("UPDATE employees SET department_id = %s WHERE id = %s", (department_id, employee_id))

    @staticmethod
    def assign_project(db: Database, employee_id: int, project_id: int):
        try:
            db.execute(
                "INSERT IGNORE INTO employee_projects (employee_id, project_id) VALUES (%s,%s)",
                (employee_id, project_id),
            )
        except Exception as exc:
            print(f"Error asignando proyecto: {exc}")

    @staticmethod
    def unassign_project(db: Database, employee_id: int, project_id: int):
        db.execute(
            "DELETE FROM employee_projects WHERE employee_id = %s AND project_id = %s",
            (employee_id, project_id),
        )

    @staticmethod
    def list_projects(db: Database, employee_id: int):
        return db.fetch_all(
            """
            SELECT p.id, p.name, p.description
            FROM projects p
                     JOIN employee_projects ep ON p.id = ep.project_id
            WHERE ep.employee_id = %s
            """,
            (employee_id,),
        )
