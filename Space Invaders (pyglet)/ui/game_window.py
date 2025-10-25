"""Графический слой игры Space Invaders."""

import pyglet

from services.game_service import GameService
from settings import Settings


class GameWindow:
    """Обёртка над pyglet.window.Window."""

    def __init__(self, service: GameService):
        self.service = service
        self.window = None

    def create_window(self):
        """Создаёт окно и регистрирует обработчики событий."""
        pass

    def bind_events(self):
        """Подключает обработчики клавиш и отрисовки."""
        pass

    def show_welcome(self):
        """Выводит приветственное сообщение."""
        print("Space Invaders (pyglet) — учебный шаблон 2D-игры.")

    def show_placeholder(self):
        """Сообщает об отсутствии реализованной логики."""
        print("Окно pyglet пока не создаётся, игровой цикл не запущен.")
        print("Выполните задачи из каталога `tasks/`, чтобы реализовать механику.")

    def schedule_updates(self):
        """Добавляет периодический вызов сервиса обновления."""
        pass

    def run(self):
        """Запускает главный цикл pyglet."""
        pass
