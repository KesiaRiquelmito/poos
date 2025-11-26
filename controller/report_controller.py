from models.administrator import Administrator
from models.security import Security


class ReportController:
    def __init__(self, db):
        self.db = db

    def _get_credentials(self):
        username = Security.clean_text(input("Ingresa tu usuario de administrador: "))
        password = Security.clean_text(input("Ingresa tu contraseña de administrador: "))
        return username, password

    def generate_employee_report(self):
        print("\n--- Reporte de Empleados ---")
        username, password = self._get_credentials()
        admin = Administrator(username, password)
        admin.generate_employee_report(self.db)

    def generate_project_report(self):
        print("\n--- Reporte de Proyectos ---")
        username, password = self._get_credentials()
        admin = Administrator(username, password)
        admin.generate_project_report(self.db)

    def generate_department_report(self):
        print("\n--- Reporte de Departamentos ---")
        username, password = self._get_credentials()
        admin = Administrator(username, password)
        admin.generate_department_report(self.db)

    def generate_shift_report(self):
        print("\n--- Reporte de Turnos ---")
        username, password = self._get_credentials()
        admin = Administrator(username, password)
        admin.generate_shift_report(self.db)
