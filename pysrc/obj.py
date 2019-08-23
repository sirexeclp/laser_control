import point

TOP     =  2 ** 15 - 1
VIS_BOTTOM  = -9000 # -2 ** 15

BOTTOM  = - 2 ** 15

FRAME=abs(TOP)+abs(BOTTOM)

def clamp(v):
	if v < BOTTOM:
		return v + FRAME
	if v > TOP:
		return v - FRAME
	return v

def mask(p):
	if p.y < VIS_BOTTOM:
		return tuple(p._replace(y=TOP))
	return tuple(p)

class LaserObject(object):

	def __init__(self, points):
		self._points = list(points)
		self.visible = True

	def _replace(self, **kwargs):
		self._points = [p._replace(**kwargs) for p in self._points]

	def setColor(self, r, g, b):
		self._replace(r=point.col_c(r), g=point.col_c(g), b=point.col_c(b))
	
	def move(self, dx=0, dy=0):
		self._points = [p._replace(x=clamp(p.x + dx), y=clamp(p.y + dy)) for p in self._points]

	def render(self):
		if not self.visible or self.outofrange():
			return []
		return list(map(mask, self._points))

	def outofrange(self):
		return all(p.y < VIS_BOTTOM for p in self._points)
