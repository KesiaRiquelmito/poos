from config.database import Database


class EconomicIndicatorLog:
    def __init__(self, indicator_name: str, indicator_date, query_date, value, provider_site, username):
        self.indicator_name = indicator_name
        self.indicator_date = indicator_date
        self.query_date = query_date
        self.value = value
        self.provider_site = provider_site
        self.username = username

    def save_log(self, db: Database):
        db.execute(
            """
            INSERT INTO economic_indicators_logs
            (indicator_name, indicator_date, query_date, value, provider_site, username)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (self.indicator_name, self.indicator_date, self.query_date, self.value, self.provider_site, self.username)
        )
        print("Indicador económico registrado exitosamente.")
