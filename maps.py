import core
from core import *


def slant(n, h):
	x, y = axes(n)
	ret = h[0][0] + (h[0][1]-h[0][0])*x + (h[1][0]-h[0][0])*y + (h[1][1]+h[0][0]-h[1][0]-h[0][1])*x*y
	return ret + np.sin(5*np.pi*ret)/(5*np.pi*0.22)
	

def slantset(arr, n):
	nd = len(arr)-1

	ret = np.zeros((nd*n, nd*n))*0.0
	for i in range(nd):
		for j in range(nd):
			ret[n*i:n*(i+1), n*j:n*(j+1)] = slant(n, arr[i:i+2,j:j+2])

	return ret
			

def randmap(x, y, r=0.7, s=256, depth=7):
	ret = np.zeros((s, s))*0.0
	for i in range(depth):

		n = 2**i
		ret += (r**i)*slantset(mr(n+1, x, y), int(s/n))
	return ret*(1-r)/(1-r**depth)


def col_map(x, y, s=256, depth=7):

	r = np.zeros((s, s)) * 0.0
	g = np.zeros((s, s)) * 0.0
	b = np.zeros((s, s)) * 0.0

	h_map = randmap(x, y, s=s, depth=depth)

	wm = (h_map < 0.35)
	ud = (wm*h_map/0.35)**4
	g += (ud*0.6+(1-ud)*0.15)*wm
	b += (ud * 0.5 + (1 - ud) * 0.2)*wm

	bm = (0.35 <= h_map)*(h_map < 0.37)
	r += bm*236/255
	g += bm*233/255
	b += bm *100/255

	fm = (0.37 <= h_map)*(h_map < 0.42)
	g += fm*170/255
	r += fm * 150 / 255

	fm = (0.42 <= h_map) * (h_map < 0.45)
	g += fm * 150 / 255
	r += fm * 120 / 255

	fm = (0.45 <= h_map) * (h_map < 0.68)
	seed = x*g_h + y
	tp = (h_map-0.45)/0.23
	tp = np.sin(0.6*np.pi*tp)
	tp = (core.rf01(tp.shape, seed)+0.1 < tp)

	g += fm * tp * (0.2+rf01(tp.shape, seed+1)/6)
	r += fm * tp * (0.1+rf01(tp.shape, seed+1)/6)

	g += (1-tp)*fm * 130 / 255
	r += (1-tp)*fm * 90 / 255

	fm = (0.68 <= h_map) * (h_map < 0.96)
	mh = (h_map-0.68)/0.28
	mh = mh+np.sin(8*np.pi*mh)/(16*np.pi)
	g += fm * (0.5*mh + 0.25*(1-mh))
	r += fm * (0.5*mh + 0.3*(1-mh))
	b += fm * (0.45*mh + 0.28*(1-mh))

	fm = (0.96 <= h_map)
	g += fm*0.7
	b += fm*0.8
	r += fm*0.8

	return [np.array([r, g, b]).transpose([1, 2, 0])]


class Map:
	def __init__(self, depth=7):
		self.depth = depth
		self.tiles = []

		self.heightmaps = []
		self.water_map = []

	def load_tiles(self, x=None, y=None):
		if (x is None) or (y is None):
			seed = np.random.randint(0, 2**15-1, [2])
			x = seed[0]
			y = seed[1]
		print("loading map at", (x, y))
		for i in range(8):
			retim = []

			for j in range(8):
				print('loading tile', (i, j))
				ret = col_map(x+i, y+j, depth=self.depth)
				retim += [img33f(ret[0])]

			self.tiles += [retim]

		print("map loading complete")

		self.tiles = np.array(self.tiles)


	def plot_map(self, x, y):
		if len(self.tiles):
			for i in np.arange(8):
				for j in np.arange(8):
					if (-255 < (x + i*256) < 1360) and (-255 < (y + j*256) < 750):
						self.tiles[i][j].blit(x+i*256-i, y+j*256-j)


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

