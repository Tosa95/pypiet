from PIL import Image, ImageDraw
import commands

def drawCodel (draw, color, coords, sz):

	(cx,cy) = coords

	draw.rectangle([coords,(cx+sz-1,cy+sz-1)],color)

def drawBlock (draw, color, startcoord, blocksz, codelsz):
	(cx,cy) = startcoord

	for i in range(blocksz):
		drawCodel(draw, color, (cx,cy), codelsz)
		cx = cx + codelsz

	return (cx, cy)

def revColor (color):
	R = (color & 0xFF0000)>>16
	G = (color & 0x00FF00)
	B = (color & 0x0000FF)

	B = B*(2**16)

	print "R: " + format(R, '#04X')
	print "G: " + format(G, '#04X')
	print "B: " + format(B, '#04X')

	print "BGR: " + format(R + G + B, '#04X')

	return R+G+B

def sequenceToPng (seq, filename, width, height, codelsz):

	img = Image.new('RGB', (width*codelsz, height*codelsz))

	draw = ImageDraw.Draw(img)

	actPos = (0,0)

	color = 0

	for ((colory,colorx),sz) in seq:
		color = revColor(commands.COLORS[colory][colorx])

		print format(color, '#04X')

		actPos = drawBlock(draw, color, actPos, sz, codelsz)

	(px,py)=actPos

	px-=codelsz

	drawCodel(draw,color,(px,py+codelsz),codelsz)
	drawCodel(draw,color,(px-codelsz,py+2*codelsz),codelsz)
	drawCodel(draw,color,(px,py+2*codelsz),codelsz)
	drawCodel(draw,color,(px+1*codelsz,py+2*codelsz),codelsz)
	#draw.rectangle([(0,20),(2000,2000)],0xC0C0FF)

	img.save(filename)
