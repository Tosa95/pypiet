# -*- coding: utf-8 -*-

import commands

def _biggerPowOfTwo (num):
	if (num < 2):
		return 0

	acc = 2
	exp = 1

	while acc<num:
		acc *= 2
		exp += 1

	return exp-1

class StringPrinter:

	#Sequence è una lista di coppie (colore,dimensione), dove dimensione è la dimensione del blocco e colore è una coppia (y,x) di coordinate della tabella dei colori

	def __init__ (self, initColor=(0,0)):
		self._color = initColor
		self._sequence = []
		self._prev = -1

	def _updateColor(self, command):
		self._color = commands.nextColor(self._color, command)

	def _append(self, size):
		self._sequence.append((self._color,size))

	#Si da per scontato che il colore self._color non sia ancora stato stampato. Va finalizzata la sequenza alla fine
	def _insertNumberInStack (self, num):
		if (num < 8):
			self._append(num)
			self._updateColor("push")
		else:
			bpot = _biggerPowOfTwo(num)
			self._append(2)
			self._updateColor("push")

			for i in range(bpot-1):
				self._append(1)
				self._updateColor("duplicate")

			for i in range(bpot-1):
				self._append(1)
				self._updateColor("multiply")

			#qua ho la potenza di 2 più vicina possibile (ma più piccola nello stack)

			remains = num - 2**bpot

			if (remains > 0):
				self._insertNumberInStack(remains)
				self._append(1)
				self._updateColor("add")



	def _stackedINIS (self, num):
		if (self._prev > 0):
			diff = num - self._prev

			if diff < 0:
				self._insertNumberInStack(-diff)
				self._append(1)
				self._updateColor("subtract")
				self._append(1)
				self._updateColor("duplicate")
			else:
				self._insertNumberInStack(diff)
				self._append(1)
				self._updateColor("add")
				self._append(1)
				self._updateColor("duplicate")

			self._prev = num
		else:
			self._insertNumberInStack(num)
			self._append(1)
			self._updateColor("duplicate")
			self._prev = num

	def printStr (self, str):
		for chr in str:
			code = ord(chr)
			self._stackedINIS(code)
			self._append(1)
			self._updateColor("outChar")

		self._append(1)


	def getSequence (self):
		return self._sequence[:]

if (__name__=="__main__"):

	print ("Ciaoooo")

	from pngPrinter import PNGPrinter

	pngptr = PNGPrinter(57,57,20)
	strptr = StringPrinter()

	strptr.printStr("R2Pi0 RULEZ")



	pngptr.printSeq(strptr.getSequence())

	pngptr.save("prova.png")


	print(strptr.getSequence())
