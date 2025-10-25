"""Заготовка хранилища заметок в текстовых файлах."""

from core.note import Note
from settings import Settings


class TxtRepository:
    """Работает с каталогом заметок и индексным файлом."""

    def __init__(self, notes_dir=None, index_file=None, export_file=None):
        self.notes_dir = notes_dir or Settings.NOTES_DIR
        self.index_file = index_file or Settings.INDEX_FILE
        self.export_file = export_file or Settings.EXPORT_FILE

    def load_notes(self):
        """Сканирует каталог и возвращает заметки."""

        pass

    def save_note(self, note: Note):
        """Сохраняет заметку в отдельный файл."""

        pass

    def delete_note(self, title: str):
        """Удаляет файл заметки и обновляет индекс."""

        pass

    def write_index(self, notes):
        """Записывает индекс ключевых слов."""

        pass

    def export_notes(self, notes):
        """Создаёт общий текстовый файл со всеми заметками."""

        pass
