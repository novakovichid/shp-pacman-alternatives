from pathlib import Path


class Settings:
    """Глобальные настройки приложения."""

    APP_NAME = "Data Analyst Tkinter"
    DATA_DIR = Path("data")
    REPORTS_DIR = Path("reports")
    LAST_SESSION_FILE = Path("state") / "last_path.txt"
    SUMMARY_REPORT = REPORTS_DIR / "summary.txt"
    STATS_REPORT = REPORTS_DIR / "stats.txt"
