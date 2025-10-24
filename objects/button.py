import pyglet
from pyglet import shapes
from .text import Text

class Button:
    def __init__(self, x, y, text, batch):
        self.rect = shapes.Rectangle(x, y, 140, 52, (255, 255, 255), batch=batch)
        self.label = Text(text, x=x + 12, y=y + 16, font_size=18, color=(0,0,0,255), batch=batch)

    def inside_button(self, mouse_x, mouse_y):
        return (
            self.rect.x <= mouse_x <= self.rect.x + self.rect.width
            and self.rect.y <= mouse_y <= self.rect.y + self.rect.height
        )
