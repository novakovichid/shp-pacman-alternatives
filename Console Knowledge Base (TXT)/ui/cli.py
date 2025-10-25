"""Заготовка консольного интерфейса Console Knowledge Base."""

from services.note_service import NoteService


class CommandLoop:
    """Минимальный слой пользовательского взаимодействия."""

    def __init__(self, service: NoteService):
        self.service = service

    def show_welcome(self):
        """Выводит приветственное сообщение."""
        print("Console Knowledge Base — учебный шаблон управления текстовыми заметками.")

    def show_placeholder(self):
        """Поясняет, что функциональность ещё не реализована."""
        print("Команды создания, поиска и экспорта заметок пока не реализованы.")
        print("Каркас демонстрирует запуск и структуру приложения.")
