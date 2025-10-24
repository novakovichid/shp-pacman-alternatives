import pyglet
from .base import BaseObject

class Image(BaseObject):
    def __init__(self, path, x, y, anchor_center=False, batch=None):
        super().__init__(x, y, batch)
        img = pyglet.image.load(path)
        if anchor_center:
            img.anchor_x = img.width // 2
            img.anchor_y = img.height // 2
        self.sprite = pyglet.sprite.Sprite(img=img, x=x, y=y, batch=batch)

    def set_position(self, x, y):
        self.x, self.y = x, y
        self.sprite.x, self.sprite.y = x, y

    def draw(self):
        if self.visible and self.batch is None:
            self.sprite.draw()
