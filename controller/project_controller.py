from config.database import Database
from models.project import Project


class ProjectController:
    def __init__(self, db: Database):
        self.db = db

    def create_project(self):
        print("\n--- Crear Proyecto ---")
        name = input("Nombre: ")
        description = input("Descripción: ")
        start_date = input("Fecha inicio (YYYY-MM-DD): ")
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
        proj_id = input("ID a editar: ")
        if not proj_id.isdigit():
            print("ID inválido")
            return
        name = input("Nuevo nombre: ")
        description = input("Nueva descripción: ")
        start_date = input("Nueva fecha inicio (YYYY-MM-DD): ")
        Project.edit_project(self.db, int(proj_id), name, description, start_date)
        print("Proyecto actualizado.")

    def delete_project(self):
        proj_id = input("ID a eliminar: ")
        if not proj_id.isdigit():
            print("ID inválido")
            return
        Project.delete_project(self.db, int(proj_id))
        print("Proyecto eliminado.")
