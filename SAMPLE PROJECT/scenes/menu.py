import pyglet

from objects.button import Button
from objects.text import Text
from objects.figure import Circle
from scenes.base import BaseScene


class MenuScene(BaseScene):
    def __init__(self, window):
        super().__init__(window)
        self.label = Text(
            "Menu", x=50, y=10, font_name="Times New Roman", font_size=36,
            color=(255, 255, 255, 255), batch=self.window.batch
        )
        self.push_button = Button(70, 100, "Hello", batch=self.window.batch)
        self.ball = Circle(x=50, y=400, radius=50, color=(255, 0, 0), batch=self.window.batch)
        self.speed = 120  # px/s

    def activate(self):
        self.ball.set_position(50, 400)

    def process_key_event(self, symbol, modifiers):
        if symbol in (pyglet.window.key.SPACE, pyglet.window.key.P):
            self.window.switch_scene("pause")

    def process_mouse_event(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT and self.push_button.inside_button(x, y):
            print("Кнопка нажата")

    def process_logic(self, dt: float):
        self.ball.set_position(self.ball.shape.x + self.speed * dt, self.ball.shape.y)
        if self.ball.shape.x - self.ball.radius > self.window.width:
            self.ball.set_position(-self.ball.radius, self.ball.shape.y)
