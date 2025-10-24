import pyglet
from pyglet import shapes

from scenes.menu import MenuScene
from scenes.pause import PauseScene
from settings import Settings


class Game(pyglet.window.Window):
    def __init__(self):
        super().__init__(Settings.WIDTH, Settings.HEIGHT, caption=Settings.CAPTION, vsync=True)
        # Применяем фон из настроек
        r, g, b, a = Settings.BACKGROUND_COLOR
        pyglet.gl.glClearColor(r/255.0, g/255.0, b/255.0, a/255.0)

        # Позиция окна
        try:
            self.set_location(Settings.WINDOW_X, Settings.WINDOW_Y)
        except Exception:
            pass

        # Общий batch для сцены
        self.batch = pyglet.graphics.Batch()

        # Ввод мыши
        self.mouse_state = pyglet.window.mouse.MouseStateHandler()
        self.push_handlers(self.mouse_state) 

        # Карта сцен
        self.scenes = {
            "menu": MenuScene,
            "pause": PauseScene,
        }
        # Текущая сцена
        self.current_scene = self.scenes["menu"](self)
        self.current_scene.activate()

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def update(self, dt):
        self.current_scene.process_logic(dt)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        if symbol in (pyglet.window.key.P,):
            self.switch_scene("pause" if isinstance(self.current_scene, MenuScene) else "menu")
            return
        self.current_scene.process_key_event(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.current_scene.process_mouse_event(x, y, button, modifiers)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / Settings.FPS)
        pyglet.app.run()

    def switch_scene(self, scene_name: str):
        self.batch = pyglet.graphics.Batch()
        new_scene = self.scenes[scene_name](self)
        self.current_scene = new_scene
        self.current_scene.activate()
