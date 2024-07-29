import pyglet as pg
import numpy as np

g_h = 2**16


def img(arr=np.array([])):
	if len(arr.shape)<3:
		arr = np.array([arr]*3).transpose([1, 2, 0])
	if arr.dtype not in [np.int64, np.int32, np.int16, np.int8]:
		arr = np.floor(arr*255).astype(np.int8)
	shp = arr.shape
	pixels = arr.flatten()
	rawData = (pg.gl.GLubyte * len(pixels))(*pixels)
	return pg.image.ImageData(shp[0], shp[1], 'RGB', rawData)

def img33i(arr):
	shp = arr.shape
	pixels = arr.flatten()
	rawData = (pg.gl.GLubyte * len(pixels))(*pixels)
	return pg.image.ImageData(shp[0], shp[1], 'RGB', rawData)


def img33f(arr):
	return img33i(np.floor(arr*255).astype(np.int))


def img2(arr):
	ret = np.array([arr]*3).transpose([1, 2, 0])
	return img33f(ret)


def rf01(shape, seed):
	np.random.seed(seed)
	return np.random.random(shape)


def ri01(shape, seed):
	np.random.seed(seed)
	return np.random.randint(0, 2, shape)


def axes(n):
	ret = np.arange(n)/n
	x = np.array([ret]*n)
	y = x.transpose()
	return x, y


def mr(n, x, y, prn=False):

	seed = g_h*x+y
	ret = np.zeros((n, n))*0.0

	h = rf01((n-1, n-1), seed)
	ret[:-1, :-1] = h

	h = rf01((n-1, n-1), seed+1)
	ret[-1, :-1] = h[0]

	h = rf01((n - 1, n - 1), seed + g_h)
	ret[:-1, -1] = h[:, 0]

	h = rf01((n - 1, n - 1), seed + g_h+1)
	ret[-1, -1] = h[0, 0]

	if prn:
		print(h)

	return ret


def draw_points(pos, col):
	p = np.floor(pos).astype(int)
	pg.graphics.draw(len(p), pg.gl.GL_POINTS, ('v2i', p.flatten()), ('c3f',col.flatten()))
	


