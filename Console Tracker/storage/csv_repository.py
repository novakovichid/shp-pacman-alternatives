"""Заготовка хранилища задач Console Tracker."""

from core.tracker import Task
from settings import Settings


class CsvTaskRepository:
    """Отвечает за работу с CSV-файлом задач."""

    def __init__(self, path=None):
        self.path = path or Settings.TASKS_FILE

    def load(self):
        """Загружает задачи из CSV-файла."""

        pass

    def save(self, tasks):
        """Сохраняет задачи в CSV-файл."""

        pass
