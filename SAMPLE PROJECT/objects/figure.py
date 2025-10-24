from pyglet import shapes
from .base import BaseObject

class Rect(BaseObject):
    def __init__(self, x, y, width, height, color=(255,255,255), batch=None):
        super().__init__(x, y, batch)
        self.width = width
        self.height = height
        self.color = color
        self.shape = shapes.Rectangle(x, y, width, height, color=color, batch=batch)

    def set_position(self, x, y):
        self.x, self.y = x, y
        self.shape.x, self.shape.y = x, y

    def process_logic(self, dt: float):
        pass

    def draw(self):
        if self.visible and self.batch is None:
            self.shape.draw()


class Circle(BaseObject):
    def __init__(self, x, y, radius, color=(255,255,255), batch=None):
        super().__init__(x, y, batch)
        self.radius = radius
        self.color = color
        self.shape = shapes.Circle(x, y, radius, color=color, batch=batch)

    def set_position(self, x, y):
        self.x, self.y = x, y
        self.shape.x, self.shape.y = x, y

    def process_logic(self, dt: float):
        pass

    def draw(self):
        if self.visible and self.batch is None:
            self.shape.draw()


class Ellipse(BaseObject):
    def __init__(self, x, y, width, height, color=(255,255,255), batch=None):
        super().__init__(x, y, batch)
        self.width = width
        self.height = height
        self.color = color
        self.shape = shapes.Ellipse(x, y, width/2, height/2, color=color, batch=batch)

    def set_position(self, x, y):
        self.x, self.y = x, y
        self.shape.x, self.shape.y = x, y

    def process_logic(self, dt: float):
        pass

    def draw(self):
        if self.visible and self.batch is None:
            self.shape.draw()
