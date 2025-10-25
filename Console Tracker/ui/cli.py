"""Заготовка консольного интерфейса Console Tracker."""

from services.task_service import TaskService


class CommandLoop:
    """Минимальный слой пользовательского взаимодействия."""

    def __init__(self, service: TaskService):
        self.service = service

    def show_welcome(self):
        """Выводит приветственное сообщение."""
        print("Console Tracker — учебный шаблон консольного приложения.")

    def show_placeholder(self):
        """Поясняет, что функциональность ещё не реализована."""
        print("Базовые команды пока не реализованы.")
        print("Сейчас приложение демонстрирует только успешный запуск каркаса.")
