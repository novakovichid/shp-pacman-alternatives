"""Точка входа учебной аркады Space Invaders."""

from services.game_service import GameService
from ui.game_window import GameWindow


class SpaceInvadersApplication:
    """Создаёт слои приложения и выводит приветствие."""

    def __init__(self):
        self.service = GameService()
        self.window = GameWindow(self.service)

    def run(self):
        """Печатает приветствие и пояснение."""
        self.window.show_welcome()
        self.window.show_placeholder()
