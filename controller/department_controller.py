from config.database import Database
from models.department import Department


class DepartmentController:
    def __init__(self, db: Database):
        self.db = db

    def create_department(self):
        print("\n--- Crear Departamento ---")
        name = input("Nombre: ")
        manager_id = input("ID del gerente (puede ser vacío): ")
        manager = int(manager_id) if manager_id.isdigit() else None
        dept = Department(name=name, manager_id=manager)
        dept_id = dept.create_department(self.db)
        if dept_id:
            print(f"Departamento creado con id {dept_id}")
            return dept_id
        print("No se pudo crear el departamento")
        return None

    def list_departments(self):
        print("\n--- Departamentos ---")
        rows = Department.list_departments(self.db)
        for row in rows:
            print(row)

    def edit_department(self):
        dept_id = input("ID a editar: ")
        if not dept_id.isdigit():
            print("ID inválido")
            return
        new_name = input("Nuevo nombre: ")
        manager_id = input("Nuevo ID de gerente: ")
        manager = int(manager_id) if manager_id.isdigit() else None
        Department.update_department(self.db, int(dept_id), new_name, manager)
        print("Departamento actualizado.")

    def delete_department(self):
        dept_id = input("ID a eliminar: ")
        if not dept_id.isdigit():
            print("ID inválido")
            return
        Department.delete_department(self.db, int(dept_id))
        print("Departamento eliminado.")
