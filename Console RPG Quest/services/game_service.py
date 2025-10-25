"""Сервисный слой консольной RPG."""

from core.entities import Enemy, GameWorld, Item, Quest


class GameService:
    """Управляет сценарием игры и взаимодействием слоёв."""

    def __init__(self):
        self.world = GameWorld()
        self.log = []

    def start_new_game(self, player_name):
        """Создаёт нового игрока и очищает состояние."""
        pass

    def load_saved_game(self, data):
        """Восстанавливает состояние мира из данных сохранения."""
        pass

    def schedule_battle(self, enemy):
        """Добавляет бой с указанным врагом."""
        pass

    def complete_quest(self, quest):
        """Помечает квест выполненным и выдаёт награды."""
        pass

    def add_item_to_player(self, item):
        """Добавляет предмет игроку и записывает событие."""
        pass

    def build_summary(self):
        """Возвращает текстовый отчёт о состоянии игрока."""
        pass
