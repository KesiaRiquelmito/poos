from datetime import datetime

from config.database import Database
from models.security import Security
from models.shift import Shift


class ShiftController:
    def __init__(self, db: Database):
        self.db = db

    def log_shift(self):
        print("\n--- Registrar Horas ---")
        emp_id = Security.clean_text(input("ID empleado: "))
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
        print("\n--- Registros de Tiempo ---")
        rows = Shift.list_shifts(self.db)
        for row in rows:
            print(row)
