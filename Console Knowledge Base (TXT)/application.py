"""Точка входа консольной базы знаний на текстовых файлах."""

from services.note_service import NoteService
from ui.cli import CommandLoop


class ConsoleApplication:
    """Инициализирует каркас приложения и запускает приветствие."""

    def __init__(self):
        self.service = NoteService()
        self.cli = CommandLoop(self.service)

    def run(self):
        """Выводит приветственное сообщение и пояснение по шаблону."""
        self.cli.show_welcome()
        self.cli.show_placeholder()
