from config.database import Database
from models.project import Project


class ProjectController:
    def __init__(self, db: Database, current_user):
        self.db = db
        self.current_user = current_user

    def create_project(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden crear proyectos.")
            return None
        print("\n--- Crear Proyecto ---")
        name = input("Nombre: ")
        if not name:
            print("El nombre no puede estar vacío")
            return None
        description = input("Descripción: ")
        if not description:
            print("La descripción no puede estar vacía")
            return None
        start_date = input("Fecha inicio (YYYY-MM-DD): ")
        if not start_date:
            print("La fecha de inicio no puede estar vacía")
            return None
        project = Project(name=name, description=description, start_date=start_date)
        project_id = project.create_project(self.db)
        if project_id:
            print(f"Proyecto creado con id {project_id}")
            return project_id
        print("No se pudo crear el proyecto")
        return None

    def list_projects(self):
        print("\n--- Proyectos ---")
        rows = Project.list_projects(self.db)
        for row in rows:
            print(row)

    def edit_project(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden editar proyectos.")
            return
        proj_id = input("ID a editar: ")
        if not proj_id.isdigit():
            print("ID inválido")
            return
        name = input("Nuevo nombre: ")
        if not name:
            print("El nombre no puede estar vacío")
            return
        description = input("Nueva descripción: ")
        if not description:
            print("La descripción no puede estar vacía")
            return
        start_date = input("Nueva fecha inicio (YYYY-MM-DD): ")
        if not start_date:
            print("La fecha de inicio no puede estar vacía")
            return
        Project.edit_project(self.db, int(proj_id), name, description, start_date)
        print("Proyecto actualizado.")

    def delete_project(self):
        if not self.current_user.is_admin():
            print("Acceso denegado. Solo administradores pueden eliminar proyectos.")
            return
        proj_id = input("ID a eliminar: ")
        if not proj_id.isdigit():
            print("ID inválido")
            return
        Project.delete_project(self.db, int(proj_id))
        print("Proyecto eliminado.")
