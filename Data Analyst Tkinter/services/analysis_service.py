"""Сервисный слой для анализа CSV."""

from core.dataset import ColumnStats, DataTable
from core.session import SessionState
from settings import Settings
from storage.csv_loader import CsvDatasetLoader
from storage.report_writer import ReportWriter


class DataAnalysisService:
    """Оркестрирует загрузку данных, расчёт статистик и работу отчётов."""

    def __init__(self):
        self.session = SessionState()
        self.loader = CsvDatasetLoader()
        self.writer = ReportWriter()

    def prepare_environment(self):
        """Создаёт каталоги и загружает путь прошлой сессии."""
        self.writer.ensure_directories()
        return self.writer.load_last_file()

    def load_dataset(self, path):
        """Загружает CSV и сохраняет состояние."""
        rows = self.loader.read(path)
        table = DataTable()
        table.load_rows(rows)
        self.session.set_dataset(path, table)
        self.writer.remember_last_file(path)
        return table

    def calculate_statistics(self):
        """Вычисляет статистику по текущей таблице."""
        table = self.session.table
        if table is None:
            return []
        stats = []
        for column in table.column_names():
            stats.append(ColumnStats(name=column))
        self.session.set_stats(stats)
        return stats

    def export_reports(self):
        """Сохраняет отчёты в текстовые файлы."""
        table = self.session.table
        stats = self.session.stats
        lines = [Settings.APP_NAME]
        if table:
            lines.append(f"Rows: {len(table._rows)}")
        if stats:
            lines.append(f"Stats: {len(stats)} columns")
        self.writer.write_report(Settings.SUMMARY_REPORT, lines)
