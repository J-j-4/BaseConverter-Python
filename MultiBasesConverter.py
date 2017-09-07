# -*- coding:utf-8 -*-

def convert_to_decimal(from_n, number):
	n = from_n

	if n in [x for x in range(27) if x != 10]:
		result = 0

		number = str(number)[::-1]
		i = 0
		for digit in number:
			if digit in [chr(x) for x in range(65, 91)]:
				result += n**i * (ord(digit) - 55)
			else:
				result += n**i * int(digit)
			i += 1

		return result

	elif n == 10:
		return number
	else:
		return -1

""" 
	Convert from/to bases in [2;26]
	Returns result under string form 
	If base from/to isn't in [2;26] range, returns -1
"""
def convert(from_n, to_m, number):
	
	if from_n == to_m:
		return number

	elif (from_n in range(2, 27)) and (to_m in range(2, 27)): 

		N = 0
		n = from_n
		m = to_m

		RList = []

		# conversion to decimal
		if n != 10:

			N = convert_to_decimal(from_n, number)

		else:
			N = int(number)

		R = 0
		Q = 1		
		result = ""

		while Q != 0:

			Q = N // m
			R = N % m
			N = Q
			RList.append(R)

		RList.reverse()

		for elm in RList:
			if elm > 9:
				result += str(chr(elm + 55))
			else:
				result += str(elm)

		return result

	# if (from_n ; to_n) not in [2:26]
	else :
		return -1

