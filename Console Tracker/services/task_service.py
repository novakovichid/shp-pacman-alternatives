"""Скелет сервисного слоя Console Tracker."""

from core.tracker import Task, TaskTracker
from storage.csv_repository import CsvTaskRepository


class TaskService:
    """Объединяет доменный трекер и слой хранения."""

    def __init__(self, tracker=None, repository=None):
        self.tracker = tracker or TaskTracker()
        self.repository = repository or CsvTaskRepository()

    def list_tasks(self):
        """Возвращает задачи из трекера."""

        pass

    def create_task(self, task: Task):
        """Добавляет новую задачу и синхронизирует хранилище."""

        pass

    def complete_task(self, title: str):
        """Отмечает задачу выполненной."""

        pass

    def delete_task(self, title: str):
        """Удаляет задачу."""

        pass

    def reload(self):
        """Перечитывает данные из хранилища."""

        pass
