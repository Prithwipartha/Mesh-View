import pyglet as pg
import numpy as np


def draw_points(pos, col):
    p = np.floor(pos).astype(int)
    pg.graphics.draw(len(p), pg.gl.GL_POINTS, ('v2i', p.flatten()), ('c3f', col.flatten()))


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hov_rad = 3
        self.pts = None
        self.col = None
        self.hov = False
        self.desc_box = pg.graphics.Batch()
        self.desc_list = [pg.shapes.Rectangle(self.x, self.y, 150, 200, batch=self.desc_box)]
        self.desc_labels = {}

    def plot_entity(self, px, py):
        draw_points(self.pts+np.array([px, py]), self.col)
        if self.hov:
            for i in self.desc_list:
                i.x = px+self.x+self.hov_rad
                i.y = py+self.y+self.hov_rad
            self.desc_box.draw()

    def hover(self, px, py, mx, my):
        p = self.pts+np.array([px-mx, py-my])
        p = p*p
        p = np.sqrt(p.sum(1)).min()
        self.hov = p < self.hov_rad




class Settlement(Entity):
    def __init__(self, x, y, c=np.array([0, 1, 1])):
        super(Settlement, self).__init__(x, y)

        self.pos = [x, y]
        self.pop = 100
        self.ruler_loyalty = .99
        self.public_loyalty = .99
        self.housing_level = 1
        self.admin_level = 1
        self.wall_level = 0
        self.barracks_level = 0
        self.tower_level = 0
        self.moat_level = 0
        self.selected = False

        x = np.array([[x-2, x-1, x, x+1, x+2]]*5)
        y = np.array([[y-2, y-1, y, y+1, y+2]]*5).transpose()
        pts = np.array([x,y]).transpose([1, 2, 0])
        self.pts = pts.reshape([25, 2])
        self.col = np.array([c]*25)







