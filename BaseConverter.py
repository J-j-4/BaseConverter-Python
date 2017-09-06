from tkinter import Tk, Entry, IntVar, StringVar, Label, Frame, Button, N, W, E, S, FLAT, GROOVE

oldVariables = [0, 0, 0]

def convertDecimalToBinary(decimalNumber):
	Q = 1
	R = 0
	N = decimalNumber
	n = 2

	RList = []
	result = ""

	while Q != 0:
		Q = N // n
		R = N % n
		RList.append(R)
		N = Q

	RList.reverse()
	for i in range(len(RList)):
		result += str(RList[i])

	return result

def convertDecimalToHexadecimal(decimalNumber):
	Q = 1
	R = 0
	N = decimalNumber
	n = 16

	RList = []
	result = ""

	while Q != 0:
		Q = N // n
		R = N % n
		RList.append(R)
		N = Q

	hexa = ("A", "B", "C", "D", "E", "F")

	RList.reverse()
	for i in range(len(RList)):
		if RList[i] > 9:
			result += hexa[RList[i] - 10]
		else:
			result += str(RList[i])

	return result

def convertHexaToDecimal(hexadecimalNumber):
	n = 0
	hexa = ("0", "1", "2", "3", "4", "5", "6", "7", 
		"8", "9", "A", "B", "C", "D", "E", "F")

	value = (lambda string : hexa.find(string))

	hexadecimalNumber = hexadecimalNumber[::-1]
	result = 0

	for i in hexadecimalNumber:
		result += find(hexa, i) * 16**n
		n += 1

	return result

def convertHexaToBinary(hexadecimalNumber):
	
	hexa = ("0", "1", "2", "3", "4", "5", "6", "7", 
		"8", "9", "A", "B", "C", "D", "E", "F")

	binarySeq = ""

	for i in hexadecimalNumber:
		sub_seq = convertDecimalToBinary(find(hexa, i))
		while len(sub_seq) < 4:
			sub_seq += "0"
		binarySeq += sub_seq

	return binarySeq

def convertBinaryToDecimal(binaryNumber):
	n = len(binaryNumber) - 1
	result = 0

	for i in binaryNumber:
		result += 2**n * int(i)
		n -= 1

	return result 

def convertBinaryToHexadecimal(binaryNumber):
	return convertDecimalToHexadecimal(convertBinaryToDecimal(binaryNumber))

def conversion(decimalVar, hexaVar, binaryVar):

	global oldVariables

	if decimalVar.get() != oldVariables[0]:
		hexaVar.set(convertDecimalToHexadecimal(decimalVar.get()))
		binaryVar.set(convertDecimalToBinary(decimalVar.get()))

	elif hexaVar.get() != str(oldVariables[1]):
		decimalVar.set(convertHexaToDecimal(hexaVar.get()))
		binaryVar.set(convertHexaToBinary(hexaVar.get()))

	elif binaryVar.get() != str(oldVariables[2]):
		decimalVar.set(convertBinaryToDecimal(binaryVar.get()))
		hexaVar.set(convertBinaryToHexadecimal(binaryVar.get()))

	oldVariables = (decimalVar.get(), hexaVar.get(), binaryVar.get())
	
def find(tpl, item):

	i = 0
	for j in tpl:
		if j == item:
			break
		i += 1

	return (i if i in range(len(tpl)) else -1)

def main():

	tk = Tk()
	tk.title("Base 10 - 2 - 16 converter")
	tk.tk_setPalette(background="#FFFFFF")

	mainFrame = Frame(master = tk, background = "#FFFFFF")

	decimalVar   = IntVar()
	entryDecimal = Entry(master = mainFrame, textvariable = decimalVar, background = "#F8F8F8")
	hexaVar      = StringVar()
	entryHexa    = Entry(master = mainFrame, textvariable = hexaVar, background = "#F8F8F8")
	binaryVar    = StringVar()
	entryBinary  = Entry(master = mainFrame, textvariable = binaryVar, background = "#F8F8F8")

	decimalLabel = Label(master = mainFrame, text = "Decimal")
	hexaLabel    = Label(master = mainFrame, text = "Hexadecimal")
	binaryLabel  = Label(master = mainFrame, text = "Binary")

	convert      = Button(master = mainFrame, text = "Convert", 
		command = lambda : conversion(decimalVar, hexaVar, binaryVar),
		relief = GROOVE, 
		highlightthickness = 3)

	mainFrame.grid(row = 0, column = 0, padx = 60, pady = 30)

	decimalLabel.grid(row = 0, column = 0, pady = 10, padx = 5, sticky = W)
	entryDecimal.grid(row = 0, column = 1, pady = 10)
	hexaLabel.grid   (row = 1, column = 0, pady = 10, padx = 5, sticky = W)
	entryHexa.grid   (row = 1, column = 1, pady = 10)
	binaryLabel.grid (row = 2, column = 0, pady = 10, padx = 5, sticky = W)
	entryBinary.grid (row = 2, column = 1, pady = 10)

	convert.grid     (row = 3, column = 0, columnspan = 2, pady = 5)

	decimalVar.set(0)
	hexaVar.set(0)
	binaryVar.set(0)

	tk.mainloop()

main()