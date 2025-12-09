import requests

VALID_INDICATORS = [
    "uf", "ivp", "dolar", "dolar_intercambio", "euro",
    "ipc", "utm", "imacec", "tpm", "libra_cobre",
    "tasa_desempleo", "bitcoin"
]


class EconomicIndicatorsLogs:

    @staticmethod
    def get_indicator_data(db, indicator: str, date: str, username: str):
        url = f"https://mindicador.cl/api/{indicator}/{date}"
        try:
            response = requests.get(url)
        except Exception as exc:
            print(f"Error en la solicitud: {exc}")
            return None

        data = response.json()
        serie = data.get("serie", [])
        if serie:
            value = serie[0].get("valor")
            indicator_date = serie[0].get("fecha").split("T")[0]
            print(f"Valor del indicador {indicator} para la fecha {indicator_date} es: {value}")

        if not serie:
            print("No hay datos para esa fecha.")
            return None
        return data
