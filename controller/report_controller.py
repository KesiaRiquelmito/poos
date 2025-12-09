from models.department import Department
from models.employee import Employee
from models.project import Project
from models.report import Report
from models.shift import Shift


class ReportController:
    def __init__(self, db, current_user):
        self.db = db
        self.current_user = current_user

    def generate_employee_report(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden generar reportes.")
            return
        rows = Employee.list_employees(self.db)
        headers = [
            "ID", "Nombre", "Email", "Telefono", "Direccion",
            "Fecha contrato", "Salario", "Id departamento"
        ]
        report = Report("Reporte empleados")
        print(report.render_text(rows, headers))

    def generate_project_report(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden generar reportes.")
            return
        rows = Project.list_projects(self.db)
        headers = ["ID", "Nombre", "Descripcion", "Fecha Inicio"]
        report = Report("Reporte Proyectos")
        print(report.render_text(rows, headers))

    def generate_department_report(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden generar reportes.")
            return
        rows = Department.list_departments(self.db)
        headers = ["ID", "Departmento", "Manager ID", "Nombre manager"]
        report = Report("Reporte Departamento")
        print(report.render_text(rows, headers))

    def generate_shift_report(self):
        if not self.current_user.is_admin:
            print("Acceso denegado. Solo administradores pueden generar reportes.")
            return
        rows = Shift.list_shifts(self.db)
        headers = ["ID", "Empleado", "Proyecto", "Fecha", "Horas trabajadas", "Tareas"]
        report = Report("Reporte turnos")
        print(report.render_text(rows, headers))
