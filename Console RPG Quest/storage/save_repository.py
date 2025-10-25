"""Заготовка для работы с файлами сохранений."""


class SaveRepository:
    """Читает и записывает данные профиля."""

    def __init__(self, path):
        self.path = path

    def load(self):
        """Возвращает содержимое файла сохранения."""
        pass

    def save(self, data):
        """Сохраняет состояние игры."""
        pass

    def backup(self):
        """Создаёт резервную копию сохранения."""
        pass
