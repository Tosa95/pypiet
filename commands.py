import operator

COLORS = [[0xFFC0C0,0xFFFFC0,0xC0FFC0,0xC0FFFF,0xC0C0FF,0xFFC0FF],
		  [0xFF0000,0xFFFF00,0x00FF00,0x00FFFF,0x0000FF,0xFF00FF],
		  [0xC00000,0xC0C000,0x00C000,0x00C0C0,0x0000C0,0xC000C0],
		  [0xFFFFFF,0xFFFFFF,0xFFFFFF,0x000000,0x000000,0x000000]]

#command:(hue,light)
COMMANDS = {                    "push":(0,1),       "pop":(0,2),
			"add":(1,0),        "subtract":(1,1),   "multiply":(1,2),
			"divide":(2,0),     "mod":(2,1),        "not":(2,2),
			"greater":(3,0),    "pointer":(3,1),    "switch":(3,2),
			"duplicate":(4,0),  "roll":(4,1),       "inNum":(4,2),
			"inChar":(5,0),     "outNum":(5,1),     "outChar":(5,2)}

def nextColor (actColor, command):
	toSum=COMMANDS[command]

	(ay,ax) = actColor
	(sx,sy) = toSum #toSum ha x e y scambiate!!!

	res =  ((ay+sy)%3,(ax+sx)%6)

	(ry,rx) = res

	print "%s : (%d,%d)+(%d,%d)=(%d,%d)" % (command,ay,ax,sy,sx,ry,rx)

	return res
