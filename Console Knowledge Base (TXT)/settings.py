from pathlib import Path


class Settings:
    """Глобальные настройки приложения."""

    APP_NAME = "Console Knowledge Base (TXT)"
    NOTES_DIR = Path("notes")
    INDEX_FILE = Path("index") / "index.txt"
    EXPORT_FILE = Path("exports") / "all_notes.txt"
