"""Заготовка для чтения CSV-файлов."""

import csv
from pathlib import Path

from core.dataset import DataRow


class CsvDatasetLoader:
    """Загружает данные из CSV в объекты доменной модели."""

    def read(self, path):
        """Читает CSV и возвращает список DataRow."""
        if not Path(path).exists():
            return []
        return []

    def detect_columns(self, rows):
        """Определяет список столбцов по заголовку."""
        if not rows:
            return []
        return list(rows[0].values.keys())
