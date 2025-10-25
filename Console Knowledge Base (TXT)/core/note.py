"""Доменный слой Console Knowledge Base."""

from dataclasses import dataclass, field


@dataclass
class Note:
    """Минимальная модель заметки."""

    title: str
    keywords: list[str] = field(default_factory=list)
    filename: str | None = None
    content: str = ""


class KnowledgeBase:
    """Коллекция заметок и операции над ними."""

    def __init__(self):
        self._notes = []

    def add_note(self, note):
        """Добавляет заметку в коллекцию."""

        pass

    def all_notes(self):
        """Возвращает список всех заметок."""

        pass

    def search(self, query):
        """Выполняет поиск заметок по ключевым словам."""

        pass

    def load_initial(self, notes):
        """Загружает стартовый набор заметок."""

        pass

    def remove(self, title):
        """Удаляет заметку по заголовку."""

        pass
