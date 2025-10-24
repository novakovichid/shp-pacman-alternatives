from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, window):
        self.window = window

    def activate(self):
        """Вызывается при входе в сцену (инициализация, сброс состояния)."""
        pass

    def process_logic(self, dt: float):
        """Игровая логика за кадр. dt — длительность кадра в секундах."""
        pass

    def process_key_event(self, symbol, modifiers):
        pass

    def process_mouse_event(self, x, y, button, modifiers):
        pass
