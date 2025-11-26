from config.database import Database
from models.employee import Employee


class EmployeeController:
    def __init__(self, db: Database):
        self.db = db

    def register_employee(self):
        print("\n--- Registrar Empleado ---")
        name = input("Nombre: ")
        email = input("Correo: ")
        phone = input("Teléfono: ")
        address = input("Dirección: ")
        contract_date = input("Fecha inicio contrato (YYYY-MM-DD): ")
        salary_input = input("Salario: ")
        salary = float(salary_input) if salary_input else None
        contract_start = contract_date if contract_date else None

        employee = Employee(
            name=name,
            email=email,
            phone_number=phone,
            address=address,
            contract_start_date=contract_start,
            salary=salary,
        )
        employee_id = employee.create_employee(self.db)
        if employee_id:
            print(f"Empleado creado con id {employee_id}")
            return employee_id
        print("No se pudo crear el empleado")
        return None

    def list_employees(self):
        print("\n--- Empleados ---")
        rows = Employee.list_employees(self.db)
        for row in rows:
            print(row)
        return rows

    def delete_employee(self):
        emp_id = input("ID a eliminar: ")
        if not emp_id.isdigit():
            print("ID inválido")
            return
        Employee.delete_employee(self.db, int(emp_id))
        print("Empleado eliminado.")

    def assign_department(self):
        emp_id = input("ID empleado: ")
        dept_id = input("ID departamento: ")
        if emp_id.isdigit() and dept_id.isdigit():
            Employee.assign_department(self.db, int(emp_id), int(dept_id))
            print("Departamento asignado.")
        else:
            print("IDs inválidos.")

    def assign_project(self):
        emp_id = input("ID empleado: ")
        proj_id = input("ID proyecto: ")
        if emp_id.isdigit() and proj_id.isdigit():
            Employee.assign_project(self.db, int(emp_id), int(proj_id))
            print("Proyecto asignado.")
        else:
            print("IDs inválidos.")

    def unassign_project(self):
        emp_id = input("ID empleado: ")
        proj_id = input("ID proyecto: ")
        if emp_id.isdigit() and proj_id.isdigit():
            Employee.unassign_project(self.db, int(emp_id), int(proj_id))
            print("Proyecto removido.")
        else:
            print("IDs inválidos.")
