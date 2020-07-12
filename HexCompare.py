# Der3k Burrola
# July 2020
# Orange Hex Compare

import binascii
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getHexOf_OLD(file):
	hexString = '    '
	with open(file, 'rb') as f:
    # Change 100 to read from the length of entire file
		for x in range(100):
			# Reads one byte at a time
			content = f.read(1)
			# Converts to hex then to useable string
			pw_bytes = binascii.hexlify(content)
			pw_bytes = pw_bytes.decode("utf-8")
			
			# Don't split string here. Split it only when showing the files separately
			if((x > 0) and ((x+1) % 4 == 0)):
				hexString = hexString + str(pw_bytes) + '    ' 
			else:
				hexString = hexString + str(pw_bytes) + ' '
	return hexString

def getHexOf(file):
	hexString = '    '
	with open(file, 'rb') as f:
    # Change 100 to read from the length of entire file
		for x in range(1000):
			# Reads one byte at a time
			content = f.read(1)
			# Converts to hex then to useable string
			pw_bytes = binascii.hexlify(content)
			pw_bytes = pw_bytes.decode("utf-8")
			
			hexString = hexString + str(pw_bytes)
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

def compareFiles(file1, file2):
	for i in range( len(file1) ):
		if((i%2==0) and (i > 2)):
			byte1 = file1[i] + file1[i+1]
			byte2 = file2[i] + file2[i+1]
			if(byte1 != byte2):
				print('Byte at: ' + str(i) + ' are different!')


file1Hex = pickFile()
file2Hex = pickFile()
printFile(1,file1Hex)
print('-------------------')
printFile(2,file2Hex)
print('-------------------')
compareFiles(file1Hex, file2Hex)