"""Доменный слой Console Tracker."""

from dataclasses import dataclass, field


@dataclass
class Task:
    """Минимальная модель задачи."""

    title: str
    description: str = ""
    deadline: str | None = None
    completed: bool = False
    tags: list[str] = field(default_factory=list)


class TaskTracker:
    """Коллекция задач и операции над ними."""

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        """Добавляет задачу в коллекцию."""

        pass

    def all_tasks(self):
        """Возвращает список всех задач."""

        pass

    def load_initial(self, tasks):
        """Загружает стартовый набор задач."""

        pass

    def find_by_title(self, title):
        """Находит задачу по заголовку."""

        pass

    def remove(self, title):
        """Удаляет задачу по заголовку."""

        pass
