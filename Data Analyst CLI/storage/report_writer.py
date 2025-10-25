"""Заготовка для сохранения текстовых отчётов."""

from pathlib import Path

from core.dataset import ColumnStats


class ReportWriter:
    """Отвечает за генерацию файлов отчётов."""

    def save_summary(self, path: Path, summary: list[ColumnStats]):
        """Записывает агрегированную статистику в текстовый файл."""

        pass

    def save_missing_report(self, path: Path, summary: list[ColumnStats]):
        """Сохраняет отчёт о пропущенных значениях."""

        pass

    def save_filtered_rows(self, path: Path, rows):
        """Экспортирует выбранные строки в отдельный файл."""

        pass
