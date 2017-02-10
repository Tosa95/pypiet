from PIL import Image, ImageDraw
import commands

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def revColor (color):
	R = (color & 0xFF0000)>>16
	G = (color & 0x00FF00)
	B = (color & 0x0000FF)

	B = B*(2**16)

	#print "R: " + format(R, '#04X')
	#print "G: " + format(G, '#04X')
	#print "B: " + format(B, '#04X')

	#print "BGR: " + format(R + G + B, '#04X')

	return R+G+B

class PNGPrinter:

	def __init__ (self, width, height, codelsz):
		self._pos = (0,0)
		self._dp = 0
		self._dps = [(+1,0),(0,+1),(-1,0),(0,-1)]
		self._width = width
		self._height = height
		self._codelsz = codelsz
		self._image = Image.new('RGB', (width*codelsz, height*codelsz))
		self._draw = ImageDraw.Draw(self._image)

	def getDP (self):
		return self._dps[self._dp]

	def incDP (self):
		self._dp = (self._dp + 1)%4

	def printSeq (self, seq, pos = None, dp = None):
		if pos != None:
			self._pos = pos

		if dp != None:
			self._dp = dp

		color = 0

		for ((colory,colorx),sz) in seq:
			color = revColor(commands.COLORS[colory][colorx])

			#print format(color, '#04X')

			self.drawBlock(color,sz)

		self.finalize(color)

	def drawCodel (self, color, coords):

		(cx,cy) = coords

		sz = self._codelsz

		self._draw.rectangle([coords,(cx+sz-1,cy+sz-1)],color)

	def drawBlock (self, color, blocksz):

		(px,py) = self._pos

		for i in range(blocksz):

			self.drawCodel(color,(px,py))

			print (px,py)

			(ix,iy)=self.getDP()

			if ((ix==1 and px == self._width*self._codelsz - self._codelsz) or
			   (iy==1 and py == self._height*self._codelsz - self._codelsz) or
			   (ix==-1 and px == 0) or
			   (iy==-1 and py == 0)):
				print (px,py)
				print self.getDP()
				self.incDP()
				print self.getDP()

			(ix,iy)=self.getDP()
			px+=ix*self._codelsz
			py+=iy*self._codelsz

		self._pos = (px,py)

	def finalize (self, color):
		cs = self._codelsz

		(px,py) = self._pos

		(dx,dy) = self.getDP()

		px -= dx*cs

		py -= dy*cs

		if (self._dp == 0):
			self.drawCodel(color,(px,py+cs))
			self.drawCodel(color,(px-cs,py+2*cs))
			self.drawCodel(color,(px,py+2*cs))
			self.drawCodel(color,(px+1*cs,py+2*cs))
		elif (self._dp == 1):
			self.drawCodel(color,(px-cs,py))
			self.drawCodel(color,(px-2*cs,py-cs))
			self.drawCodel(color,(px-2*cs,py))
			self.drawCodel(color,(px-2*cs,py+cs))
		elif (self._dp == 2):
			self.drawCodel(color,(px,py-cs))
			self.drawCodel(color,(px-cs,py-2*cs))
			self.drawCodel(color,(px,py-2*cs))
			self.drawCodel(color,(px+cs,py-2*cs))
		else:
			self.drawCodel(color,(px+cs,py))
			self.drawCodel(color,(px+2*cs,py-cs))
			self.drawCodel(color,(px+2*cs,py))
			self.drawCodel(color,(px+2*cs,py+cs))


	def save (self, name):
		self._image.save(name)
