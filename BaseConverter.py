from tkinter import Tk, Menu, Entry, Scale, Spinbox, IntVar, StringVar, BooleanVar, Label, Frame, Button, N, W, E, S, FLAT, GROOVE, HORIZONTAL
from MultiBasesConverter import convert

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

	def switchFrame(current_frame, todisplay_frame):
		current_frame.grid_forget()
		todisplay_frame.grid(row = 0, column = 0, padx = 60, pady = 30)

	tk = Tk()
	tk.title("BaseConverter")
	tk.tk_setPalette(background="#FFFFFF")

	menu = Menu(master = tk, bg = "#DDDDDD", activebackground = "#999999")
	menu.add_command(label = "Switch to complete converter", 
		command = lambda : [switchFrame((classicFrame if frameDisplayed.get() == 0 else completeFrame), 
									   (completeFrame if frameDisplayed.get() == 0 else classicFrame)),
							frameDisplayed.set((1 if frameDisplayed.get() == 0 else 0)),
							menu.entryconfig(index = 1, label = ("Switch to complete converter" if frameDisplayed.get() == 0 else
								"Switch to quick converter"))])
	tk.config(menu = menu)

	frameDisplayed = BooleanVar() # 0 = classic, 1 = complete
	frameDisplayed.set(0)


	##### classic frame #####
	classicFrame = Frame(master = tk, background = "#FFFFFF")

	decimalVar   = IntVar()
	entryDecimal = Entry(master = classicFrame, textvariable = decimalVar, background = "#F8F8F8")
	hexaVar      = StringVar()
	entryHexa    = Entry(master = classicFrame, textvariable = hexaVar, background = "#F8F8F8")
	binaryVar    = StringVar()
	entryBinary  = Entry(master = classicFrame, textvariable = binaryVar, background = "#F8F8F8")

	decimalLabel = Label(master = classicFrame, text = "Decimal")
	hexaLabel    = Label(master = classicFrame, text = "Hexadecimal")
	binaryLabel  = Label(master = classicFrame, text = "Binary")

	convertButton1 = Button(master = classicFrame, text = "Convert", 
		command = lambda : conversion(decimalVar, hexaVar, binaryVar),
		relief = GROOVE)

	classicFrame.grid(row = 0, column = 0, padx = 60, pady = 30)

	decimalLabel.grid(row = 0, column = 0, pady = 10, padx = 5, sticky = W)
	entryDecimal.grid(row = 0, column = 1, pady = 10)
	hexaLabel.grid   (row = 1, column = 0, pady = 10, padx = 5, sticky = W)
	entryHexa.grid   (row = 1, column = 1, pady = 10)
	binaryLabel.grid (row = 2, column = 0, pady = 10, padx = 5, sticky = W)
	entryBinary.grid (row = 2, column = 1, pady = 10)

	convertButton1.grid(row = 3, column = 0, columnspan = 2, pady = 5)

	decimalVar.set(0)
	hexaVar.set(0)
	binaryVar.set(0)
	######################### classic frame


	##### complete Frame #####

	completeFrame = Frame(master = tk)

	labelFrom   = Label(completeFrame, text = "From base")
	
	fromBaseVar = IntVar()
	fromBaseVar.set(0)
	baseFrom    = Scale(completeFrame, from_ = 2, to = 26, orient = HORIZONTAL, variable = fromBaseVar)
	fromVar     = StringVar()
	fromVar.set("0")
	fromEntry   = Entry(completeFrame, textvariable = fromVar)

	labelFrom.grid(row = 0, column = 0, pady = 10, padx = 5, sticky = W)
	baseFrom.grid (row = 0, column = 1, pady = 10, padx = 5)
	fromEntry.grid(row = 0, column = 2, pady = 10, padx = 5)

	labelTo   = Label(completeFrame, text = "To base")
	toBaseVar = IntVar()
	toBaseVar.set(0)
	baseFrom  = Scale(completeFrame, from_ = 2, to = 26, orient = HORIZONTAL, variable = toBaseVar)
	toVar     = StringVar()
	toVar.set("0")
	toEntry   = Entry(completeFrame, textvariable = toVar)

	labelTo.grid (row = 1, column = 0, pady = 10, padx = 5, sticky = W)
	baseFrom.grid(row = 1, column = 1, pady = 10, padx = 5)
	toEntry.grid (row = 1, column = 2, pady = 10, padx = 5)

	convertButton2 = Button(master = completeFrame, text = "Convert", 
		command = lambda : toVar.set(convert(from_n = fromBaseVar.get(), to_m = toBaseVar.get(), number = fromVar.get())),
		relief = GROOVE)
	convertButton2.grid(row = 2, column = 0, columnspan = 3, pady = 10)


	######################### complete frame

	tk.mainloop()

main()