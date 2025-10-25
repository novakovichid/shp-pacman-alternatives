"""Доменный слой для работы с табличными данными."""

from dataclasses import dataclass, field


@dataclass
class DataRow:
    """Строка таблицы с доступом к значениям по именам столбцов."""

    values: dict[str, str] = field(default_factory=dict)

    def get(self, key, default=None):
        """Возвращает значение по имени столбца."""
        return self.values.get(key, default)

    def set(self, key, value):
        """Устанавливает значение столбца."""
        self.values[key] = value


@dataclass
class ColumnStats:
    """Заготовка для статистики по столбцу."""

    name: str
    count: int = 0
    missing: int = 0
    minimum: float | None = None
    maximum: float | None = None
    average: float | None = None

    def register_value(self, value):
        """Регистрирует числовое значение в статистике."""
        pass

    def register_missing(self):
        """Учитывает пропуск значения."""
        pass

    def finalize(self):
        """Вычисляет агрегированные показатели."""
        pass


class DataTable:
    """Коллекция строк и операций над ними."""

    def __init__(self):
        self._rows = []
        self._columns = []

    def load_rows(self, rows):
        """Загружает строки данных в таблицу."""
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
