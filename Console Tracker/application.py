"""Точка входа консольного трекера задач."""

from services.task_service import TaskService
from ui.cli import CommandLoop


class ConsoleApplication:
    """Инициализирует каркас приложения и запускает приветствие."""

    def __init__(self):
        self.service = TaskService()
        self.cli = CommandLoop(self.service)

    def run(self):
        """Выводит приветственное сообщение и пояснение по шаблону."""
        self.cli.show_welcome()
        self.cli.show_placeholder()
