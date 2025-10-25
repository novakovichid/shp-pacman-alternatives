"""Доменный слой консольной RPG."""


class Item:
    """Предмет инвентаря с типом и эффектами."""

    def __init__(self, name="", description="", item_type="", power=0):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.power = power

    def apply_to(self, target):
        """Применяет эффект предмета к цели."""
        pass


class Character:
    """Базовый персонаж с характеристиками."""

    def __init__(self, name="", max_health=0, attack=0, defense=0):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def is_alive(self):
        """Возвращает True, если персонаж жив."""
        pass

    def receive_damage(self, amount):
        """Уменьшает здоровье с учётом защиты."""
        pass

    def add_item(self, item):
        """Добавляет предмет в инвентарь."""
        pass


class Player(Character):
    """Игрок с опытом и активным квестом."""

    def __init__(self):
        super().__init__()
        self.experience = 0
        self.level = 1
        self.active_quest = None

    def gain_experience(self, amount):
        """Начисляет опыт и проверяет повышение уровня."""
        pass

    def choose_action(self, context):
        """Возвращает выбранное игроком действие."""
        pass


class Enemy(Character):
    """Противник с шаблоном поведения."""

    def __init__(self):
        super().__init__()
        self.behaviour = "aggressive"
        self.loot_table = []

    def decide_move(self, context):
        """Определяет действие врага в бою."""
        pass


class Quest:
    """Сюжетный квест с условиями выполнения."""

    def __init__(self, title="", description="", objectives=None, rewards=None):
        self.title = title
        self.description = description
        self.objectives = objectives or []
        self.rewards = rewards or []
        self.completed = False

    def is_ready_to_complete(self, player):
        """Проверяет, выполнены ли все цели квеста."""
        pass

    def apply_rewards(self, player):
        """Выдаёт награды игроку."""
        pass


class GameWorld:
    """Текущее состояние мира и активных сцен."""

    def __init__(self):
        self.player = Player()
        self.locations = []
        self.active_enemies = []
        self.time_of_day = "day"

    def advance_time(self):
        """Смещает время суток и запускает события."""
        pass

    def spawn_enemy(self, enemy):
        """Добавляет врага в текущую сцену."""
        pass

    def start_quest(self, quest):
        """Назначает квест игроку."""
        pass
