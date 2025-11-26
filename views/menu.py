from config.database import Database
from controller.department_controller import DepartmentController
from controller.employee_controller import EmployeeController
from controller.project_controller import ProjectController
from controller.shift_controller import ShiftController
from controller.user_controller import UserController
from controller.report_controller import ReportController


class Menu:
    def __init__(self):
        self.db = Database()
        self.employee_controller = EmployeeController(self.db)
        self.department_controller = DepartmentController(self.db)
        self.project_controller = ProjectController(self.db)
        self.shift_controller = ShiftController(self.db)
        self.user_controller = UserController(self.db)
        self.report_controller = ReportController(self.db)

    def start(self):
        print("Bienvenido al Sistema de Gestión de Empleados (EcoTech Solutions)")
        while True:
            option = self.main_menu()
            if option == "1":
                self.employee_menu()
            elif option == "2":
                self.department_menu()
            elif option == "3":
                self.project_menu()
            elif option == "4":
                self.shift_menu()
            elif option == "5":
                self.report_menu()
            elif option == "6":
                self.user_menu()
            elif option == "0":
                print("Saliendo...")
                self.db.disconnect_database()
                break
            else:
                print("Opción no válida")

    def user_menu(self):
        print(
            "\nUsuarios\n"
            "1. Crear Usuario\n"
            "2. Listar Usuarios\n"
            "3. Eliminar Usuario\n"
            "0. Volver"
        )
        option = input("Opción: ")
        if option == "1":
            self.user_controller.create_user()

    def main_menu(self):
        print(
            "\nMenú Principal\n"
            "1. Empleados\n"
            "2. Departamentos\n"
            "3. Proyectos\n"
            "4. Registro de tiempo\n"
            "5. Reportes\n"
            "6. Usuarios\n"
            "0. Salir"
        )
        return input("Opción: ")

    def employee_menu(self):
        print(
            "\nEmpleados\n"
            "1. Crear\n"
            "2. Listar\n"
            "3. Eliminar\n"
            "4. Asignar a departamento\n"
            "5. Asignar a proyecto\n"
            "6. Quitar de proyecto\n"
            "0. Volver"
        )
        option = input("Opción: ")
        if option == "1":
            self.employee_controller.register_employee()
        elif option == "2":
            self.employee_controller.list_employees()
        elif option == "3":
            self.employee_controller.delete_employee()
        elif option == "4":
            self.employee_controller.assign_department()
        elif option == "5":
            self.employee_controller.assign_project()
        elif option == "6":
            self.employee_controller.unassign_project()

    def department_menu(self):
        print(
            "\nDepartamentos\n"
            "1. Crear\n"
            "2. Listar\n"
            "3. Editar\n"
            "4. Eliminar\n"
            "0. Volver"
        )
        option = input("Opción: ")
        if option == "1":
            self.department_controller.create_department()
        elif option == "2":
            self.department_controller.list_departments()
        elif option == "3":
            self.department_controller.edit_department()
        elif option == "4":
            self.department_controller.delete_department()

    def project_menu(self):
        print(
            "\nProyectos\n"
            "1. Crear\n"
            "2. Listar\n"
            "3. Editar\n"
            "4. Eliminar\n"
            "0. Volver"
        )
        option = input("Opción: ")
        if option == "1":
            self.project_controller.create_project()
        elif option == "2":
            self.project_controller.list_projects()
        elif option == "3":
            self.project_controller.edit_project()
        elif option == "4":
            self.project_controller.delete_project()

    def shift_menu(self):
        print(
            "\nRegistro de tiempo\n"
            "1. Registrar horas\n"
            "2. Listar horas\n"
            "0. Volver"
        )
        option = input("Opción: ")
        if option == "1":
            self.shift_controller.log_shift()
        elif option == "2":
            self.shift_controller.list_shifts()

    def report_menu(self):
        print(
            "\nReportes\n"
            "1. Empleados\n"
            "2. Departmentos\n"
            "3. Proyectos\n"
            "4. Turnos\n"
            "0. Volver"
        )
        option = input("Opción: ")

        if option == "1":
            self.report_controller.generate_employee_report()
        elif option == "2":
            self.report_controller.generate_department_report()
        elif option == "3":
            self.report_controller.generate_project_report()
        elif option == "4":
            self.report_controller.generate_shift_report()
