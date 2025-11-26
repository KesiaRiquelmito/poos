from models.department import Department
from models.employee import Employee
from models.project import Project
from models.report import Report
from models.shift import Shift
from models.user import User


class Administrator(User):
    def __init__(self, username: str, password_hash: str, role: str = None):
        super().__init__(username, password_hash, role)

    def _is_admin(self, db):
        user = User.authenticate(db, self.username, self.password_hash)
        if not user or user.get_user_role() != "admin":
            print("Autenticación fallida o no tienes permisos de administrador.")
            return False
        return True

    def generate_employee_report(self, db):
        if not self._is_admin(db):
            return
        rows = Employee.list_employees(db)
        headers = [
            "ID", "Nombre", "Email", "Telefono", "Direccion",
            "Fecha contrato", "Salario", "Id departamento"
        ]
        report = Report("Reporte empleados")
        print(report.render_text(rows, headers))

    def generate_project_report(self, db):
        if not self._is_admin(db):
            return
        rows = Project.list_projects(db)
        headers = ["ID", "Nombre", "Descripcion", "Fecha Inicio"]
        report = Report("Reporte Proyectos")
        print(report.render_text(rows, headers))

    def generate_department_report(self, db):
        if not self._is_admin(db):
            return
        rows = Department.list_departments(db)
        headers = ["ID", "Departmento", "Manager ID", "Nombre manager"]
        report = Report("Reporte Departamento")
        print(report.render_text(rows, headers))

    def generate_shift_report(self, db):
        if not self._is_admin(db):
            return
        rows = Shift.list_shifts(db)
        headers = ["ID", "Empleado", "Proyecto", "Fecha", "Horas trabajadas", "Tareas"]
        report = Report("Reporte turnos")
        print(report.render_text(rows, headers))

    def register_employee(self, employee: Employee, db, password: str):
        if not self._is_admin(db):
            return
        return employee.create_employee(db)
