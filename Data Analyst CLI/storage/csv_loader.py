"""Заготовка слоя чтения CSV-файлов."""

import csv
from pathlib import Path

from core.dataset import DataRow


class CsvDatasetReader:
    """Отвечает за загрузку данных из CSV."""

    def load(self, path: Path):
        """Читает файл и возвращает коллекцию строк."""

        pass

    def detect_columns(self, path: Path):
        """Определяет названия столбцов на основе заголовка."""

        pass
