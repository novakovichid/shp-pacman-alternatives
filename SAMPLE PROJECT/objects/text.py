import pyglet
from .base import BaseObject

class Text(BaseObject):
    def __init__(self, text, x, y, font_name='Times New Roman', font_size=24, color=(255,255,255,255), anchor_x='left', anchor_y='baseline', batch=None):
        super().__init__(x, y, batch)
        self.text = pyglet.text.Label(
            text,
            x=x, y=y,
            font_name=font_name, font_size=font_size,
            color=color, anchor_x=anchor_x, anchor_y=anchor_y,
            batch=batch
        )

    def set_text(self, value: str):
        self.text.text = value

    def set_position(self, x, y):
        self.x, self.y = x, y
        self.text.x, self.text.y = x, y

    def draw(self):
        if self.visible and self.batch is None:
            self.text.draw()
