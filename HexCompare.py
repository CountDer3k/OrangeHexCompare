import binascii
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getHexOf(file):
	hexString = '    '
	with open(file, 'rb') as f:
    # Change 100 to read from the length of entire file
		for x in range(100):
			# Reads one byte at a time
			content = f.read(1)
			# Converts to hex then to useable string
			pw_bytes = binascii.hexlify(content)
			pw_bytes = pw_bytes.decode("utf-8")
			if((x > 0) and ((x+1) % 4 == 0)):
				hexString = hexString + str(pw_bytes) + '    ' 
			else:
				hexString = hexString + str(pw_bytes) + ' '
	return hexString

def pickFile():
	print()
	Tk().withdraw()
	file = askopenfilename()
	fileHex = getHexOf(file)
	return fileHex

def printFile(num, file):
	print('File ' + str(num) + ': ')
	print(file)



file1Hex = pickFile()
file2Hex = pickFile()
printFile(1,file1Hex)
print('-------------------')
printFile(2,file2Hex)
