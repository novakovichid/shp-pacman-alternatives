from pathlib import Path


class Settings:
    """Глобальные настройки приложения."""

    APP_NAME = "Console Tracker"
    DATA_DIR = Path("data")
    TASKS_FILE = DATA_DIR / "tasks.csv"
    LOG_FILE = Path("logs") / "app.log"
