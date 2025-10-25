"""Заготовки механики боя."""


class BattleContext:
    """Описывает текущее состояние боя."""

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_order = []
        self.round = 1

    def next_turn(self):
        """Переходит к следующему участнику."""
        pass

    def is_finished(self):
        """Возвращает True, если бой завершён."""
        pass


class TurnAction:
    """Выбранное действие в бою."""

    def __init__(self, actor, action_type="attack", payload=None):
        self.actor = actor
        self.action_type = action_type
        self.payload = payload or {}

    def resolve(self, context):
        """Применяет действие к контексту боя."""
        pass


class LootDrop:
    """Результат добычи после боя."""

    def __init__(self, items=None, gold=0):
        self.items = items or []
        self.gold = gold

    def is_empty(self):
        """Проверяет, содержит ли трофеи предметы или золото."""
        pass
