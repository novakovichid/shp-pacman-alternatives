class BaseObject:

    def __init__(self, x=0, y=0, batch=None, visible=True):
        self.x = x
        self.y = y
        self.batch = batch
        self.visible = visible

    def activate(self):
        pass

    def process_logic(self, dt: float):
        pass
    
    def set_position(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pass

    def process_event(self, event_type: str, *args, **kwargs):
        pass

    def destroy(self):
        pass
