import pyglet
from pyglet.graphics import Batch

from scenes.base import BaseScene


class PauseScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)
        self.label = pyglet.text.Label(
            "Pause",
            font_name="Times New Roman",
            font_size=36,
            x=50,
            y=10,
            batch=self.window.batch,
            color=(255, 255, 255, 255),
        )

    def process_key_event(self, symbol, modifiers):
        if symbol in (pyglet.window.key.SPACE, pyglet.window.key.P):
            self.window.switch_scene("menu")
