import pyglet as pg
import maps
import entity
import numpy as np


class GameWindow(pg.window.Window):

    def __init__(self):
        super(GameWindow, self).__init__(300, 100)
        pg.gl.glClearColor(0.0, 0.0, 0.0, 0.0)
        self.entities = [entity.Settlement(500, 500, [1, 0, 0]),
                         entity.Settlement(360, 510, [0, 1, 0])]
        self.map = maps.Map(depth=7)
        self.set_caption('Loading Map')
        self.map.load_tiles()
        self.px = 0
        self.py = 0

        self.mov = [0, 0]
        self.set_caption('Map')
        self.maximize()

    def on_draw(self):
        self.map.plot_map(self.px, self.py)
        for i in self.entities:
            i.plot_entity(self.px, self.py)

    def move_pos(self, dt):
        self.px += self.mov[0]
        self.py += self.mov[1]
        self.clear()
        self.map.plot_map(self.px, self.py)

    def on_key_press(self, symbol, modifiers):
        if symbol in [65361, 97]:
            self.mov[0] = 5
        elif symbol in [65363, 100]:
            self.mov[0] = -5
        elif symbol in [65362, 119]:
            self.mov[1] = -5
        elif symbol in [65364, 115]:
            self.mov[1] = 5

    def on_mouse_motion(self, x, y, dx, dy):
        for i in self.entities:
            i.hover(self.px, self.py, x, y)

    def on_key_release(self, symbol, modifiers):
        if symbol in [65361, 97]:
            self.mov[0] = 0
        elif symbol in [65363, 100]:
            self.mov[0] = 0
        elif symbol in [65362, 119]:
            self.mov[1] = 0
        elif symbol in [65364, 115]:
            self.mov[1] = 0
        elif symbol is pg.window.key.F:
            self.maximize()

    def __run__(self):
        pg.clock.schedule_interval(self.move_pos, 0.02)
        pg.app.run()





