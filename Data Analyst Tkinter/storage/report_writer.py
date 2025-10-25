"""Заготовка для записи текстовых отчётов."""

from pathlib import Path

from settings import Settings


class ReportWriter:
    """Сохраняет отчёты о данных."""

    def ensure_directories(self):
        """Создаёт каталоги для отчётов и состояния."""
        for directory in (Settings.REPORTS_DIR, Settings.DATA_DIR, Settings.LAST_SESSION_FILE.parent):
            directory.mkdir(parents=True, exist_ok=True)

    def write_report(self, path, lines):
        """Записывает строки отчёта в файл."""
        Path(path).write_text("\n".join(lines), encoding="utf-8")

    def remember_last_file(self, path):
        """Сохраняет путь к последнему открытому CSV."""
        Settings.LAST_SESSION_FILE.write_text(str(path), encoding="utf-8")

    def load_last_file(self):
        """Возвращает путь к последнему открытому CSV, если он сохранён."""
        if not Settings.LAST_SESSION_FILE.exists():
            return None
        return Settings.LAST_SESSION_FILE.read_text(encoding="utf-8").strip()
