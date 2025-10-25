"""Точка входа учебной RPG."""

from services.game_service import GameService
from ui.console_interface import ConsoleInterface


class ConsoleRPGApplication:
    """Создаёт слои приложения и печатает приветствие."""

    def __init__(self):
        self.service = GameService()
        self.ui = ConsoleInterface(self.service)

    def run(self):
        """Выводит приветствие и пояснение."""
        self.ui.show_greeting()
        self.ui.show_placeholder()
