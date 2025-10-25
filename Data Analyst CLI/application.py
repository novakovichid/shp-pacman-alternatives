"""Точка входа утилиты Data Analyst CLI."""

from services.analysis_service import DataAnalysisService
from ui.cli import CommandLineInterface


class CliApplication:
    """Инициализирует каркас приложения и запускает приветствие."""

    def __init__(self):
        self.service = DataAnalysisService()
        self.cli = CommandLineInterface(self.service)

    def run(self):
        """Выводит приветственное сообщение и пояснение по шаблону."""
        self.cli.show_welcome()
        self.cli.show_placeholder()
