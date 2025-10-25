"""Точка входа настольного приложения анализа CSV."""

from services.analysis_service import DataAnalysisService
from ui.windows import RootWindow


class TkinterApplication:
    """Инициализирует базовые зависимости и запуск графического интерфейса."""

    def __init__(self):
        self.service = DataAnalysisService()
        self.window = RootWindow(self.service)

    def run(self):
        """Открывает главное окно и показывает приветственное сообщение."""
        self.window.show_welcome()
        self.window.start_loop()
