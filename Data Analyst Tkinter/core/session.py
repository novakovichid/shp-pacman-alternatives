"""Состояние текущей сессии приложения."""


class SessionState:
    """Хранит выбранный файл и результаты анализа."""

    def __init__(self):
        self.current_path = None
        self.table = None
        self.stats = []

    def set_dataset(self, path, table):
        """Сохраняет путь к CSV и таблицу данных."""
        self.current_path = path
        self.table = table

    def set_stats(self, stats):
        """Сохраняет вычисленные статистики."""
        self.stats = stats

    def reset(self):
        """Сбрасывает состояние сессии."""
        self.current_path = None
        self.table = None
        self.stats = []
