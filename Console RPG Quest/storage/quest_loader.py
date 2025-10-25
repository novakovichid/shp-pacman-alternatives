"""Заготовка загрузки библиотеки квестов."""


class QuestLoader:
    """Отвечает за чтение и парсинг JSON-файлов с квестами."""

    def __init__(self, path):
        self.path = path

    def load_all(self):
        """Возвращает список определений квестов."""
        pass

    def validate_schema(self, data):
        """Проверяет структуру файла с квестами."""
        pass
