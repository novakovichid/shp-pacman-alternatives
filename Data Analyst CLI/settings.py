from pathlib import Path


class Settings:
    """Глобальные настройки приложения."""

    APP_NAME = "Data Analyst CLI"
    DATA_DIR = Path("data")
    REPORTS_DIR = Path("reports")
    DEFAULT_DATASET = DATA_DIR / "dataset.csv"
    SUMMARY_REPORT = REPORTS_DIR / "summary.txt"
