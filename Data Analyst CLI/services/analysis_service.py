"""Сервисный слой для аналитических операций."""

from core.dataset import ColumnStats, DataTable
from storage.csv_loader import CsvDatasetReader
from storage.report_writer import ReportWriter


class DataAnalysisService:
    """Организует взаимодействие доменной модели и хранилища."""

    def __init__(self):
        self.table = DataTable()
        self.reader = CsvDatasetReader()
        self.reporter = ReportWriter()

    def load_dataset(self, path):
        """Загружает данные из CSV-файла."""

        pass

    def available_columns(self):
        """Возвращает список столбцов для анализа."""

        pass

    def compute_summary(self, column):
        """Строит статистику по заданному столбцу."""

        pass

    def filter_rows(self, column, value):
        """Фильтрует строки по условию равенства."""

        pass

    def export_reports(self, summary: list[ColumnStats]):
        """Сохраняет текстовые отчёты на основе статистики."""

        pass
