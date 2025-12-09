from datetime import datetime

from config.database import Database
from models.security import Security
from models.shift import Shift


class ShiftController:
    def __init__(self, db: Database, current_user):
        self.db = db
        self.current_user = current_user

    def log_shift(self):
        print("\n--- Registrar Horas ---")
        if self.current_user.is_admin() or self.current_user.is_manager():
            emp_id = Security.clean_text(input("ID empleado: "))
        else:
            print("Solo puedes registrar tus propias horas.")
            emp_id = Security.clean_text(input("Ingresa tu ID de empleado: "))

        if not emp_id:
            print("El ID de empleado es obligatorio.")
            return
        proj_id = input("ID proyecto: ")
        date_str = input("Fecha (YYYY-MM-DD): ")
        hours = input("Horas trabajadas: ")
        task = input("Descripción corta: ")

        if not emp_id.isdigit() or not proj_id.isdigit() or not hours.isdigit():
            print("Datos inválidos.")
            return

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception:
            print("Fecha inválida.")
            return

        shift = Shift(
            worked_hours=int(hours),
            shift_date=date_obj,
            task_description=task,
            employee_id=int(emp_id),
            project_id=int(proj_id),
        )
        shift_id = shift.log_worked_hours(self.db)
        if shift_id:
            print(f"Registro guardado con id {shift_id}")

    def list_shifts(self):
        if not self.current_user.is_admin() and not self.current_user.is_manager():
            print("No tienes permisos para ver registros de tiempo")
            return
        print("\n--- Registros de Tiempo ---")
        rows = Shift.list_shifts(self.db)
        for row in rows:
            print(row)
