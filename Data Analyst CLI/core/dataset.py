"""Доменный слой для работы с табличными данными."""

from dataclasses import dataclass, field


@dataclass
class DataRow:
    """Представление строки CSV-файла."""

    values: dict[str, str] = field(default_factory=dict)


@dataclass
class ColumnStats:
    """Заготовка для статистики по столбцу."""

    name: str
    count: int = 0
    missing: int = 0
    minimum: float | None = None
    maximum: float | None = None
    average: float | None = None


class DataTable:
    """Коллекция строк и операций над ними."""

    def __init__(self):
        self._rows = []
        self._columns = []

    def load_rows(self, rows):
        """Загружает строки данных."""

        pass

    def column_names(self):
        """Возвращает список столбцов."""

        pass

    def summarize(self, column):
        """Вычисляет базовую статистику по столбцу."""

        pass

    def filter_rows(self, predicate):
        """Возвращает строки, удовлетворяющие условию."""

        pass
