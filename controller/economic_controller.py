from datetime import datetime

from services.economic_indicators_logs import VALID_INDICATORS, EconomicIndicatorsLogs
from models.economic_indicator import EconomicIndicatorLog


class EconomicIndicatorController:
    def __init__(self, db, current_user):
        self.db = db
        self.current_user = current_user

    def query_indicator(self):
        while True:
            indicator = input("Ingrese el indicador a consultar: ").strip().lower()
            if indicator in VALID_INDICATORS:
                break
            print("Indicador inválido. Intenta nuevamente.")

        date = input("Ingrese la fecha (dd-mm-AAAA): ").strip()

        print("\nConsultando indicador económico...")
        data = EconomicIndicatorsLogs.get_indicator_data(
            self.db,
            indicator,
            date,
            self.current_user.username,
        )

        save_data = input("¿Desea registrar esta consulta en el sistema? si/no: ")
        if save_data.lower() == "si":
            serie = data.get("serie", [])
            if serie:
                value = serie[0].get("valor")
                indicator_date = serie[0].get("fecha")
                log = EconomicIndicatorLog(
                    indicator_name=indicator,
                    indicator_date=indicator_date,
                    query_date=datetime.now(),
                    value=value,
                    provider_site="mindicador.cl",
                    username=self.current_user.username
                )
                log.save_log(self.db)
