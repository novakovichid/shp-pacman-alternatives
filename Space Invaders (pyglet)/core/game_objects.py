"""Доменный слой игры Space Invaders."""


class GameObject:
    """Базовая сущность с положением и размерами."""

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, sprite_name=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite_name = sprite_name

    def update(self, dt):
        """Обновляет состояние объекта."""
        pass


class PlayerShip(GameObject):
    """Игровой корабль игрока."""

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.cooldown = 0.0

    def move_left(self, dt):
        """Смещает корабль влево."""
        pass

    def move_right(self, dt):
        """Смещает корабль вправо."""
        pass

    def fire(self):
        """Создаёт новый снаряд."""
        pass


class Enemy(GameObject):
    """Противник со скоростью и направлением движения."""

    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.direction = 1

    def change_direction(self):
        """Инвертирует направление движения врага."""
        pass


class Projectile(GameObject):
    """Снаряд игрока или врага."""

    def __init__(self):
        super().__init__()
        self.velocity_y = 0.0
        self.owner = "player"

    def advance(self, dt):
        """Перемещает снаряд по вертикали."""
        pass


class Wave:
    """Коллекция врагов одной волны."""

    def __init__(self):
        self.enemies = []
        self.drop_distance = 20.0

    def update(self, dt):
        """Обновляет движение всех врагов."""
        pass

    def is_cleared(self):
        """Возвращает True, если все враги побеждены."""
        pass


class GameWorld:
    """Общее состояние уровня."""

    def __init__(self):
        self.player = PlayerShip()
        self.wave = Wave()
        self.projectiles = []
        self.score = 0
        self.level = 1

    def reset(self):
        """Перезапускает игру с начальными значениями."""
        pass

    def spawn_wave(self):
        """Генерирует новую волну врагов."""
        pass

    def cleanup_projectiles(self):
        """Удаляет снаряды, вышедшие за пределы экрана."""
        pass
