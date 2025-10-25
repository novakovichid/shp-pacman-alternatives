"""Скелет сервисного слоя Console Knowledge Base."""

from core.note import KnowledgeBase, Note
from storage.txt_repository import TxtRepository


class NoteService:
    """Управляет заметками и индексом."""

    def __init__(self, base=None, repository=None):
        self.base = base or KnowledgeBase()
        self.repository = repository or TxtRepository()

    def list_notes(self):
        """Возвращает заметки из базы."""

        pass

    def create_note(self, note: Note):
        """Добавляет новую заметку и обновляет индекс."""

        pass

    def delete_note(self, title: str):
        """Удаляет заметку по заголовку."""

        pass

    def rebuild_index(self):
        """Перестраивает индекс ключевых слов."""

        pass

    def export_all(self):
        """Создаёт общий текстовый файл со всеми заметками."""

        pass
