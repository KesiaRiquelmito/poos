from datetime import datetime


class Report:

    def __init__(self, name: str, generation_date=None, file_format: str = None):
        self.name = name
        self.generation_date = generation_date or datetime.now()
        self.file_format = file_format

    def render_text(self, rows, headers):
        lines = [f"Reporte: {self.name} - {self.generation_date:%Y-%m-%d %H:%M}"]
        lines.append(" | ".join(headers))
        for row in rows:
            lines.append(" | ".join(str(item) for item in row))
        return "\n".join(lines)
