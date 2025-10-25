"""Заготовка хранилища данных Space Invaders."""

from settings import Settings


class HighscoreRepository:
    """Отвечает за сохранение рекордов игрока."""

    def __init__(self, path=None):
        self.path = path or Settings.HIGHSCORE_FILE

    def load(self):
        """Возвращает сохранённый рекорд."""
        pass

    def save(self, value):
        """Сохраняет новый рекорд."""
        pass


class AssetManifest:
    """Хранит сведения о ресурсах игры."""

    def __init__(self):
        self.images = {}
        self.sounds = {}

    def register_image(self, name, path):
        """Добавляет изображение в манифест."""
        pass

    def register_sound(self, name, path):
        """Добавляет звук в манифест."""
        pass

    def all_assets(self):
        """Возвращает словарь всех ресурсов."""
        pass
